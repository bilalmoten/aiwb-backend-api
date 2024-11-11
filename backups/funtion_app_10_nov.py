import json
import os
import time
import azure.functions as func
import logging

from supabase import create_client, Client

# from dotenv import load_dotenv

import requests

#  url to check this function http://localhost:7071/api/code_website?user_id=a8d5d92f-b745-4b8c-b29e-d704ead7209b&website_id=51&model=claude-3-5-sonnet-20241022

# # Load environment variables from .env file
# load_dotenv()

# Initialize the Supabase client
supabase_url: str = os.environ.get("SUPABASE_URL")
supabase_key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

# Initialize Azure GPT-4 API settings
AZURE_KEY = os.environ.get("AZURE_KEY")
AZURE_KEY2 = os.environ.get("AZURE_KEY2")
GPT4o_ENDPOINT = os.environ.get("GPT4o_ENDPOINT")
GPT4o_MINI_ENDPOINT = os.environ.get("GPT4o_MINI_ENDPOINT")
O1_PREVIEW_ENDPOINT = os.environ.get("O1_PREVIEW_ENDPOINT")
O1_MINI_ENDPOINT = os.environ.get("O1_MINI_ENDPOINT")
GPT4o_MINI_AIWB_ENDPOINT = os.environ.get("GPT4o_MINI_AIWB_ENDPOINT")
CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY")


def call_claude_api(messages):
    endpoint = "https://api.anthropic.com/v1/messages"

    # Convert messages to Claude's format if needed
    claude_messages = messages
    claude_messages[0]["role"] = "user"

    payload = {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 8000,
        "messages": claude_messages,
    }

    headers = {
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }

    logging.info("Calling Claude API")
    logging.info(f"Payload: {payload}")

    claude_response = None
    try:
        claude_response = requests.post(endpoint, headers=headers, json=payload)
        claude_response.raise_for_status()
        print(claude_response.json())
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
        endpoint = O1_MINI_ENDPOINT
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
    logging.info(f"Payload: {payload}")
    gpt4_response = None
    try:
        gpt4_response = requests.post(endpoint, headers=headers, json=payload)
        gpt4_response.raise_for_status()
        return gpt4_response.json()
    except requests.RequestException as e:
        if gpt4_response:
            logging.error(gpt4_response.raw)
        logging.error(f"Error calling GPT-4 API: {e}")
        raise


def parse_markdown(markdown):
    sections = markdown.split("## ")[1:]  # Split the markdown into sections
    file_contents = []
    for section in sections:
        lines = section.split("\n")
        filename = lines[0].strip()  # The filename is the first line of the section
        print("filename is: ", filename)
        code_block = "\n".join(lines[1:])  # The rest of the section is the code block
        if "```html" in code_block:
            code_lines = code_block.split("```html")[1].split(
                "\n"
            )  # Extract the code lines
            file_content = "\n".join(
                code_lines[1:]
            ).strip()  # Join the code lines into a single string
            file_contents.append((filename, file_content))
    return file_contents


