import json
import os
from datetime import datetime
from function_app import (
    create_website_plan,
    fetch_available_components,
    generate_component_structure,
    select_random_components,
    pre_assemble_pages,
    generate_design_feedback,
    refine_website_code,
    fetch_conversation_data,
)

# Test data - replace with your test website ID
TEST_USER_ID = "a8d5d92f-b745-4b8c-b29e-d704ead7209b"
TEST_WEBSITE_ID = "29"
MODEL = "o1-mini"


def log_to_file(message, filename="test_log4.txt"):
    """Log message to file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)


def capture_component_responses():
    """Run the component-based website generation once and capture all responses"""
    responses = {}
    current_step = "initialization"
    log_filename = f"test_component_log4.txt"

    try:
        log_to_file("Starting component-based website generation test", log_filename)
        log_to_file("-" * 50, log_filename)

        # Step 1: Fetch website data
        current_step = "fetch_website_data"
        log_to_file(
            f"\nStep 1: Fetching website data for ID: {TEST_WEBSITE_ID}", log_filename
        )
        website_data = fetch_conversation_data(TEST_USER_ID, TEST_WEBSITE_ID)
        responses["website_data"] = website_data
        log_to_file("✓ Success: Website data fetched", log_filename)
        log_to_file("Data:", log_filename)
        log_to_file(json.dumps(website_data, indent=2), log_filename)
        log_to_file("-" * 50, log_filename)

        # Step 2: Create plan
        current_step = "create_plan"
        log_to_file("\nStep 2: Creating website plan", log_filename)
        responses["create_plan"] = create_website_plan(website_data, MODEL)
        log_to_file("✓ Success: Plan created", log_filename)
        log_to_file("Plan:", log_filename)
        log_to_file(responses["create_plan"], log_filename)
        log_to_file("-" * 50, log_filename)

        # Step 3: Fetch component categories
        current_step = "fetch_components"
        log_to_file("\nStep 3: Fetching component categories", log_filename)
        responses["available_components"] = fetch_available_components()
        log_to_file("✓ Success: Component categories fetched", log_filename)
        log_to_file("Categories:", log_filename)
        log_to_file(
            json.dumps(responses["available_components"], indent=2), log_filename
        )
        log_to_file("-" * 50, log_filename)

        # Step 4: Generate component structure
        current_step = "generate_structure"
        log_to_file("\nStep 4: Generating component structure", log_filename)
        responses["component_structure"] = generate_component_structure(
            responses["create_plan"], responses["available_components"]
        )
        log_to_file("✓ Success: Component structure generated", log_filename)
        log_to_file("Structure:", log_filename)
        log_to_file(
            json.dumps(responses["component_structure"], indent=2), log_filename
        )
        log_to_file("-" * 50, log_filename)

        # Step 5: Select components and fetch codes
        current_step = "select_components"
        log_to_file("\nStep 5: Selecting components and fetching codes", log_filename)
        responses["selected_components"] = select_random_components(
            responses["component_structure"], responses["available_components"]
        )
        log_to_file("✓ Success: Components selected and codes fetched", log_filename)
        log_to_file("Selected components:", log_filename)
        log_to_file(
            json.dumps(responses["selected_components"], indent=2), log_filename
        )
        log_to_file("-" * 50, log_filename)

        # Step 6: Assemble template
        current_step = "assemble_template"
        log_to_file("\nStep 6: Assembling website template", log_filename)
        responses["initial_code"] = pre_assemble_pages(
            responses["selected_components"]["structure"],
            responses["selected_components"]["codes"],
        )
        log_to_file("✓ Success: Template assembled", log_filename)
        log_to_file("-" * 50, log_filename)

        # Step 7: Generate feedback
        current_step = "generate_feedback"
        log_to_file("\nStep 7: Generating design feedback", log_filename)
        responses["generate_feedback"] = generate_design_feedback(
            responses["initial_code"], MODEL
        )
        log_to_file("✓ Success: Feedback generated", log_filename)
        log_to_file("Feedback:", log_filename)
        log_to_file(responses["generate_feedback"], log_filename)
        log_to_file("-" * 50, log_filename)

        # Step 8: Refine code
        current_step = "refine_code"
        log_to_file("\nStep 8: Refining website code", log_filename)
        responses["refine_code"] = refine_website_code(
            responses["initial_code"], responses["generate_feedback"], MODEL
        )
        log_to_file("✓ Success: Code refined", log_filename)
        log_to_file("-" * 50, log_filename)

        # Save responses
        current_step = "save_responses"
        responses_filename = f"component_responses4.json"
        with open(responses_filename, "w") as f:
            json.dump(responses, f, indent=2)
        log_to_file(f"\n✓ All responses saved to {responses_filename}", log_filename)

        # Save generated files
        current_step = "save_files"
        output_dir = f"test_output4"
        os.makedirs(output_dir, exist_ok=True)
        log_to_file(f"\nSaving generated files to {output_dir}", log_filename)

        sections = responses["refine_code"].split("## ")[1:]
        for section in sections:
            if section.strip() == "All Files Completed":
                continue

            lines = section.split("\n")
            filename = lines[0].strip()

            if "```html" in section:
                code_block = section.split("```html")[1].split("```")[0].strip()
                file_path = os.path.join(output_dir, filename)
                with open(file_path, "w") as f:
                    f.write(code_block)
                log_to_file(f"✓ Saved {filename}", log_filename)

        log_to_file("\n✓ Test completed successfully!", log_filename)

    except Exception as e:
        error_msg = f"""
ERROR in step: {current_step}
Error type: {type(e).__name__}
Error message: {str(e)}
"""
        log_to_file("\n" + "!" * 50, log_filename)
        log_to_file(error_msg, log_filename)
        log_to_file("!" * 50, log_filename)

        # Save partial responses with error details
        if responses:
            partial_filename = f"partial_component_responses4.json"
            responses["error"] = {
                "step": current_step,
                "type": type(e).__name__,
                "message": str(e),
            }
            with open(partial_filename, "w") as f:
                json.dump(responses, f, indent=2)
            log_to_file(
                f"\nPartial responses and error details saved to: {partial_filename}",
                log_filename,
            )


if __name__ == "__main__":
    capture_component_responses()
