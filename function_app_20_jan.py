import base64
from datetime import datetime
import json
import logging
import os
import time
import random

# Third-party imports
import azure.functions as func
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.auth import default
import requests
from supabase import create_client, Client

# Local imports
from new import sections2
from prompts import (
    WEBSITE_PLAN_PROMPT,
    DESIGN_BLUEPRINT_PROMPT,
    WEBSITE_CODE_PROMPT,
    DESIGN_FEEDBACK_PROMPT,
    CODE_REFINEMENT_PROMPT,
    COMPONENT_STRUCTURE_PROMPT,
)

sections = sections2
# Initialize the Supabase client
supabase_url: str = os.environ.get("SUPABASE_URL")
supabase_key: str = os.environ.get("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    error_details = {
        "error_type": "ConfigError",
        "error_message": "Supabase credentials not found in environment variables",
        "missing_vars": [
            k
            for k, v in {
                "SUPABASE_URL": supabase_url,
                "SUPABASE_KEY": supabase_key,
            }.items()
            if not v
        ],
    }
    raise Exception(json.dumps(error_details))

try:
    supabase: Client = create_client(supabase_url, supabase_key)
    # Test connection
    supabase.table("websites").select("count").limit(1).execute()
    logging.info("Supabase client initialized and connected successfully")
except Exception as e:
    error_details = {
        "error_type": type(e).__name__,
        "error_message": str(e),
        "supabase_url": (
            supabase_url[:10] + "..." if supabase_url else None
        ),  # Only show part of URL for security
    }
    raise Exception(json.dumps(error_details))

# Initialize Azure GPT-4 API settings
AZURE_KEY = os.environ.get("AZURE_KEY")
AZURE_KEY2 = os.environ.get("AZURE_KEY2")
AZURE_KEY3 = os.environ.get("AZURE_KEY3")
GPT4o_ENDPOINT = os.environ.get("GPT4o_ENDPOINT")
GPT4o_MINI_ENDPOINT = os.environ.get("GPT4o_MINI_ENDPOINT")
O1_PREVIEW_ENDPOINT = os.environ.get("O1_PREVIEW_ENDPOINT")
O1_MINI_ENDPOINT = os.environ.get("O1_MINI_ENDPOINT")
O1_MINI_ENDPOINT2 = os.environ.get("O1_MINI_ENDPOINT2")
GPT4o_MINI_AIWB_ENDPOINT = os.environ.get("GPT4o_MINI_AIWB_ENDPOINT")
CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY")

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://aiwebsitebuilder.tech",
    "https://www.aiwebsitebuilder.tech",
]

# Load mock responses
with open("mock_responses_2.json", "r") as f:
    MOCK_RESPONSES = json.load(f)


def pre_assemble_pages(website_componentised_structure, component_codes):
    """
    Creates markdown formatted pages from components before AI enhancement
    """
    html_boilerplate_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
     <!--PAID Tailwind CSS CDN -- DO NOT CHANGE -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/framer-motion@11.15.0/dist/framer-motion.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/particlesjs/2.2.3/particles.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Swiper/11.0.5/swiper-bundle.min.js"></script>
    <!-- Add required scripts -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/3.13.5/cdn.min.js" defer></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://aiwebsitebuilder.tech/form-capture.js"></script>
</head>
<body>"""

    html_boilerplate_end = """
</body>
</html>"""

    markdown_output = ""

    try:
        structure = json.loads(website_componentised_structure)

        for page_name, components in structure.items():
            page_content = []
            page_content.append(html_boilerplate_start.format(title=page_name))

            for component_id in components:
                if component_id in component_codes:
                    page_content.append(component_codes[component_id])
                else:
                    logging.warning(
                        f"Missing component {component_id} for page {page_name}"
                    )

            page_content.append(html_boilerplate_end)

            markdown_output += f"\n## {page_name}.html\n```html\n"
            markdown_output += "\n".join(page_content)
            markdown_output += "\n```\n"

        markdown_output += "\n## All Files Completed"
        # print(markdown_output)
        return markdown_output

    except Exception as e:
        logging.error(f"Error pre-assembling pages: {e}")
        raise


def generate_request_id(user_id: str, website_id: str) -> str:
    """
    Creates a traceable but unique request ID
    Format: user_id__website_id__timestamp
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{user_id}__{website_id}__{timestamp}"


