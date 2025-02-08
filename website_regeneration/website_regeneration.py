import asyncio
import aiohttp
import json
import os
import logging
from datetime import datetime
from typing import List, Dict
import base64
from playwright.async_api import async_playwright
from supabase import create_client
from azure.communication.email import EmailClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=f"website_regeneration/logs/website_regeneration_1.log",
)

# Configuration
AZURE_FUNCTION_URL = "https://api2.azurewebsites.net/api/code_website"
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
AZURE_EMAIL_CONNECTION_STRING = os.getenv("AZURE_EMAIL_CONNECTION_STRING")
SENDER_EMAIL = "DoNotReply@aiwebsitebuilder.tech"
REPLY_TO_EMAIL = "mbilal@aiwebsitebuilder.tech"

# Initialize clients
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
email_client = EmailClient.from_connection_string(AZURE_EMAIL_CONNECTION_STRING)


async def take_website_screenshot(website_id: str, subdomain: str) -> str:
    """Take a screenshot of the website preview"""
    preview_url = f"https://{subdomain}.aiwebsitebuilder.tech"
    screenshot_path = f"website_regeneration/screenshots/{website_id}.png"

    # Ensure screenshots directory exists
    os.makedirs("website_regeneration/screenshots", exist_ok=True)

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.set_viewport_size({"width": 1920, "height": 1080})
            await page.goto(preview_url, wait_until="networkidle")
            # Wait for any animations to complete
            await page.wait_for_timeout(2000)
            await page.screenshot(path=screenshot_path, full_page=True)
            await browser.close()
            return screenshot_path
    except Exception as e:
        logging.error(f"Screenshot error for {website_id}: {str(e)}")
        raise

    # return screenshot_path


def create_email_content(
    user_name: str,
    website_name: str,
    # screenshot_path: str,
    subdomain: str,
    website_id: str,
) -> Dict:
    """Create HTML email content with embedded screenshot"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 600px;
                margin: 0 auto;
            }}
            .header {{
                background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%);
                color: white;
                padding: 20px;
                text-align: center;
                border-radius: 10px 10px 0 0;
            }}
            .content {{
                padding: 20px;
                background: #fff;
                border: 1px solid #ddd;
            }}
            .screenshot {{
                width: 100%;
                max-width: 600px;
                margin: 20px 0;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .button {{
                display: inline-block;
                padding: 10px 20px;
                background: #6366F1;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                margin: 10px 5px;
            }}
            .button-container {{
                text-align: center;
                margin: 20px 0;
            }}
            .footer {{
                text-align: center;
                padding: 20px;
                color: #666;
                font-size: 0.9em;
            }}
            .contact-info {{
                background: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
            }}
            .new-features {{
                background: #f0f4ff;
                padding: 15px;
                border-radius: 5px;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Your Website Has Been Regenerated! 🎉</h1>
        </div>
        <div class="content">
            <p>Hello {user_name},</p>
            
            <p>I hope this email finds you well. First and foremost, I want to personally apologize for any inconvenience you experienced when initially creating your website <strong>"{website_name}"</strong>. As the founder of AI Website Builder, ensuring a smooth experience for our users is my top priority.</p>

            <p>Over the past few weeks, our team has been working tirelessly to enhance our system's stability and features. I'm pleased to inform you that we've successfully regenerated your website with our improved system.</p>
            
            <p>Here's a preview of your newly generated website (see attached screenshot):</p>
            
            <div class="new-features">
                <h3>🚀 Exciting New Features & Updates:</h3>
                <ul>
                    <li>✨ Form Response Management - Receive and manage form submissions directly</li>
                    <li>🌐 Custom Domain Connection (Pro Feature)</li>
                    <li>🛠️ Enhanced Website Editor</li>
                    <li>📱 Improved Mobile Responsiveness</li>
                    <li>🔜 Coming Soon:
                        <ul>
                            <li>Blog functionality</li>
                            <li>Newsletter integration</li>
                            <li>E-commerce capabilities</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <p>Your website is now live and ready for your review. Here are your important links:</p>
            
            <div class="button-container">
                <a href="https://{subdomain}.aiwebsitebuilder.tech" class="button">View Live Website</a>
                <a href="https://aiwebsitebuilder.tech/dashboard/editor/{website_id}" class="button">Edit Website</a>
                <a href="https://aiwebsitebuilder.tech/dashboard" class="button">Dashboard</a>
            </div>

            <div class="contact-info">
                <h3>Need Help? Contact Us Directly:</h3>
                <p>I'm personally committed to ensuring your success with AI Website Builder. Feel free to reach out:</p>
                <ul>
                    <li>📧 Email: <a href="mailto:mbilal@aiwebsitebuilder.tech">mbilal@aiwebsitebuilder.tech</a></li>
                    <li>📱 WhatsApp: <a href="https://wa.me/923351379362">+92 335 137 9362</a></li>
                </ul>
            </div>
            
            <p>Thank you for your patience and trust in AI Website Builder. We're excited to see how you'll use these new features to enhance your online presence.</p>
            
            <p>Best regards,<br>Muhammad Bilal<br>Founder, AI Website Builder</p>
        </div>
        <div class="footer">
            <p>© 2024 AI Website Builder. All rights reserved.</p>
            <p><small>This is an automated message from DoNotReply@aiwebsitebuilder.tech. Please reply to mbilal@aiwebsitebuilder.tech</small></p>
        </div>
    </body>
    </html>
    """

    return {
        "subject": f"Your Website '{website_name}' Has Been Regenerated! 🎉",
        "html": html_content,
    }


