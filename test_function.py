import json
import os
from datetime import datetime
from function_app import (
    create_website_plan,
    create_design_blueprint,
    generate_website_code,
    generate_design_feedback,
    refine_website_code,
    fetch_conversation_data,
)

# Test data - replace with your test website ID
TEST_USER_ID = "a8d5d92f-b745-4b8c-b29e-d704ead7209b"
TEST_WEBSITE_ID = "29"
MODEL = "o1-mini"


def log_to_file(message, filename="test_log.txt"):
    """Log message to file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)


def capture_responses():
    """Run the website generation once and capture all responses"""
    responses = {}
    log_filename = f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    try:
        log_to_file(
            f"Starting test with USER_ID: {TEST_USER_ID}, WEBSITE_ID: {TEST_WEBSITE_ID}",
            log_filename,
        )

        # Fetch real website data
        website_data = fetch_conversation_data(TEST_USER_ID, TEST_WEBSITE_ID)
        log_to_file("\nWebsite Data:", log_filename)
        log_to_file(json.dumps(website_data, indent=2), log_filename)

        # Capture each step's response
        responses["create_plan"] = create_website_plan(website_data, MODEL)
        log_to_file("\n✓ Plan created:", log_filename)
        log_to_file(responses["create_plan"], log_filename)

        responses["create_blueprint"] = create_design_blueprint(
            responses["create_plan"], MODEL
        )
        log_to_file("\n✓ Blueprint created:", log_filename)
        log_to_file(responses["create_blueprint"], log_filename)

        responses["generate_code"] = generate_website_code(
            responses["create_blueprint"], MODEL
        )
        log_to_file("\n✓ Initial code generated:", log_filename)
        log_to_file(responses["generate_code"], log_filename)

        responses["generate_feedback"] = generate_design_feedback(
            responses["generate_code"], MODEL
        )
        log_to_file("\n✓ Feedback generated:", log_filename)
        log_to_file(responses["generate_feedback"], log_filename)

        responses["refine_code"] = refine_website_code(
            responses["generate_code"], responses["generate_feedback"], MODEL
        )
        log_to_file("\n✓ Code refined:", log_filename)
        log_to_file(responses["refine_code"], log_filename)

        # Save responses to file
        responses_filename = (
            f"mock_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        with open(responses_filename, "w") as f:
            json.dump(responses, f, indent=2)

        log_to_file(
            f"\n✓ All responses captured and saved to {responses_filename}",
            log_filename,
        )

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        log_to_file(f"\n! {error_msg}", log_filename)

        # If we have partial responses, save them
        if responses:
            partial_filename = (
                f"partial_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
            with open(partial_filename, "w") as f:
                json.dump(responses, f, indent=2)
            log_to_file(
                f"\n! Partial responses saved to {partial_filename}", log_filename
            )


if __name__ == "__main__":
    capture_responses()
