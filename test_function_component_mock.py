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


def mock_fetch_available_components() -> dict:
    """Mock function to return available component categories and IDs"""
    return {
        "Blog Header": [
            {
                "id": "1",
                "component_id": "blog-header-1",
            },
            {
                "id": "2",
                "component_id": "blog-header-2",
            },
        ],
        "Navbar": [
            {
                "id": "3",
                "component_id": "navbar-1",
            }
        ],
    }


def mock_fetch_component_codes(component_ids: list) -> dict:
    """Mock function to return component codes for selected IDs"""
    mock_codes = {
        "blog-header-1": "<div>Mock Blog Header 1</div>",
        "blog-header-2": "<div>Mock Blog Header 2</div>",
        "navbar-1": "<nav>Mock Navbar 1</nav>",
    }
    return {
        comp_id: mock_codes[comp_id]
        for comp_id in component_ids
        if comp_id in mock_codes
    }


def mock_generate_component_structure(
    structured_plan: str, available_components: dict
) -> dict:
    """Mock function to return component structure"""
    return {
        "index": {"header": "Blog Header", "navigation": "Navbar"},
        "about": {"header": "Blog Header"},
    }


def mock_select_random_components(
    category_structure: dict, available_components: dict
) -> dict:
    """Mock function to select components and fetch their codes"""
    structure = {"index": ["blog-header-1", "navbar-1"], "about": ["blog-header-2"]}

    # Get all component IDs
    all_ids = []
    for page_components in structure.values():
        all_ids.extend(page_components)

    # Fetch codes
    codes = mock_fetch_component_codes(all_ids)

    return {"structure": json.dumps(structure), "codes": codes}


def mock_generate_design_feedback(website_code: str, model: str) -> str:
    """Mock function to return design feedback"""
    return MOCK_RESPONSES["generate_feedback"]


def mock_refine_website_code(initial_code: str, feedback: str, model: str) -> str:
    """Mock function to return refined code"""
    return MOCK_RESPONSES["refine_code"]


def save_files_locally(website_code: str, output_dir: str = "test_output"):
    """Save generated files locally"""
    os.makedirs(output_dir, exist_ok=True)

    sections = website_code.split("## ")[1:]
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
            print(f"Saved {filename} to {file_path}")


def log_to_file(message, filename="test_log.txt"):
    """Log message to file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)


def test_component_workflow():
    """Run the component-based website generation with mock responses"""
    log_filename = (
        f"mock_test_component_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )
    output_dir = f"test_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    try:
        log_to_file("Starting component-based mock test", log_filename)

        # Step 1: Get website data
        website_data = mock_fetch_conversation_data("test_user", "test_website")
        log_to_file("\nMock Website Data:", log_filename)
        log_to_file(json.dumps(website_data, indent=2), log_filename)

        # Step 2: Create plan
        plan = mock_create_website_plan(website_data, "mock-model")
        log_to_file("\n✓ Mock Plan created:", log_filename)
        log_to_file(plan, log_filename)

        # Step 3: Fetch component categories
        components = mock_fetch_available_components()
        log_to_file("\n✓ Mock Components categories fetched:", log_filename)
        log_to_file(json.dumps(components, indent=2), log_filename)

        # Step 4: Generate component structure
        structure = mock_generate_component_structure(plan, components)
        log_to_file("\n✓ Mock Component structure generated:", log_filename)
        log_to_file(json.dumps(structure, indent=2), log_filename)

        # Step 5: Select components and fetch their codes
        selected = mock_select_random_components(structure, components)
        log_to_file("\n✓ Mock Components selected and codes fetched:", log_filename)
        log_to_file(json.dumps(selected, indent=2), log_filename)

        # Step 6: Assemble template
        from function_app import pre_assemble_pages

        initial_code = pre_assemble_pages(selected["structure"], selected["codes"])
        log_to_file("\n✓ Template assembled:", log_filename)
        log_to_file(initial_code, log_filename)

        # Step 7: Generate feedback
        feedback = mock_generate_design_feedback(initial_code, "mock-model")
        log_to_file("\n✓ Mock Feedback generated:", log_filename)
        log_to_file(feedback, log_filename)

        # Step 8: Refine code
        final_code = mock_refine_website_code(initial_code, feedback, "mock-model")
        log_to_file("\n✓ Mock Code refined:", log_filename)
        log_to_file(final_code, log_filename)

        # Save files locally
        save_files_locally(final_code, output_dir)
        log_to_file(f"\n✓ Files saved locally in {output_dir}", log_filename)

    except Exception as e:
        error_msg = f"Error in mock test: {str(e)}"
        log_to_file(f"\n! {error_msg}", log_filename)


if __name__ == "__main__":
    test_component_workflow()
