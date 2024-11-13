import base64
from datetime import datetime
import json
from logging.handlers import RotatingFileHandler
import os
import time
import azure.functions as func
import logging
import json
import os
from google.auth import default
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from new import sections2


from supabase import create_client, Client


import requests

sections = sections2
# Initialize the Supabase client
supabase_url: str = os.environ.get("SUPABASE_URL")
supabase_key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

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


def call_google_ai_api(messages, model="gemini-1.5-flash-002"):
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
        # logging.info(payload)
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
        # if gpt4_response:
        #     logging.error(gpt4_response.raw)
        # logging.error(f"Error calling GPT-4 API11: {e}")
        error_details = {
            "status_code": gpt4_response.status_code,
            "error_message": str(e),
            "response_text": gpt4_response,
            "response_json": gpt4_response,
            "response_headers": dict(gpt4_response.headers),
            "request_url": gpt4_response.url,
            "request_method": gpt4_response.request.method,
            "request_headers": (dict(gpt4_response.request.headers)),
            # "request_body": payload,
        }

        logging.error("Detailed GPT-4 API Error:")
        for key, value in error_details.items():
            logging.error(f"{key}: {value}")

        raise


def get_componentized_structure(
    website_name: str,
    website_description: str,
    chat_conversation: str,
    # sections: str,
    model,
) -> dict:
    model = "gpt-4o-mini"
    sample_output = {
        "pagename": ["navbar-4", "layout-388", "portfolio-11", "footer-1"],
        "pagename": ["navbar-4", "layout-340", "footer-1"],
    }

    system_prompt = """
    you are an expert web developer. Your goal is to output a json for the component wise website structure based on the user requirements, using the sections provided to you, each page having consistant Navbar and Footer components as shown below.
    
    Remember, you are selecting components based on the layout and structure of the component, not the text, as that would be changed. So choose only from the given components, and no new components should be named.
    
    Keep max 3 pages, 3-10 components per page.

        Sample Output:
        {sample_output}
    Remember to give just the json, no backticks (```) no other text, no explantions. nothing excpet json, so that the json is parsable.
    
    You have blog-header, blog-post-header, career, contact, features, footer, hero, layout, portfolio, pricing, team, testimonials, event-header, event-item-header, faq, legal-pages, links, timeline, comparision, footer, logo, contact, gallery, navbar, contact-modal, header, portfolio, content, portfolio-header and hero components as defined below.

        {sections}

        """
    # Prepare payload for GPT-4 API
    messages = [
        {
            "role": "system",
            "content": system_prompt.format(
                sections=sections, sample_output=sample_output
            ),
        },
        {
            "role": "user",
            "content": f"""Here is the details of the website the user wants to create: 
                         Website Name: {website_name} \n
                         Website Description: {website_description} \n
                         Chat Conversation: 
                         {chat_conversation}""",
        },
    ]

    # Call GPT-4 API
    try:
        response_json = call_gpt4_api(messages, model)
        return response_json
    except requests.RequestException as e:
        logging.error(f"Error calling GPT-4 API 2 for componentized structure: {e}")
        return {}


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


def pre_assemble_pages(website_componentised_structure, component_codes):
    """
    Creates markdown formatted pages from components before AI enhancement
    """
    html_boilerplate_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://kit.fontawesome.com/037776171a.js" crossorigin="anonymous"></script>
    <title>{title}</title>
</head>
<body>"""

    html_boilerplate_end = """<div class="AI WEBSITE BUILDER POPUP fixed bottom-0 left-0 right-0 bg-gradient-to-r from-purple-600 to-indigo-600 text-white p-3 text-center shadow-lg">
  <div class="container mx-auto flex flex-col sm:flex-row items-center justify-center gap-4">
    <p class="text-sm font-medium">
      This website was created with AI Website Builder
    </p>
    <a 
      href="https://aiwebsitebuilder.tech" 
      target="_blank" 
      rel="noopener noreferrer" 
      class="inline-flex items-center px-4 py-1.5 text-sm font-semibold bg-white text-purple-600 rounded-full hover:bg-purple-50 transition-colors duration-200"
    >
      Build Your Free Website →
    </a>
  </div>
</div>
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


