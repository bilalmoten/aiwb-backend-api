import os
import base64
import json
from vertex_testing import call_google_ai_api


def test_vertex_ai():
    # Make sure you have your Google credentials set up
    # This is just an example structure of credentials - you need to replace with your actual encoded credentials
    credentials = {
        "type": "service_account",
        "project_id": "eng-venture-439304-b2",
        # ... other credential fields ...
    }

    # Encode credentials and set environment variable
    encoded_credentials = base64.b64encode(json.dumps(credentials).encode()).decode()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"] = encoded_credentials
    os.environ["GOOGLE_CLOUD_PROJECT_ID"] = "eng-venture-439304-b2"

    # Prepare the messages
    messages = [{"role": "user", "content": "Hi"}]

    try:
        # Test with Gemini model (default)
        response = call_google_ai_api(messages)
        print("Gemini Response:")
        print(response["choices"][0]["message"]["content"])

        # Test with Claude model
        response = call_google_ai_api(messages, model="claude-3-sonnet")
        print("\nClaude Response:")
        print(response["choices"][0]["message"]["content"])

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_vertex_ai()