def execute_step(
    step_name: str, request_id: str, func, test_mode: bool = False, *args, **kwargs
):
    """
    Wrapper function to handle execution, retries, and logging.
    Now supports test mode with mock responses.
    """
    max_retries = 2
    attempt = 0

    # If test mode is enabled and we have a mock response, return it
    if test_mode:
        if step_name not in MOCK_RESPONSES:
            logging.warning(f"No mock response for {step_name}, using real function")
        else:
            log_entry = {
                "request_id": request_id,
                "user_id": kwargs.get("user_id"),
                "website_id": kwargs.get("website_id"),
                "step": step_name,
                "status": "success (mock)",
                "timestamp": datetime.now().isoformat(),
            }
            try:
                supabase.table("website_generation_logs").insert(log_entry).execute()
            except Exception as e:
                logging.warning(f"Failed to log mock step: {e}")
            return MOCK_RESPONSES[step_name]

    while attempt < max_retries:
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start_time

            log_entry = {
                "request_id": request_id,
                "user_id": kwargs.get("user_id"),
                "website_id": kwargs.get("website_id"),
                "step": step_name,
                "status": "success",
                "attempt": attempt + 1,
                "duration": duration,
                "timestamp": datetime.now().isoformat(),
                "error": None,
            }

            try:
                supabase.table("website_generation_logs").insert(log_entry).execute()
            except Exception as e:
                logging.warning(f"Failed to log success: {e}")
            return result

        except Exception as e:
            attempt += 1
            error_details = {
                "step": step_name,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "attempt": attempt,
                "user_id": kwargs.get("user_id"),
                "website_id": kwargs.get("website_id"),
            }

            # Try to get more error details if it's a Supabase error
            if hasattr(e, "code") or hasattr(e, "details"):
                error_details.update(
                    {
                        "error_code": getattr(e, "code", None),
                        "error_details": getattr(e, "details", None),
                        "error_hint": getattr(e, "hint", None),
                    }
                )

            logging.error(
                f"Step {step_name} failed: {json.dumps(error_details, indent=2)}"
            )

            try:
                log_entry = {
                    "request_id": request_id,
                    "user_id": kwargs.get("user_id"),
                    "website_id": kwargs.get("website_id"),
                    "step": step_name,
                    "status": "failed",
                    "attempt": attempt,
                    "error": json.dumps(error_details),
                    "timestamp": datetime.now().isoformat(),
                }
                supabase.table("website_generation_logs").insert(log_entry).execute()
            except Exception as log_error:
                logging.warning(f"Failed to log error: {log_error}")

            if attempt == max_retries:
                raise Exception(json.dumps(error_details))

            time.sleep(2**attempt)


def call_google_ai_api(messages, model="gemini-2.0-flash-exp"):
    # gemini-1.5-flash-002
    """
    Call Google's Vertex AI API with the provided messages.
    """
    # Google Cloud configuration
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
    location_id = "us-central1"
    model_id = model

    # Get credentials from environment variable
    credentials_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if not credentials_json:
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS_JSON is not set")

    try:
        # Get credentials from environment variable
        credentials_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
        if not credentials_json:
            raise ValueError(
                "GOOGLE_APPLICATION_CREDENTIALS_JSON environment variable is not set"
            )

        # Decode base64 and create credentials
        try:
            decoded_credentials = base64.b64decode(credentials_json).decode("utf-8")
            credentials_dict = json.loads(decoded_credentials)

            credentials = service_account.Credentials.from_service_account_info(
                credentials_dict,
                scopes=["https://www.googleapis.com/auth/cloud-platform"],
            )
        except Exception as e:
            logging.error(f"Error decoding credentials: {str(e)}")
            raise ValueError("Invalid credentials format")

        # Project settings
        project_id = credentials_dict.get("project_id")
        if not project_id:
            raise ValueError("Project ID not found in credentials")

        location_id = "us-central1"

        # Ensure credentials are fresh
        if not credentials.valid:
            credentials.refresh(Request())

        access_token = credentials.token
        if not access_token:
            raise ValueError("Failed to obtain access token")

        endpoint = f"https://{location_id}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{location_id}/publishers/google/models/{model_id}:generateContent"
        geminimessages = messages
        system = messages[0]["content"]
        geminimessages.pop(0)

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": messages[0]["content"]}],
                }
            ],
            "systemInstruction": {"role": "user", "parts": [{"text": system}]},
            "generationConfig": {
                # "temperature": 0.7,
                "maxOutputTokens": 8192,
            },
        }

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        logging.info(f"Calling Google AI API: {endpoint}")
        # logging.info(f"Payload: {payload}")

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            logging.info("google response recieved")
            response.raise_for_status()

            logging.info(response.json())
            # data = response.json()
            # # Direct Gemini response parsing - taking the last response chunk
            # last_chunk = data[-1]  # Get the last item in the response list
            # content = last_chunk["candidates"][0]["content"]["parts"][0]["text"]

            return response.json()

        except requests.RequestException as e:
            if response:
                logging.error(response.text)
            logging.error(f"Error calling Google AI API: {e}")
            raise

    except Exception as e:
        logging.error(f"Error in Google AI API call: {e}")
        raise


