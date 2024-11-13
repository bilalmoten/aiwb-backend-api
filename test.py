# test_components.py
from supabase import create_client
import os
import json

from function_app import fetch_component_base_code, pre_assemble_pages

# supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])


# Test function
def test_fetch_components():
    comp = {
        "homepage": ["navbar-4", "layout-388", "portfolio-118", "footer-1"],
        "about_us": ["navbar-4", "layout-340", "footer-1"],
    }
    all_components = set()
    for page_components in comp.values():
        all_components.update(page_components)

    # Convert to list
    component_list = list(all_components)

    # Fetch component codes from Supabase
    components = fetch_component_base_code(component_list)

    # Convert the structure to JSON string
    comp_json = json.dumps(comp)
    assembled_pages_md = pre_assemble_pages(comp_json, components)
    print(assembled_pages_md)


test_fetch_components()
