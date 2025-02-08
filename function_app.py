import json
import logging
import azure.functions as func
import base_functions_for_function_app as base_functions

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="code_website")
def get_website_code(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Extract and validate parameters
        params = base_functions.extract_request_params(req)
        user_id = params["user_id"]
        website_id = params["website_id"]
        model = params["model"]

        if not user_id or not website_id:
            return func.HttpResponse(
                json.dumps(
                    {
                        "success": False,
                        "error": "Missing required parameters: user_id and website_id",
                    }
                ),
                status_code=400,
            )

        # Initialize request tracking
        request_id = base_functions.generate_request_id(user_id, website_id)
        logging.info(f"Starting website generation - Request ID: {request_id}")

        # Update website status to 'processing'
        base_functions.supabase.table("websites").update({"status": "processing"}).eq(
            "id", website_id
        ).execute()

        try:
            # Step 0: Delete existing pages
            base_functions.execute_step(
                "delete_pages",
                request_id,
                base_functions.delete_existing_pages,
                user_id=user_id,
                website_id=website_id,
            )

            # Step 1: Fetch conversation data
            website_data = base_functions.execute_step(
                "fetch_data",
                request_id,
                base_functions.fetch_conversation_data,
                user_id=user_id,
                website_id=website_id,
            )

            # Step 2: Create structured plan
            structured_plan = base_functions.execute_step(
                "create_plan",
                request_id,
                base_functions.create_website_plan,
                website_data=website_data,
                website_id=website_id,
                model=model,
            )

            # Step 3: Generate initial website code
            website_code = base_functions.execute_step(
                "generate_code",
                request_id,
                base_functions.generate_website_code,
                user_conversation=website_data,
                website_plan=structured_plan,
                model=model,
                website_id=website_id,
            )

            # Step 4: Save generated pages
            base_functions.execute_step(
                "save_pages",
                request_id,
                base_functions.save_generated_pages,
                user_id=user_id,
                website_id=website_id,
                website_code=website_code,
            )

            return func.HttpResponse(
                json.dumps(
                    {
                        "success": True,
                        "request_id": request_id,
                        "message": "Website generated successfully",
                    }
                )
            )

        except Exception as e:
            # Rollback: Update website status to 'failed' and delete any generated pages
            base_functions.supabase.table("websites").update({"status": "failed"}).eq(
                "id", website_id
            ).execute()
            base_functions.delete_existing_pages(user_id, website_id)
            raise e

    except Exception as e:
        error_msg = str(e)
        logging.error(f"Error in website generation: {error_msg}")

        return func.HttpResponse(
            json.dumps({"success": False, "error": error_msg}), status_code=500
        )