def call_google_llama(messages, model="meta/llama-3.1-8b-instruct-maas"):
    """
    Call Google's Vertex AI API with the provided messages.
    """
    # Google Cloud configuration
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
    location_id = "us-central1"
    model_id = model

    # Get credentials from environment variable
    credentials_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if not credentials_json:
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS_JSON is not set")

    try:
        # Decode and parse credentials
        credentials = json.loads(base64.b64decode(credentials_json))

        # Get credentials and project
        credentials, project = default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )

        # Refresh token if necessary
        if not credentials.valid:
            credentials.refresh(Request())

        # Get access token
        access_token = credentials.token
        if not access_token:
            raise ValueError("Failed to get access token")

        endpoint = f"https://{location_id}-aiplatform.googleapis.com/v1beta1/projects/{project_id}/locations/{location_id}/endpoints/openapi/chat/completions"

        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "max_tokens": 8192,
        }

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        logging.info(f"Calling Google AI API: {endpoint}")
        # logging.info(f"Payload: {payload}")

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            logging.info("google response recieved")
            response.raise_for_status()

            logging.info(response.json())

            return response.json()

        except requests.RequestException as e:
            if response:
                logging.error(response.text)
            logging.error(f"Error calling Google AI API: {e}")
            raise

    except Exception as e:
        logging.error(f"Error in Google AI API call: {e}")
        raise


def call_claude_api(messages):
    endpoint = "https://api.anthropic.com/v1/messages"

    # Convert messages to Claude's format if needed
    claude_messages = messages
    system = messages[0]["content"]
    claude_messages.pop(0)

    payload = {
        "model": "claude-3-5-sonnet-20241022",
        "system": system,
        "max_tokens": 8000,
        "messages": claude_messages,
    }

    headers = {
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }

    logging.info("Calling Claude API")
    # logging.info(f"Payload: {payload}")

    claude_response = None
    try:
        claude_response = requests.post(endpoint, headers=headers, json=payload)
        claude_response.raise_for_status()
        # print(claude_response.json())
        return claude_response.json()
    except requests.RequestException as e:
        if claude_response:
            logging.error(claude_response.raw)
        logging.error(f"Error calling Claude API: {e}")
        raise