async def process_website(
    session: aiohttp.ClientSession, user_id: str, website_id: str
) -> bool:
    """Process a single website: create, screenshot, and send email"""
    try:
        # Step 1: Generate website
        params = {"user_id": user_id, "website_id": website_id, "model": "o1-mini"}

        async with session.post(AZURE_FUNCTION_URL, params=params) as response:
            if response.status != 200:
                raise Exception(f"Website generation failed: {await response.text()}")

            logging.info(f"Website {website_id} generated successfully")

        # Wait for a moment to ensure the preview is ready
        await asyncio.sleep(5)

        # Get website details including subdomain
        website_response = (
            supabase.table("websites")
            .select("website_name, subdomain")
            .eq("id", website_id)
            .execute()
        )
        if not website_response.data:
            raise Exception("Website details not found")

        website_name = website_response.data[0]["website_name"]
        subdomain = website_response.data[0]["subdomain"]

        # Step 2: Take screenshot
        screenshot_path = await take_website_screenshot(website_id, subdomain)
        logging.info(f"Screenshot taken for website {website_id}")

        # Step 3: Get user details
        user_response = (
            supabase.table("users")
            .select("email, name, first_name, last_name")
            .eq("id", user_id)
            .execute()
        )
        if not user_response.data:
            raise Exception("User details not found")

        user_data = user_response.data[0]
        user_email = user_data["email"]

        # Try different name fields in order of preference
        user_name = (
            user_data.get("full_name")
            or user_data.get("name")
            or (
                f"{user_data.get('first_name', '')} {user_data.get('last_name', '')}".strip()
                if user_data.get("first_name") or user_data.get("last_name")
                else None
            )
            or user_email.split("@")[0]  # Fallback to email username
            or "there"  # Final fallback
        )

        # Step 4: Send email
        email_content = create_email_content(
            user_name, website_name, subdomain, website_id
        )

        # Read the screenshot file for attachment
        with open(screenshot_path, "rb") as image_file:
            image_content = image_file.read()
            image_base64 = base64.b64encode(image_content).decode()

        message = {
            "content": {
                "subject": email_content["subject"],
                "plainText": f"Hello {user_name}, Your website {website_name} has been regenerated! Please check your email for the full message.",
                "html": email_content["html"],
            },
            "recipients": {"to": [{"address": user_email}]},
            "senderAddress": SENDER_EMAIL,
            "replyTo": [{"address": REPLY_TO_EMAIL}],
            "attachments": [
                {
                    "name": "website-preview.png",
                    "contentType": "image/png",
                    "contentInBase64": image_base64,
                }
            ],
        }

        poller = email_client.begin_send(message)
        result = poller.result()
        logging.info(f"Email sent for website {website_id} to {user_email}")

        # Cleanup screenshot
        # os.remove(screenshot_path)

        return True

    except Exception as e:
        logging.error(f"Error processing website {website_id}: {str(e)}")
        return False


async def main(max_parallel: int, total_to_run: int):
    """Main function to process websites in parallel"""
    # Original code to get failed websites (commented out for now)
    # websites_response = supabase.table("websites").select(
    #     "id, user_id"
    # ).eq("status", "failed").limit(total_to_run).execute()

    # if not websites_response.data:
    #     logging.info("No websites found to process")
    #     return

    # websites = websites_response.data

    # Specific websites to process
    websites = [
        # {"id": "81", "user_id": "a8d5d92f-b745-4b8c-b29e-d704ead7209b"},
        {"id": "31", "user_id": "a8d5d92f-b745-4b8c-b29e-d704ead7209b"},
    ]

    # Create semaphore for parallel control
    semaphore = asyncio.Semaphore(max_parallel)

    async def process_with_semaphore(
        session: aiohttp.ClientSession, user_id: str, website_id: str
    ):
        async with semaphore:
            return await process_website(session, user_id, website_id)

    # Process websites
    async with aiohttp.ClientSession() as session:
        tasks = [
            process_with_semaphore(session, website["user_id"], website["id"])
            for website in websites[:total_to_run]
        ]

        results = await asyncio.gather(*tasks)

        # Summary
        successful = sum(1 for r in results if r)
        failed = len(results) - successful

        logging.info(
            f"""
        Processing completed:
        - Total processed: {len(results)}
        - Successful: {successful}
        - Failed: {failed}
        """
        )


if __name__ == "__main__":
    # Configuration
    MAX_PARALLEL = 5  # Maximum parallel executions
    TOTAL_TO_RUN = 30  # Total number of websites to process

    # Run the async main function
    asyncio.run(main(MAX_PARALLEL, TOTAL_TO_RUN))