def get_website_pages_codes(
    website_componentised_structure,
    chat_conversation,
    website_name,
    website_description,
    assembled_pages_md,
    model,
):
    system_prompt = f"""Please create an amazing, mesmerising, custom website for the user, based on the user's requirements and the template the user has provided. 
    The template is a starting point, and you are expected to use your knowledge, user's requirements and experience to fully furnish the website. from colours, to styling, to layout, to text, to images, to links, to consistant header and footer, to everything, you are expected to make sure the website is a masterpiece. Full complete implementation of the website, using HTML, Tailwind CSS and JavaScript(where needed). Do not add placeholder content, comment for further instructions or further implementations etc. Your job is to create a complete, fully functional, ready to publish website.
    
    Your job is not to fill the template, but to customise the website for the user. You can add, edit or remove any elements from the template, to make sure the website is a masterpiece.
    
    Expected Output:
    For the output you are expected to give the full code for each page in markdown format, as shown below, and nothing else. Do not add any Placeholders, comments, backticks (```) or any other text in your response.

    Only Respond with a Properly Formatted MARKDOWN with the HTML code for each HTML file(each page) of the website and Write ## All Files Completed at the end of the markdown file, after all the HTML code for each page.

    the markdown should include each codeblock seperatly with language specified as HTML, and heading as name of the file, and a final heading of code completed.
    
    Also, on each page there is an AI WEBSITE BUILDER POPUP, which should be added to the bottom of each page, and not removed.
    

    such as

    ## index.html
    ```html
    <html code here>
    ```
    
    ## about_us.html
    ```html
    <html code here>
    ```
    
    ## contact_us.html
    ```html
    <html code here>
    ```
    
    ## All Files Completed
    
    """
    user_prompt = f"""
    
    Here is the details of the website the user wants to create: 
                         Website Name: {website_name} \n
                         Website Description: {website_description} \n
                         Chat Conversation: 
                         {chat_conversation}
                         
                         assembled pages markdown:
                         {assembled_pages_md}
                         """
    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]

    # Call GPT-4 API
    try:
        final_response = ""
        while True:
            response_json = call_gpt4_api(messages, model)
            # logging.info(f"response_json: {response_json}")
            if model == "claude-3-5-sonnet-20241022":
                response_text = response_json.get("content")[0].get("text")
            elif model == "gemini-1.5-flash-002" or model == "gemini-1.5-pro-002":
                # last_chunk = response_json[-1]  # Get the last item in the response list
                response_text = response_json["candidates"][0]["content"]["parts"][0][
                    "text"
                ]
            else:
                response_text = (
                    response_json.get("choices")[0].get("message").get("content")
                )
            final_response += response_text + "\n"

            if response_text.strip().endswith("## All Files Completed"):
                break
            messages.append({"role": "assistant", "content": response_text})
            time.sleep(0.5)

        page_code = final_response
        # logging.info(f"page_code: {page_code}")
        return page_code
    except requests.RequestException as e:
        logging.error(f"Error calling GPT-4 API 3 for website Code: {e}")
        return "error calling GPT-4 API  4 for website code. \n Error: {e}"