def call_gpt4_api(messages, model="gpt-4o-mini"):
    auth_key = AZURE_KEY

    if model == "claude-3-5-sonnet-20241022":
        return call_claude_api(messages)
    if model == "gemini-1.5-flash-002" or model == "gemini-1.5-pro-002":
        return call_google_ai_api(messages, model)
    if (
        model == "meta/llama-3.2-90b-vision-instruct-maas"
        or model == "meta/llama-3.1-8b-instruct-maas"
        or model == "meta/llama-3.1-70b-instruct-maas"
        or model == "meta/llama-3.1-405b-instruct-maas"
    ):
        return call_google_llama(messages, model)
    # endpoint = GPT4o_ENDPOINT
    if model == "gpt-4o-mini":
        endpoint = GPT4o_MINI_ENDPOINT
        payload = {
            "messages": messages,
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 4000,
        }
    elif model == "gpt-4o-mini-aiwb":
        endpoint = GPT4o_MINI_AIWB_ENDPOINT
        auth_key = AZURE_KEY2
        payload = {
            "messages": messages,
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 4000,
        }
    elif model == "o1-preview":
        endpoint = O1_PREVIEW_ENDPOINT
        messages[0]["role"] = "user"
        payload = {
            # messages without system message
            "messages": messages,
            "max_completion_tokens": 1000,
        }
    elif model == "o1-mini":
        # endpoint = O1_MINI_ENDPOINT
        endpoint = O1_MINI_ENDPOINT2
        auth_key = AZURE_KEY3
        messages[0]["role"] = "user"
        payload = {
            # messeges without system message
            "messages": messages,
            "max_completion_tokens": 50000,
        }
        # print(payload)
    else:
        endpoint = GPT4o_ENDPOINT
        payload = {
            "messages": messages,
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 4000,
        }

    headers = {
        "Content-Type": "application/json",
        "api-key": auth_key,
    }
    logging.info(f"Calling {model} with endpoint: {endpoint}")
    # logging.info(f"Payload: {payload}")
    gpt4_response = None
    try:
        gpt4_response = requests.post(endpoint, headers=headers, json=payload)
        gpt4_response.raise_for_status()
        return gpt4_response.json()
    except requests.RequestException as e:
        error_details = {
            "status_code": gpt4_response.status_code if gpt4_response else None,
            "error_message": str(e),
            "response_text": gpt4_response.text if gpt4_response else None,
            "response_headers": dict(gpt4_response.headers) if gpt4_response else None,
            "request_url": endpoint,
            "request_method": "POST",
            "request_headers": headers,
            "model": model,
        }

        logging.error("GPT-4 API Error Details:")
        for key, value in error_details.items():
            logging.error(f"{key}: {value}")

        raise Exception(f"API call failed for model {model}: {str(e)}")


def parse_markdown(markdown):
    sections = markdown.split("## ")[1:]  # Split the markdown into sections
    file_contents = []
    for section in sections:
        lines = section.split("\n")
        filename = lines[0].strip()  # The filename is the first line of the section
        print("filename is: ", filename)
        code_block = "\n".join(lines[1:])  # The rest of the section is the code block
        if "```html" in code_block:
            code_lines = (
                code_block.split("```html")[1].split("```")[0].split("\n")
            )  # Extract the code lines and remove trailing backticks
            file_content = "\n".join(
                code_lines[1:]
            ).strip()  # Join the code lines into a single string
            file_contents.append((filename, file_content))
    return file_contents

    # def pre_assemble_pages(website_componentised_structure, component_codes):
    #     """
    #     Creates markdown formatted pages from components before AI enhancement
    #     """
    #     html_boilerplate_start = """<!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <script src="https://cdn.tailwindcss.com"></script>
    #     <script src="https://kit.fontawesome.com/037776171a.js" crossorigin="anonymous"></script>
    #     <title>{title}</title>
    # </head>
    # <body>"""

    #     html_boilerplate_end = """<div class="AI WEBSITE BUILDER POPUP fixed bottom-0 left-0 right-0 bg-gradient-to-r from-purple-600 to-indigo-600 text-white p-3 text-center shadow-lg">
    #   <div class="container mx-auto flex flex-col sm:flex-row items-center justify-center gap-4">
    #     <p class="text-sm font-medium">
    #       This website was created with AI Website Builder
    #     </p>
    #     <a
    #       href="https://aiwebsitebuilder.tech"
    #       target="_blank"
    #       rel="noopener noreferrer"
    #       class="inline-flex items-center px-4 py-1.5 text-sm font-semibold bg-white text-purple-600 rounded-full hover:bg-purple-50 transition-colors duration-200"
    #     >
    #       Build Your Free Website →
    #     </a>
    #   </div>
    # </div>
    # </body>
    # </html>"""

    #     markdown_output = ""

    #     try:
    #         structure = json.loads(website_componentised_structure)

    #         for page_name, components in structure.items():
    #             page_content = []
    #             page_content.append(html_boilerplate_start.format(title=page_name))

    #             for component_id in components:
    #                 if component_id in component_codes:
    #                     page_content.append(component_codes[component_id])
    #                 else:
    #                     logging.warning(
    #                         f"Missing component {component_id} for page {page_name}"
    #                     )

    #             page_content.append(html_boilerplate_end)

    #             markdown_output += f"\n## {page_name}.html\n```html\n"
    #             markdown_output += "\n".join(page_content)
    #             markdown_output += "\n```\n"

    #         markdown_output += "\n## All Files Completed"
    #         # print(markdown_output)
    #         return markdown_output

    #     except Exception as e:
    #         logging.error(f"Error pre-assembling pages: {e}")
    #         raise


