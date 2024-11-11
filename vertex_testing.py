from dotenv import load_dotenv

load_dotenv()  # Add this at the top of your file

import json
import os
import logging
from google.auth import default
from google.auth.transport.requests import Request
import json
import base64
import os


import requests

#  url to check this function http://localhost:7071/api/code_website?user_id=a8d5d92f-b745-4b8c-b29e-d704ead7209b&website_id=51&model=claude-3-5-sonnet-20241022


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

        endpoint = f"https://{location_id}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{location_id}/publishers/google/models/{model_id}:streamGenerateContent"

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": messages[0]["content"]}],
                }
            ],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 2000,
            },
        }

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        logging.info(f"Calling Google AI API: {endpoint}")
        logging.info(f"Payload: {payload}")

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()

            data = response.json()
            # Direct Gemini response parsing - taking the last response chunk
            last_chunk = data[-1]  # Get the last item in the response list
            content = last_chunk["candidates"][0]["content"]["parts"][0]["text"]

            return {"choices": [{"message": {"content": content}}]}

        except requests.RequestException as e:
            if response:
                logging.error(response.text)
            logging.error(f"Error calling Google AI API: {e}")
            raise

    except Exception as e:
        logging.error(f"Error in Google AI API call: {e}")
        raise


# Test code
if __name__ == "__main__":
    test_messages = [{"role": "user", "content": "Hi"}]

    try:
        response = call_google_ai_api(test_messages)
        print("=== Gemini Model Response ===")
        print(response["choices"][0]["message"]["content"])

    except Exception as e:
        print(f"Error during testing: {e}")