def fetch_component_base_code(components):
    base_codes = {}
    missing_components = []

    try:
        # Single efficient query using in_
        response = (
            supabase.table("components")
            .select("component_id, code")
            .in_("component_id", components)
            .execute()
        )

        # Create mapping of fetched components
        supabase_components = {
            comp["component_id"]: comp["code"] for comp in response.data
        }

        # Map requested components to their codes
        for component in components:
            if component in supabase_components:
                base_codes[component] = supabase_components[component]
            else:
                missing_components.append(component)
                logging.warning(
                    f"Component {component} not found in database - skipping"
                )

    except Exception as e:
        logging.error(f"Error fetching components from Supabase: {e}")
        raise

    return base_codes


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="code_website")
def get_website_code(req: func.HttpRequest) -> func.HttpResponse:
    logger = logging.getLogger()
    # Create logs directory in a location we're sure has write permissions

    logger.info("Logging initialized successfully1")

    logger.info("Logging initialized successfully2")
    logging.info("Logging initialized successfully")

    logging.info("Python HTTP trigger function processed a request.")

    user_id = req.params.get("user_id")
    website_id = req.params.get("website_id")
    model = req.params.get("model")

    logging.info(f"user_id: {user_id}, website_id: {website_id}, model: {model}")
    if not user_id or not website_id:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            user_id = req_body.get("user_id")
            website_id = req_body.get("website_id")

    if user_id and website_id:
        # Fetch data from Supabase

        try:
            result = (
                supabase.table("pages").delete().eq("website_id", website_id).execute()
            )
            logging.info(
                f"Deleted {len(result.data)} existing pages for website_id: {website_id}"
            )
            print("working here 2")
            response = (
                supabase.table("websites")
                .select("website_name, website_description, chat_conversation")
                .eq("user_id", user_id)
                .eq("id", website_id)
                .execute()
            )
            print("working here 3")
            data = response.data
            if data:
                website_data = data[0]
                website_name = website_data.get("website_name")
                website_description = website_data.get("website_description")
                chat_conversation = website_data.get("chat_conversation")
                print("working here 4")

                try:
                    response_json = get_componentized_structure(
                        website_name,
                        website_description,
                        chat_conversation,
                        # sections,
                        model,
                    )
                    print("working here 5")
                    if response_json:
                        try:
                            if model == "claude-3-5-sonnet-20241022":
                                website_componentised_structure = response_json.get(
                                    "content"
                                )[0].get("text")
                            elif (
                                model == "gemini-1.5-flash-002"
                                or model == "gemini-1.5-pro-002"
                            ):  # last_chunk = response_json[-1]  # Get the last item in the response list
                                website_componentised_structure = response_json[
                                    "candidates"
                                ][0]["content"]["parts"][0]["text"]
                            else:
                                website_componentised_structure = (
                                    response_json.get("choices")[0]
                                    .get("message")
                                    .get("content")
                                )

                            logging.info(
                                f"website_componentised_structure: {website_componentised_structure}"
                            )
                            logging.info("working here 6")
                            # Save website componentised structure to Supabase
                            response = (
                                supabase.table("websites")
                                .update(
                                    {
                                        "website_componentised_structure": website_componentised_structure
                                    }
                                )
                                .eq("user_id", user_id)
                                .eq("id", website_id)
                                .execute()
                            )
                            logging.info("working here 7")

                            ## update website status

                            response = (
                                supabase.table("websites")
                                .update({"status": "45%"})
                                .eq("user_id", user_id)
                                .eq("id", website_id)
                                .execute()
                            )
                            logging.info("working here 8")
                            ## next step: website code

                            if response:
                                try:
                                    logging.info("working here 9")
                                    # Step 1: Extract all components
                                    try:
                                        website_componentized_structure_dict = (
                                            json.loads(website_componentised_structure)
                                        )
                                    except json.JSONDecodeError as e:

                                        logging.info(
                                            "Failed to parse the componentized structure:",
                                            e,
                                        )
                                    logging.info("working here 10")
                                    all_components = set()
                                    for (
                                        page_components
                                    ) in website_componentized_structure_dict.values():
                                        all_components.update(page_components)

                                    # Convert to list
                                    component_list = list(all_components)

                                    # Fetch component codes from Supabase
                                    components = fetch_component_base_code(
                                        component_list
                                    )

                                    assembled_pages_md = pre_assemble_pages(
                                        website_componentised_structure, components
                                    )

                                    website_code = get_website_pages_codes(
                                        website_componentised_structure,
                                        chat_conversation,
                                        website_name,
                                        website_description,
                                        assembled_pages_md,
                                        model,
                                    )

                                    logging.info("working here 12")
                                    ## parse markdown to get each page code seperatly, and then save to supabase

                                    page_codes = parse_markdown(website_code)
                                    logging.info("working here 13")
                                    ## save each page code to supabase
                                    all_pages = []
                                    for page_code2 in page_codes:
                                        page_name, page_code = page_code2
                                        all_pages.append(page_name)
                                        response = (
                                            supabase.table("pages")
                                            .insert(
                                                {
                                                    "user_id": user_id,
                                                    "website_id": website_id,
                                                    "title": page_name,
                                                    "content": page_code,
                                                }
                                            )
                                            .execute()
                                        )
                                        logging.info(
                                            f"{page_name} code saved successfully."
                                        )
                                    logging.info("working here 14")
                                    response = (
                                        supabase.table("websites")
                                        .update({"pages": all_pages})
                                        .eq("user_id", user_id)
                                        .eq("id", website_id)
                                        .execute()
                                    )
                                    logging.info("working here 15")
                                    ## update website status

                                    response = (
                                        supabase.table("websites")
                                        .update({"status": "completed"})
                                        .eq("user_id", user_id)
                                        .eq("id", website_id)
                                        .execute()
                                    )
                                    logging.info("working here 16")
                                    return func.HttpResponse(
                                        ## dont output the full code here, just a success message and a few lines of code
                                        f""" website code generated successfully. \n\nwebsite_code \n\n. This HTTP triggered function executed successfully. website code generated and saved successfully to supabase.""",
                                        status_code=200,
                                        headers={
                                            "Access-Control-Allow-Origin": "http://localhost:3000",
                                            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                                            "Access-Control-Allow-Headers": "Content-Type",
                                        },
                                    )
                                except Exception as e:
                                    logging.error(f"Error getting website code {e}")
                                    return func.HttpResponse(
                                        f"Componentised structure generated but error in getting website code: {e}",
                                    )

                        except Exception as e:
                            logging.error(
                                f"Error getting or saving website componentised structure: {e}"
                            )

                            return func.HttpResponse(
                                f"Error getting or saving website componentised structure: {e}",
                                status_code=500,
                            )
                    else:
                        return func.HttpResponse(
                            "GPT 4 call for website componentised structure error"
                        )

                except requests.RequestException as e:
                    logging.error(f"Error calling GPT-4 API 6 : {e}")
                    return func.HttpResponse(
                        f"Error calling GPT-4 API 7 : {e}", status_code=500
                    )
            else:
                return func.HttpResponse(
                    f"No data found for user_id: {user_id} and website_id: {website_id}."
                )
        except Exception as e:
            logging.error(f"Error fetching data from Supabase: {e}")
            return func.HttpResponse(
                f"Error fetching data from Supabase: {e}", status_code=500
            )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass user_id and website_id in the query string or in the request body for a personalized response.",
            status_code=200,
        )
