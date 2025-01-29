import json
import os
from datetime import datetime
from supabase import create_client, Client
from function_app import (
    generate_request_id,
    execute_step,
    fetch_conversation_data,
    create_website_plan,
    fetch_available_categories,
    generate_component_structure,
    select_random_components,
    assemble_template,
    generate_website_code,
    generate_design_feedback,
    refine_website_code,
    supabase,  # Import the initialized client
    save_generated_pages,
    parse_markdown,
    delete_existing_pages,
)

# Test data
# TEST_USER_ID = "a8d5d92f-b745-4b8c-b29e-d704ead7209b"
TEST_USER_ID = "a8d5d92f-b745-4b8c-b29e-d704ead7209b"
TEST_WEBSITE_ID = "380"
# version = "2"
MODEL = f"o1-mini"
DIRECTORY_NAME = "website_380"


def log_to_file(message: str, filename: str):
    """Log message with timestamp to file and console"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"

    with open(filename, "a") as f:
        f.write(log_message + "\n")
    print(message)


def log_step_details(step_name: str, inputs: dict, output: any, log_file: str):
    """Log detailed information about a step's inputs and outputs"""
    log_to_file(f"\n=== {step_name} Details ===", log_file)
    log_to_file("Inputs:", log_file)
    for key, value in inputs.items():
        log_to_file(f"  {key}: {json.dumps(value, indent=2)}", log_file)
    log_to_file("\nOutput:", log_file)
    log_to_file(f"  {json.dumps(output, indent=2)}", log_file)
    log_to_file("=" * 50 + "\n", log_file)


def test_supabase_connection():
    """Test Supabase connection and credentials"""
    try:
        # First test basic connection
        response = supabase.table("websites").select("count").limit(1).execute()
        print("✓ Basic connection successful")

        # Now test the actual query we'll use
        test_query = (
            supabase.table("websites")
            .select("website_name, website_description, chat_conversation")
            .eq("user_id", TEST_USER_ID)
            .eq("id", TEST_WEBSITE_ID)
            .execute()
        )
        print(f"Query response: {test_query}")
        print(f"Data: {test_query.data}")

        if not test_query.data:
            print(
                f"✗ No data found for user_id: {TEST_USER_ID}, website_id: {TEST_WEBSITE_ID}"
            )
            return False

        return True
    except Exception as e:
        print(f"✗ Supabase query failed: {str(e)}")
        return False


