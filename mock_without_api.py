from typing import Dict, Any
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[logging.FileHandler("mock_inputs.log"), logging.StreamHandler()],
)

# Load mock responses
try:
    with open("mock_responses_2.json", "r") as f:
        MOCK_RESPONSES = json.load(f)
except FileNotFoundError:
    MOCK_RESPONSES = {}


def log_ai_call(step: str, inputs: Dict[str, Any]) -> None:
    """Log the inputs that would go to the AI call"""
    logging.info(f"\nAI Call for: {step}")
    logging.info("Inputs:")
    logging.info(json.dumps(inputs, indent=2))


def mock_create_website_plan(website_data: dict, model: str = "gpt-4") -> str:
    """Mock function to capture website plan generation inputs"""
    inputs = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are an expert web designer and strategist...",
            },
            {
                "role": "user",
                "content": f"""
                Website Name: {website_data['website_name']}
                Description: {website_data['website_description']}
                User Conversation: {website_data['chat_conversation']}
                """,
            },
        ],
    }
    log_ai_call("Website Plan", inputs)
    return MOCK_RESPONSES.get("create_plan", "Mock website plan response")


def mock_create_design_blueprint(structured_plan: str, model: str = "gpt-4") -> str:
    """Mock function to capture design blueprint generation inputs"""
    inputs = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an expert web designer..."},
            {"role": "user", "content": f"Previous Plan: {structured_plan}"},
        ],
    }
    log_ai_call("Design Blueprint", inputs)
    return MOCK_RESPONSES.get("design_blueprint", "Mock design blueprint response")


def mock_generate_website_code(design_blueprint: str, model: str = "gpt-4") -> str:
    """Mock function to capture website code generation inputs"""
    inputs = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an expert web developer..."},
            {"role": "user", "content": f"Design Blueprint: {design_blueprint}"},
        ],
    }
    log_ai_call("Website Code", inputs)
    return MOCK_RESPONSES.get("website_code", "Mock website code response")


def mock_generate_design_feedback(website_code: str, model: str = "gpt-4") -> str:
    """Mock function to capture design feedback generation inputs"""
    inputs = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an expert web design reviewer..."},
            {"role": "user", "content": f"Website Code: {website_code}"},
        ],
    }
    log_ai_call("Design Feedback", inputs)
    return MOCK_RESPONSES.get("design_feedback", "Mock design feedback response")


def mock_refine_website_code(
    initial_code: str, feedback: str, model: str = "gpt-4"
) -> str:
    """Mock function to capture code refinement inputs"""
    inputs = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an expert web developer..."},
            {
                "role": "user",
                "content": f"""
                Initial Code: {initial_code}
                Feedback: {feedback}
                """,
            },
        ],
    }
    log_ai_call("Code Refinement", inputs)
    return MOCK_RESPONSES.get("refined_code", "Mock refined code response")


def mock_generate_website(website_data: dict) -> dict:
    """Main function to run the entire website generation process with mocks"""
    try:
        # Step 1: Create website plan
        plan = mock_create_website_plan(website_data)

        # Step 2: Create design blueprint
        blueprint = mock_create_design_blueprint(plan)

        # Step 3: Generate initial website code
        initial_code = mock_generate_website_code(blueprint)

        # Step 4: Get design feedback
        feedback = mock_generate_design_feedback(initial_code)

        # Step 5: Refine website code
        final_code = mock_refine_website_code(initial_code, feedback)

        return {
            "plan": plan,
            "blueprint": blueprint,
            "initial_code": initial_code,
            "feedback": feedback,
            "final_code": final_code,
        }

    except Exception as e:
        logging.error(f"Error in mock generation: {str(e)}")
        raise


# Example usage
if __name__ == "__main__":
    test_data = {
        "website_name": "Cosmetica",
        "website_description": "A 100% organic, cruelty-free skincare brand",
        "chat_conversation": "[conversation history here]",
    }

    results = mock_generate_website(test_data)
    logging.info("\nGeneration Complete!")