def delete_existing_pages(user_id: str, website_id: str) -> bool:
    """Delete existing pages for the website before generating new ones"""
    try:
        result = supabase.table("pages").delete().eq("website_id", website_id).execute()
        return True
    except Exception as e:
        raise Exception(f"Failed to delete existing pages: {str(e)}")


def fetch_conversation_data(user_id: str, website_id: str) -> dict:
    """Fetch website details and chat conversation from Supabase"""
    try:
        # Use the exact same query that works in the test
        response = (
            supabase.table("websites")
            .select("website_name, website_description, chat_conversation")
            .eq("user_id", user_id)
            .eq("id", website_id)
            .execute()
        )

        if not response.data:
            raise Exception(f"No data found for website_id: {website_id}")

        logging.info(f"Supabase response: {response}")
        logging.info(f"Data: {response.data}")

        return response.data[0]

    except Exception as e:
        error_details = {
            "error_type": type(e).__name__,
            "error_message": str(e),
            "error_code": getattr(e, "code", None),
            "error_details": getattr(e, "details", None),
            "error_hint": getattr(e, "hint", None),
            "user_id": user_id,
            "website_id": website_id,
        }
        logging.error(f"Database error details: {json.dumps(error_details, indent=2)}")
        raise Exception(json.dumps(error_details))


def save_generated_pages(user_id: str, website_id: str, website_code: str) -> bool:
    """Parse and save generated pages to Supabase"""
    try:
        # Parse markdown into separate pages
        page_codes = parse_markdown(website_code)
        all_pages = []

        # Prepare bulk insert data
        pages_to_insert = [
            {
                "user_id": user_id,
                "website_id": website_id,
                "title": page_name,
                "content": page_code,
            }
            for page_name, page_code in page_codes
        ]

        # Save all pages in one operation
        supabase.table("pages").insert(pages_to_insert).execute()

        # Update website with page list
        supabase.table("websites").update(
            {"pages": [page[0] for page in page_codes], "status": "completed"}
        ).eq("user_id", user_id).eq("id", website_id).execute()

        return True
    except Exception as e:
        raise Exception(f"Failed to save generated pages: {str(e)}")


def create_website_plan(website_data: dict, model: str, website_id: str) -> str:
    """
    Step 1: Create structured website plan from user conversation
    """
    messages = [
        {"role": "system", "content": WEBSITE_PLAN_PROMPT},
        {
            "role": "user",
            "content": f""" Here are the details of the website added by the user and the conversation where the user explains what they want for the website:

Website Name: {website_data['website_name']}

Description: {website_data['website_description']}

User Conversation: 

{website_data['chat_conversation']}

Please refine this into a detailed website plan using the provided guidelines.
        """,
        },
    ]

    response = call_gpt4_api(messages, model)
    return parse_ai_response(response, model)


###########################################
# Original Website Generation Functions   #
# (Kept for reference/fallback)          #
###########################################


def create_design_blueprint(structured_plan: str, model: str) -> str:
    """
    Step 2: Expand plan into detailed design blueprint
    """
    messages = [
        {"role": "system", "content": DESIGN_BLUEPRINT_PROMPT},
        {
            "role": "user",
            "content": f"""Here is the website plan: 
         
        {structured_plan}
        
        Please create a detailed design blueprint for each section following the provided guidelines. 
        """,
        },
    ]

    response = call_gpt4_api(messages, model)
    return parse_ai_response(response, model)