def test_website_generation():
    # # Test Supabase connection first
    # if not test_supabase_connection():
    #     print("Aborting test due to Supabase connection failure")
    #     return

    # Create test directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_dir = DIRECTORY_NAME
    os.makedirs(test_dir, exist_ok=True)

    # Initialize logging and response files
    log_file = os.path.join(test_dir, "test_log.txt")
    responses_file = os.path.join(test_dir, "responses.json")
    responses = {}

    # Initialize request tracking
    request_id = generate_request_id(TEST_USER_ID, TEST_WEBSITE_ID)
    log_to_file(f"Starting test with request ID: {request_id}", log_file)
    log_to_file("-" * 50, log_file)

    try:
        # Step 0: Delete existing pages
        current_step = "delete_pages"
        log_to_file("\nStep 0: Deleting existing pages...", log_file)
        try:
            inputs = {"user_id": TEST_USER_ID, "website_id": TEST_WEBSITE_ID}
            execute_step(
                "delete_pages",
                request_id,
                delete_existing_pages,
                user_id=TEST_USER_ID,
                website_id=TEST_WEBSITE_ID,
            )
            log_step_details(current_step, inputs, "Existing pages deleted", log_file)
            log_to_file("✓ Existing pages deleted", log_file)
        except Exception as e:
            error_details = {
                "step": current_step,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "inputs": inputs,
            }
            log_to_file(
                f"! Error deleting pages: {json.dumps(error_details, indent=2)}",
                log_file,
            )
            raise Exception(json.dumps(error_details))
        log_to_file("-" * 50, log_file)

        # Step 1: Fetch conversation data
        current_step = "fetch_data"
        log_to_file("\nStep 1: Fetching website data...", log_file)
        try:
            inputs = {"user_id": TEST_USER_ID, "website_id": TEST_WEBSITE_ID}
            website_data = execute_step(
                "fetch_data",
                request_id,
                fetch_conversation_data,
                # test_mode=True,  # Use mock data
                user_id=TEST_USER_ID,
                website_id=TEST_WEBSITE_ID,
            )
            log_step_details(current_step, inputs, website_data, log_file)
            responses["website_data"] = website_data
            # log_to_file("✓ Website data fetched (mock)", log_file)
        except Exception as e:
            error_details = {
                "step": current_step,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "inputs": inputs,
            }
            log_to_file(
                f"! Error details: {json.dumps(error_details, indent=2)}", log_file
            )
            raise Exception(json.dumps(error_details))
        log_to_file("-" * 50, log_file)

        # Step 2: Create plan
        current_step = "create_plan"
        log_to_file("\nStep 2: Creating website plan...", log_file)
        inputs = {"website_data": website_data, "model": MODEL}
        structured_plan = execute_step(
            "create_plan",
            request_id,
            create_website_plan,
            # test_mode=True,  # Use mock data
            website_data=website_data,
            model=MODEL,
        )
        log_step_details(current_step, inputs, structured_plan, log_file)
        responses["structured_plan"] = structured_plan
        # log_to_file("✓ Plan created (mock)", log_file)

        # Step 3: Fetch categories
        current_step = "fetch_categories"
        log_to_file("\nStep 3: Fetching component categories...", log_file)
        try:
            inputs = {}  # No inputs for this step
            available_categories = execute_step(
                "fetch_categories",
                request_id,
                fetch_available_categories,
                # test_mode=True,  # Use mock data
            )
            log_step_details(current_step, inputs, available_categories, log_file)
            responses["available_categories"] = available_categories
            # log_to_file("✓ Categories fetched (mock)", log_file)
        except Exception as e:
            error_details = {
                "step": current_step,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "inputs": inputs,
            }
            log_to_file(
                f"! Error details: {json.dumps(error_details, indent=2)}", log_file
            )
            raise Exception(json.dumps(error_details))

        # Step 4: Generate structure
        current_step = "generate_structure"
        log_to_file("\nStep 4: Generating component structure...", log_file)
        inputs = {
            "structured_plan": structured_plan,
            "available_categories": available_categories,
            "model": MODEL,
        }
        component_structure = execute_step(
            "generate_structure",
            request_id,
            generate_component_structure,
            structured_plan=structured_plan,
            available_categories=available_categories,
            model=MODEL,
        )
        log_step_details(current_step, inputs, component_structure, log_file)
        responses["component_structure"] = component_structure
        log_to_file("✓ Structure generated", log_file)

        # Step 5: Select components
        current_step = "select_components"
        log_to_file("\nStep 5: Selecting components...", log_file)
        try:
            inputs = {
                "category_structure": component_structure,
                "available_categories": available_categories,
            }
            selected_components = execute_step(
                "select_components",
                request_id,
                select_random_components,
                category_structure=component_structure,
                available_categories=available_categories,
            )
            log_step_details(current_step, inputs, selected_components, log_file)
            responses["selected_components"] = selected_components
            log_to_file("✓ Components selected", log_file)
        except Exception as e:
            error_details = {
                "step": current_step,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "inputs": inputs,
            }
            log_to_file(
                f"! Error details: {json.dumps(error_details, indent=2)}", log_file
            )
            raise Exception(json.dumps(error_details))

        # Step 6: Assemble template
        current_step = "assemble_template"
        log_to_file("\nStep 6: Assembling template...", log_file)
        inputs = {"components_data": selected_components}
        initial_code = execute_step(
            "assemble_template",
            request_id,
            assemble_template,
            components_data=selected_components,
        )
        log_step_details(current_step, inputs, initial_code, log_file)
        responses["initial_code"] = initial_code
        log_to_file("✓ Template assembled", log_file)

        # Step 7: Generate initial website code
        current_step = "generate_code"
        log_to_file("\nStep 7: Generating initial website code...", log_file)
        inputs = {
            "website_plan": structured_plan,
            "website_assembled_template": initial_code,
            "model": MODEL,
        }
        website_code = execute_step(
            "generate_code",
            request_id,
            generate_website_code,
            website_plan=structured_plan,
            website_assembled_template=initial_code,
            model=MODEL,
        )
        log_step_details(current_step, inputs, website_code, log_file)
        responses["website_code"] = website_code
        log_to_file("✓ Initial code generated", log_file)

        # # Step 8: Generate feedback
        # current_step = "generate_feedback"
        # log_to_file("\nStep 8: Generating feedback...", log_file)
        # inputs = {"website_code": website_code, "model": MODEL}
        # feedback = execute_step(
        #     "generate_feedback",
        #     request_id,
        #     generate_design_feedback,
        #     website_code=website_code,
        #     model=MODEL,
        # )
        # log_step_details(current_step, inputs, feedback, log_file)
        # responses["feedback"] = feedback
        # log_to_file("✓ Feedback generated", log_file)

        # # Step 9: Refine code
        # current_step = "refine_code"
        # log_to_file("\nStep 9: Refining code...", log_file)
        # inputs = {"initial_code": initial_code, "feedback": feedback, "model": MODEL}
        # final_code = execute_step(
        #     "refine_code",
        #     request_id,
        #     refine_website_code,
        #     initial_code=initial_code,
        #     feedback=feedback,
        #     model=MODEL,
        # )
        # log_step_details(current_step, inputs, final_code, log_file)
        # responses["final_code"] = final_code
        # log_to_file("✓ Code refined", log_file)

        # Save all responses
        with open(responses_file, "w") as f:
            json.dump(responses, f, indent=2)
        log_to_file(f"\n✓ All responses saved to {responses_file}", log_file)

        # Save pages to Supabase
        current_step = "save_pages"
        log_to_file("\nSaving pages to Supabase...", log_file)
        try:
            inputs = {
                "user_id": TEST_USER_ID,
                "website_id": TEST_WEBSITE_ID,
                "website_code": website_code,
            }
            execute_step(
                "save_pages",
                request_id,
                save_generated_pages,
                user_id=TEST_USER_ID,
                website_id=TEST_WEBSITE_ID,
                website_code=website_code,
                # website_code=final_code,
            )
            log_step_details(current_step, inputs, "Pages saved successfully", log_file)
            log_to_file("✓ Pages saved to Supabase", log_file)
        except Exception as e:
            error_details = {
                "step": current_step,
                "error_type": type(e).__name__,
                "error_message": str(e),
                "inputs": inputs,
            }
            log_to_file(
                f"! Error saving pages: {json.dumps(error_details, indent=2)}", log_file
            )
            raise Exception(json.dumps(error_details))

        # Save pages locally
        pages_dir = os.path.join(test_dir, "pages")
        os.makedirs(pages_dir, exist_ok=True)

        try:
            # Parse the markdown into separate pages
            page_codes = parse_markdown(website_code)

            # Save each page
            for page_name, page_content in page_codes:
                file_path = os.path.join(pages_dir, page_name)
                with open(file_path, "w") as f:
                    f.write(page_content)
                log_to_file(f"✓ Saved {page_name} locally", log_file)

            log_to_file(f"✓ All pages saved locally in {pages_dir}", log_file)
        except Exception as e:
            log_to_file(f"! Error saving pages locally: {str(e)}", log_file)

        log_to_file("\n✓ Test completed successfully!", log_file)

    except Exception as e:
        try:
            error_details = json.loads(str(e))
            error_msg = f"""
ERROR in step: {error_details.get('step')}
Error type: {error_details.get('error_type')}
Error message: {error_details.get('error_message')}
Attempt: {error_details.get('attempt')}
User ID: {error_details.get('user_id')}
Website ID: {error_details.get('website_id')}
"""
        except json.JSONDecodeError:
            error_msg = f"""
ERROR in step: {current_step}
Error type: {type(e).__name__}
Error message: {str(e)}
"""

        log_to_file("\n" + "!" * 50, log_file)
        log_to_file(error_msg, log_file)
        log_to_file("!" * 50, log_file)

        # Save partial responses if error occurs
        if responses:
            partial_file = os.path.join(test_dir, "partial_responses.json")
            try:
                responses["error"] = json.loads(str(e))
            except json.JSONDecodeError:
                responses["error"] = {
                    "step": current_step,
                    "type": type(e).__name__,
                    "message": str(e),
                }


if __name__ == "__main__":
    test_website_generation()