def get_website_pages_codes(
    website_structure,
    website_componentised_structure,
    chat_conversation,
    website_name,
    website_description,
    component_codes,
    model,
):
    system_prompt = """You are the lead Website developer at black wolf Designs. You excel at creating mesmerising websites that are based on the clients requirements.
    From your vast knowledge of HTML and Tailwind Css and how amazing website designs are made, please make a website for the user based on the following conversation between the user and an ai agent.
    the user requirements(the chat conversation between the client and an AI agent about the client's requirements) will be provided to you along with other website details.
    remember to include the following CDNs to ensure all icons and tailwind styling is applied correctly.
    
    As the Lead developer, you are responsible for giving the full, complete, properly functional code for the website that the user wants.
    Remember, the user's satisfaction is what matters the most. So give it your best and make sure to make any adjustments and edits needed to the code, to make sure the final code u deliver follows the best practices of the Industry.
    From consistant colour themes, to proper layouts, to proper text, and images, working links, consistant header and footer on all pages, everything needs to be the best. The goal is to create a website that the user falls in love with and is ready to publish right from the first draft.
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://kit.fontawesome.com/037776171a.js" crossorigin="anonymous"></script>
 
    Example Output:
    Do Not add any Placeholders, comments, backticks (```) or any other text in your response

    Only Respond with a Properly Formatted MARKDOWN with the HTML code for each HTML file(each page) of the website.


REMEMBER: Ensure that all pages have a consistent header and footer. The header should include navigation links to all pages of the website. The footer should be consistent across all pages as well.

Ensure all pages have a consistent header with navigation and a consistent footer.

    Write 
    
    ## All Files Completed 
    
    at the end of the markdown file, after all the HTML code for each page.

    the markdown should include each codeblock seperatly with language specified as HTML, and heading as name of the file, and a final heading of code completed.
    

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

    NOTHING ELSE. 
    
    """
    user_prompt = f"""Here is the details of the website the user wants to create: 
                         Website Name: {website_name} \n
                         Website Description: {website_description} \n
                         Chat Conversation: 
                         {chat_conversation}"""
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
            logging.info(f"response_json: {response_json}")
            if model == "claude-3-5-sonnet-20241022":
                response_text = response_json.get("content")[0].get("text")
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
        logging.info(f"page_code: {page_code}")
        return page_code
    except requests.RequestException as e:
        logging.error(f"Error calling GPT-4 API 3 for website Code: {e}")
        return "error calling GPT-4 API  4 for website code. \n Error: {e}"



app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


# @app.route(route="code_website")
# def code_website(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info("Python HTTP trigger function processed a request.")

# name = req.params.get("name")
# if not name:
#     try:
#         req_body = req.get_json()
#     except ValueError:
#         pass
#     else:
#         name = req_body.get("name")

# if name:
#     return func.HttpResponse(
#         f"Hello, {name}. This HTTP triggered function executed successfully."
#     )
# else:
#     return func.HttpResponse(
#         "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#         status_code=200,
#     )


@app.route(route="code_website")
def get_website_code(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    user_id = req.params.get("user_id")
    website_id = req.params.get("website_id")
    model = req.params.get("model")

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
            response = (
                supabase.table("websites")
                .select("website_name, website_description, chat_conversation")
                .eq("user_id", user_id)
                .eq("id", website_id)
                .execute()
            )
            data = response.data
            if data:
                website_data = data[0]
                website_name = website_data.get("website_name")
                website_description = website_data.get("website_description")
                chat_conversation = website_data.get("chat_conversation")

                website_code = get_website_pages_codes(
                    # website_structure,
                    # website_componentised_structure,
                    chat_conversation,
                    website_name,
                    website_description,
                    # component_codes,
                    model,
                )

                ## parse markdown to get each page code seperatly, and then save to supabase

                page_codes = parse_markdown(website_code)
                # pages_list = list(
                #     website_componentized_structure_dict.keys()
                # )

                ## save each page code to supabase
                                                all_pages = []
                                                for page_code2 in page_codes:
                                                    page_name, page_code = page_code2
                                                    all_pages.append(page_name)
                                                    # make a list of pages like [ "home",  "about_us",  "contact_us"]
                                                    # pages_list = list(
                                                    #     website_componentized_structure_dict.keys()
                                                    # )
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
                                                response = (
                                                    supabase.table("websites")
                                                    .update({"pages": all_pages})
                                                    .eq("user_id", user_id)
                                                    .eq("id", website_id)
                                                    .execute()
                                                )

                                                ## update website status

                                                response = (
                                                    supabase.table("websites")
                                                    .update({"status": "completed"})
                                                    .eq("user_id", user_id)
                                                    .eq("id", website_id)
                                                    .execute()
                                                )

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
                                                logging.error(
                                                    f"Error getting website code {e}"
                                                )
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

                            except Exception as e:
                                logging.error(
                                    f"Error getting componentized structure: {e}"
                                )
                                return func.HttpResponse(
                                    f"Error getting componentized structure: {e}",
                                    status_code=500,
                                )
                            # if not response:

                        except Exception as e:
                            logging.error(f"Error saving website structure: {e}")

                            return func.HttpResponse(
                                f"Error saving website structure: {e}", status_code=500
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