def generate_website_code(design_blueprint: str, model: str, website_id: str) -> str:
    """
    Step 3: Generate initial website code
    """
    messages = [
        {"role": "system", "content": WEBSITE_CODE_PROMPT},
        {
            "role": "user",
            "content": f"""Here is the design blueprint: 
            
            {design_blueprint}
            
            Please generate the complete code for the website following the provided instructions.
            
            """,
        },
    ]

    response = call_gpt4_api(messages, model)
    return parse_ai_response(response, model)


###########################################
# New Component-Based Generation System   #
###########################################


def fetch_available_categories(website_id: str) -> list:
    """
    Fetch only unique component categories from Supabase
    """
    try:
        response = (
            # TODO: remove after testing
            supabase.table("components_new")
            .select("section_type")
            .eq("is_active", True)
            .execute()
        )

        # Get unique categories
        categories = list(set(item["section_type"] for item in response.data))
        return categories
    except Exception as e:
        raise Exception(f"Failed to fetch categories: {str(e)}")


def fetch_random_component(category: str) -> dict:
    """
    Fetch one random component from a category
    """
    try:
        response = (
            supabase.table("random_components")
            .select("id, component_id")
            .eq("section_type", category)
            .eq("is_active", True)
            .limit(1)
            .execute()
            # .select("id, component_id")
            # .eq("section_type", category)
            # .eq("is_active", True)
            # .order("id", desc=None)  # Order by id to get consistent results
            # .execute()
        )

        if not response.data:
            raise Exception(f"No components found for category: {category}")

        # Get all matching components and randomly select one using Python

        return random.choice(response.data)
    except Exception as e:
        raise Exception(f"Failed to fetch random component: {str(e)}")


def fetch_component_codes(component_ids: list) -> dict:
    """
    Fetch code only for selected components
    """
    try:
        response = (
            supabase.table("components")
            .select("component_id, code")
            .in_("component_id", component_ids)
            .execute()
        )

        return {comp["component_id"]: comp["code"] for comp in response.data}
    except Exception as e:
        raise Exception(f"Failed to fetch component codes: {str(e)}")


def generate_component_structure(
    structured_plan: str, available_categories: list, model: str, website_id: str
) -> dict:
    """
    Generate component category structure based on website plan
    """
    # Format available categories for the prompt
    categories_text = "\n".join(f"- {cat}" for cat in available_categories)

    messages = [
        {
            "role": "system",
            "content": COMPONENT_STRUCTURE_PROMPT,
        },
        {
            "role": "user",
            "content": f"""
            Available component categories:
            {categories_text}
            
            Here is the website plan:
            {structured_plan}
            Please assign appropriate component categories to each section.
            
            Remember:
            1. Only use categories from the provided list
            2. Return a valid JSON object
            3. Use the exact category names as provided
            4. Do not add any extra text or formatting, just the JSON""",
        },
    ]

    response = call_gpt4_api(messages, model)
    raw_response = parse_ai_response(response, model)
    logging.info(f"AI Response for component structure: {raw_response}")

    try:
        # Try to clean the response if it has extra text
        if "```json" in raw_response:
            raw_response = raw_response.split("```json")[1].split("```")[0]
        elif "```" in raw_response:
            raw_response = raw_response.split("```")[1].split("```")[0]

        # Remove any leading/trailing whitespace
        raw_response = raw_response.strip()

        structure = json.loads(raw_response)

        # Validate structure against available categories
        for page in structure.values():
            for category in page.values():
                if category not in available_categories:
                    raise ValueError(f"Invalid category in response: {category}")
        return structure
    except json.JSONDecodeError as e:
        error_details = {
            "error": "Invalid JSON structure",
            "raw_response": raw_response,
            "json_error": str(e),
        }
        logging.error(f"JSON Parse Error: {json.dumps(error_details, indent=2)}")
        raise Exception(
            f"AI returned invalid JSON structure: {json.dumps(error_details, indent=2)}"
        )
    except Exception as e:
        raise Exception(f"Error processing AI response: {str(e)}")


