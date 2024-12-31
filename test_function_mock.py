import json
import os
from datetime import datetime

# Load mock responses
with open("mock_responses_2.json", "r") as f:
    MOCK_RESPONSES = json.load(f)


def mock_fetch_conversation_data(user_id: str, website_id: str) -> dict:
    """Mock function to return website data"""
    return {
        "website_name": "Test Website",
        "website_description": "A test website",
        "chat_conversation": "Test conversation",
    }


def mock_create_website_plan(website_data: dict, model: str) -> str:
    """Mock function to return website plan"""
    return MOCK_RESPONSES["create_plan"]


def mock_create_design_blueprint(structured_plan: str, model: str) -> str:
    """Mock function to return design blueprint"""
    return MOCK_RESPONSES["create_blueprint"]


def mock_generate_website_code(design_blueprint: str, model: str) -> str:
    """Mock function to return website code"""
    return MOCK_RESPONSES["generate_code"]


def mock_generate_design_feedback(website_code: str, model: str) -> str:
    """Mock function to return design feedback"""
    return MOCK_RESPONSES["generate_feedback"]


def mock_refine_website_code(initial_code: str, feedback: str, model: str) -> str:
    """Mock function to return refined code"""
    return MOCK_RESPONSES["refine_code"]


def save_files_locally(website_code: str, output_dir: str = "test_output"):
    """Save generated files locally"""
    os.makedirs(output_dir, exist_ok=True)

    # Parse the markdown and save individual files
    sections = website_code.split("## ")[1:]  # Split the markdown into sections
    for section in sections:
        if section.strip() == "All Files Completed":
            continue

        lines = section.split("\n")
        filename = lines[0].strip()  # The filename is the first line of the section

        if "```html" in section:
            code_block = section.split("```html")[1].split("```")[0].strip()

            # Save to file
            file_path = os.path.join(output_dir, filename)
            with open(file_path, "w") as f:
                f.write(code_block)
            print(f"Saved {filename} to {file_path}")


def log_to_file(message, filename="test_log.txt"):
    """Log message to file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)


def test_with_mocks():
    """Run the website generation with mock responses"""
    log_filename = f"mock_test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    output_dir = f"test_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    try:
        log_to_file("Starting mock test", log_filename)

        # Step 1: Get website data
        website_data = mock_fetch_conversation_data("test_user", "test_website")
        log_to_file("\nMock Website Data:", log_filename)
        log_to_file(json.dumps(website_data, indent=2), log_filename)

        # Step 2: Create plan
        plan = mock_create_website_plan(website_data, "mock-model")
        log_to_file("\n✓ Mock Plan created:", log_filename)
        log_to_file(plan, log_filename)

        # Step 3: Create blueprint
        blueprint = mock_create_design_blueprint(plan, "mock-model")
        log_to_file("\n✓ Mock Blueprint created:", log_filename)
        log_to_file(blueprint, log_filename)

        # Step 4: Generate code
        code = mock_generate_website_code(blueprint, "mock-model")
        log_to_file("\n✓ Mock Code generated:", log_filename)
        log_to_file(code, log_filename)

        # Step 5: Generate feedback
        feedback = mock_generate_design_feedback(code, "mock-model")
        log_to_file("\n✓ Mock Feedback generated:", log_filename)
        log_to_file(feedback, log_filename)

        # Step 6: Refine code
        final_code = mock_refine_website_code(code, feedback, "mock-model")
        log_to_file("\n✓ Mock Code refined:", log_filename)
        log_to_file(final_code, log_filename)

        # Save files locally
        save_files_locally(final_code, output_dir)
        log_to_file(f"\n✓ Files saved locally in {output_dir}", log_filename)

    except Exception as e:
        error_msg = f"Error in mock test: {str(e)}"
        log_to_file(f"\n! {error_msg}", log_filename)


if __name__ == "__main__":
    test_with_mocks()