def select_random_components(
    category_structure: dict, available_categories: list, website_id: str
) -> dict:
    """
    Select random components for each category in the structure
    First fetches a navbar to use across all pages
    """
    try:
        # First get a random navbar
        navbar = fetch_random_component("Navbar")
        navbar_id = navbar["component_id"]
        selected_ids = [navbar_id]  # Start with navbar
        structure_with_ids = {}

        # For each page, start with navbar and add other components
        for page, sections in category_structure.items():
            structure_with_ids[page] = [navbar_id]  # Add navbar first
            for section, category in sections.items():
                if category in available_categories and category != "Navbar":
                    component = fetch_random_component(category)
                    component_id = component["component_id"]
                    structure_with_ids[page].append(component_id)
                    if (
                        component_id not in selected_ids
                    ):  # Avoid duplicating navbar in selected_ids
                        selected_ids.append(component_id)

        # Fetch codes for all components (including navbar)
        component_codes = fetch_component_codes(selected_ids)

        return {"structure": json.dumps(structure_with_ids), "codes": component_codes}
    except Exception as e:
        error_details = {
            "error_type": type(e).__name__,
            "error_message": str(e),
            "step": "select_components",
            "details": "Error while selecting components and navbar",
        }
        logging.error(
            f"Component selection error: {json.dumps(error_details, indent=2)}"
        )
        raise Exception(json.dumps(error_details))


def assemble_template(components_data: dict, website_id: str) -> str:
    """
    Wrapper for pre_assemble_pages
    """
    return pre_assemble_pages(components_data["structure"], components_data["codes"])


def generate_website_code(
    website_plan: str, website_assembled_template: str, model: str
) -> str:
    """
    Step 3: Generate initial website code
    """
    messages = [
        {"role": "system", "content": WEBSITE_CODE_PROMPT},
        {
            "role": "user",
            "content": f"""Here is the website plan: 
            
            {website_plan}
            
            Here is the template that is generated, 
            
            {website_assembled_template}
            
            
            Please customise and furnish the code according to the plan, and make it ready to go live.
            
            """,
        },
    ]

    response = call_gpt4_api(messages, model)
    return parse_ai_response(response, model)


def generate_design_feedback(website_code: str, model: str) -> str:
    """
    Step 4: Generate feedback on the website design
    """
    messages = [
        {"role": "system", "content": DESIGN_FEEDBACK_PROMPT},
        {
            "role": "user",
            "content": f"""
         
            Here is the website code generated according to the user requirements:  

            {website_code}

            Your task is to:  
            1. Review the code thoroughly for layout, design, and user experience.  
            2. Provide detailed feedback on how to make the design more visually stunning, unique, and functional.  
            3. Highlight specific suggestions for improving layout, color schemes, animations, interactivity, responsiveness, and usability.  
            4. Ensure the feedback aligns with the user's original intent while enhancing the website's overall quality.  

            Respond with actionable recommendations in the specified format.""",
        },
    ]

    response = call_gpt4_api(messages, model)
    return parse_ai_response(response, model)


def refine_website_code(initial_code: str, feedback: str, model: str) -> str:
    """
    Step 5: Refine website code based on feedback
    """
    messages = [
        {"role": "system", "content": CODE_REFINEMENT_PROMPT},
        {
            "role": "user",
            "content": f""" Here is the initial website code:
            
            {initial_code}
            
            Here are the identified issues and suggestions:
            
            {feedback}
            
            """,
        },
    ]

    response = call_gpt4_api(messages, model)
    return parse_ai_response(response, model)


def parse_ai_response(response: dict, model: str) -> str:
    """
    Parse AI response based on model type
    """
    try:
        if model == "claude-3-5-sonnet-20241022":
            return response.get("content")[0].get("text")
        elif model in ["gemini-1.5-flash-002", "gemini-1.5-pro-002"]:
            return response["candidates"][0]["content"]["parts"][0]["text"]
        else:  # GPT models
            return response.get("choices")[0].get("message").get("content")
    except Exception as e:
        raise Exception(f"Failed to parse AI response: {str(e)}")


def extract_request_params(req: func.HttpRequest) -> dict:
    """Helper function to extract and validate request parameters"""
    params = {
        "user_id": req.params.get("user_id"),
        "website_id": req.params.get("website_id"),
        "model": req.params.get("model", "gpt-4o-mini"),
    }

    # Try getting params from body if not in query
    if not params["user_id"] or not params["website_id"]:
        try:
            body = req.get_json()
            params["user_id"] = params["user_id"] or body.get("user_id")
            params["website_id"] = params["website_id"] or body.get("website_id")
        except ValueError:
            pass

    return params


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="code_website")
def get_website_code(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Extract and validate parameters
        params = extract_request_params(req)
        user_id = params["user_id"]
        website_id = params["website_id"]
        model = params["model"]

        if not user_id or not website_id:
            return func.HttpResponse(
                json.dumps(
                    {
                        "success": False,
                        "error": "Missing required parameters: user_id and website_id",
                    }
                ),
                status_code=400,
            )

        # Initialize request tracking
        request_id = generate_request_id(user_id, website_id)
        logging.info(f"Starting website generation - Request ID: {request_id}")

        # Update website status to 'processing'
        supabase.table("websites").update({"status": "processing"}).eq(
            "id", website_id
        ).execute()

        try:
            # Step 0: Delete existing pages
            execute_step(
                "delete_pages",
                request_id,
                delete_existing_pages,
                user_id=user_id,
                website_id=website_id,
            )

            # Step 1: Fetch conversation data
            website_data = execute_step(
                "fetch_data",
                request_id,
                fetch_conversation_data,
                user_id=user_id,
                website_id=website_id,
            )

            # Step 2: Create structured plan
            structured_plan = execute_step(
                "create_plan",
                request_id,
                create_website_plan,
                website_data=website_data,
                website_id=website_id,
                model=model,
                # test_mode=True,  # This will use mock response from mock_responses_2.json
            )

            # Step 3: Fetch available categories
            available_categories = execute_step(
                "fetch_categories",
                request_id,
                fetch_available_categories,
                website_id=website_id,
            )

            # Step 4: Generate component structure
            component_structure = execute_step(
                "generate_structure",
                request_id,
                generate_component_structure,
                structured_plan=structured_plan,
                available_categories=available_categories,
                model=model,
                website_id=website_id,
            )

            # Step 5: Select random components
            selected_components = execute_step(
                "select_components",
                request_id,
                select_random_components,
                category_structure=component_structure,
                available_categories=available_categories,
                website_id=website_id,
            )

            # Step 6: Assemble template
            initial_code = execute_step(
                "assemble_template",
                request_id,
                assemble_template,
                components_data=selected_components,
                website_id=website_id,
            )

            # Step 7: Generate initial website code
            website_code = execute_step(
                "generate_code",
                request_id,
                generate_website_code,
                website_plan=structured_plan,
                website_assembled_template=initial_code,
                model=model,
                website_id=website_id,
            )

            # # Step 8: Generate feedback
            # feedback = execute_step(
            #     "generate_feedback",
            #     request_id,
            #     generate_design_feedback,
            #     website_code=website_code,
            #     model=model,
            # )

            # # Step 9: Final code refinement
            # final_code = execute_step(
            #     "refine_code",
            #     request_id,
            #     refine_website_code,
            #     initial_code=website_code,
            #     feedback=feedback,
            #     model=model,
            # )

            # Step 10: Save generated pages
            execute_step(
                "save_pages",
                request_id,
                save_generated_pages,
                user_id=user_id,
                website_id=website_id,
                # changed final_code to website_code for removing feedback and refinement
                website_code=website_code,
            )

            return func.HttpResponse(
                json.dumps(
                    {
                        "success": True,
                        "request_id": request_id,
                        "message": "Website generated successfully",
                    }
                )
            )

        except Exception as e:
            # Rollback: Update website status to 'failed' and delete any generated pages
            supabase.table("websites").update({"status": "failed"}).eq(
                "id", website_id
            ).execute()
            delete_existing_pages(user_id, website_id)
            raise e

    except Exception as e:
        error_msg = str(e)
        logging.error(f"Error in website generation: {error_msg}")

        return func.HttpResponse(
            json.dumps({"success": False, "error": error_msg}), status_code=500
        )
