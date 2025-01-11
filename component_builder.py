from function_app import call_gpt4_api, parse_ai_response


COMPONENT_CATEGORIES = {
    "Navigation": {
        "components": ["MainNavbar", "SideNav", "MegaMenu", "DropdownNav", "MobileNav"],
        "variations": {
            "styles": ["glassmorphic", "floating", "minimal", "gradient", "bordered"],
            "features": [
                "search",
                "notifications",
                "user-profile",
                "multi-level",
                "language-switcher",
            ],
            "layouts": ["centered", "split", "compact", "expanded", "sticky"],
        },
        "requirements": """
        - Smooth reveal animation on page load
        - Glassmorphic backdrop effect
        - Dropdown menus with stagger animations
        - Mobile hamburger with smooth transitions
        - Hover effects with scale and glow
        - Search bar with expanding animation
        - Notification badge with pulse effect
        - User profile with hover card
        - Responsive breakpoint animations
        """,
    },
    "Hero": {
        "components": [
            "MainHero",
            "SplitHero",
            "VideoHero",
            "AnimatedHero",
            "ParallaxHero",
        ],
        "variations": {
            "styles": ["gradient", "video-bg", "particle", "wave", "3d"],
            "features": [
                "scroll-indicator",
                "cta-buttons",
                "social-proof",
                "newsletter",
                "video-modal",
            ],
            "layouts": ["centered", "split", "asymmetric", "fullscreen", "grid"],
        },
        "requirements": """
        - Dynamic background animations
        - Scroll-triggered reveal effects
        - Floating elements with parallax
        - Gradient text animations
        - Interactive CTA buttons
        - Background pattern animations
        - Text reveal sequences
        - Image/video transitions
        - Mouse movement effects
        """,
    },
    "Content": {
        "components": [
            "FeatureGrid",
            "TestimonialCard",
            "PricingTable",
            "BlogCard",
            "TeamMember",
        ],
        "variations": {
            "styles": ["modern", "glassmorphic", "gradient", "minimal", "layered"],
            "features": [
                "hover-effects",
                "animations",
                "interactive",
                "expandable",
                "filterable",
            ],
            "layouts": ["grid", "masonry", "carousel", "list", "columns"],
        },
        "requirements": """
        - Card hover animations
        - Content reveal on scroll
        - Interactive pricing toggles
        - Testimonial carousel
        - Team member hover cards
        - Feature icon animations
        - Grid layout transitions
        - Image lazy loading effects
        - Content filtering animations
        """,
    },
}

GENERATION_PROMPTS = {
    "base_template": """
    Create a {component_type} component for {category} category.
    
    Technical Requirements:
    - Pure HTML
    - Tailwind CSS for styling
    - Vanilla JavaScript where needed (include within script tags)
    - GSAP for smooth animations
    - Framer Motion for interactive animations
    
    Visual Requirements:
    - Modern glassmorphic effects (backdrop-filter)
    - Subtle gradients and shadows
    - Micro-interactions on hover/focus
    - Smooth color transitions
    - Multi-layered depth using shadows
    - High-contrast accessible color schemes
    
    Animation Requirements:
    - Entry animations using GSAP
    - Hover state transitions (scale, opacity, color)
    - Scroll-triggered animations where appropriate
    - Stagger effects for lists/grids
    - Smooth page load transitions
    - Interactive feedback animations
    
    Component Requirements:
    {requirements}
    
    Style Guidelines:
    - Ultra-modern design language
    - Consistent spacing using Tailwind's fluid spacing
    - Mobile-first with smooth breakpoint transitions
    - Dark/light mode with smooth transitions
    - Layered visual hierarchy
    - Subtle border treatments
    
    Additional Features:
    - Loading states with skeleton animations
    - Interactive states with scale/transform effects
    - Smooth reveal animations
    - Accessible but visually rich
    
    Return only the component HTML with any JS in script tags. Do not include boilerplate or CDN imports.
    """,
    "variation": """
    Modify this base {component_type} component:
    
    Style Variation: {style}
    Feature Set: {features}
    Layout: {layout}
    
    Visual Enhancements:
    - Add depth with layered shadows
    - Use gradient overlays for depth
    - Implement micro-interactions
    - Add subtle background patterns
    - Use modern color transitions
    - Include hover/focus effects
    
    Animation Improvements:
    - Smooth entry/exit transitions
    - Hover state animations
    - Scroll-based reveals
    - Loading state animations
    - Interactive feedback
    - Stagger effects for lists
    
    Requirements:
    - Keep pure HTML/Tailwind structure
    - Include JS animations within script tags
    - Maintain accessibility
    - Ensure mobile-first responsiveness
    - Keep dark/light mode support
    
    Return only the modified component code without boilerplate.
    """,
    "optimization": """
    Optimize this component for:
    
    1. Performance:
    - Efficient JavaScript (within script tags)
    - Optimized GSAP/Framer Motion animations
    - Proper event handling
    
    2. Accessibility:
    - Semantic HTML
    - ARIA attributes
    - Keyboard navigation
    
    3. Best Practices:
    - Clean Tailwind classes
    - Organized structure
    - Proper commenting
    
    Return the optimized component code with all JS included in script tags.
    """,
}


def generate_base_component(category: str, component_type: str, model: str = "o1-mini"):
    """Generate base component using AI"""
    prompt = GENERATION_PROMPTS["base_template"].format(
        component_type=component_type,
        category=category,
        requirements=COMPONENT_CATEGORIES[category]["requirements"],
    )

    messages = [{"role": "user", "content": prompt}]

    response = call_gpt4_api(messages, model)
    return parse_ai_response(response, model)


def generate_variation(
    base_component: str, category: str, variation_config: dict, model: str = "o1-mini"
):
    """Generate component variation using AI"""
    prompt = GENERATION_PROMPTS["variation"].format(
        component_type=variation_config["type"],
        style=variation_config["style"],
        features=variation_config["features"],
        layout=variation_config.get("layout", "default"),
    )

    messages = [
        {"role": "user", "content": f"Base component:\n{base_component}\n\n{prompt}"}
    ]

    response = call_gpt4_api(messages, model)
    return parse_ai_response(response, model)


def optimize_component(component: str, model: str = "o1-mini"):
    """Optimize component using AI"""
    messages = [
        {
            "role": "user",
            "content": f"Component to optimize:\n{component}\n\n{GENERATION_PROMPTS['optimization']}",
        }
    ]

    response = call_gpt4_api(messages, model)
    return parse_ai_response(response, model)


def generate_component_set(category: str, model: str = "o1-mini"):
    """Generate a complete set of components for a category"""
    results = {}

    for component_type in COMPONENT_CATEGORIES[category]["types"]:
        # Generate base component
        base = generate_base_component(category, component_type, model)
        results[component_type] = {"base": base, "variations": {}}

        # Generate variations
        for variation in COMPONENT_CATEGORIES[category]["variations"]:
            for style in variation["style"]:
                variation_config = {
                    "type": component_type,
                    "style": style,
                    "features": variation.get("features", ["Basic"])[0],
                    "layout": variation.get("layout", ["Default"])[0],
                }

                variant = generate_variation(base, category, variation_config, model)
                optimized = optimize_component(variant, model)

                results[component_type]["variations"][style] = optimized

    return results


# Add these functions to component_builder.py
import os
import json


def save_component(
    component_code: str, category: str, component_type: str, variation: str = "base"
):
    """Save component with proper HTML structure"""
    # HTML boilerplate
    boilerplate_start = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <!--PAID Tailwind CSS CDN -- DO NOT CHANGE -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Font Awesome CDN  -- DO NOT CHANGE  -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css" />
    <script src=https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js></script>
    <script src="https://cdn.jsdelivr.net/npm/framer-motion@11.15.0/dist/framer-motion.min.js"></script>
    <title>{title}</title>
</head>
<body>"""

    boilerplate_end = """</body>
</html>"""

    # Create directory structure
    base_dir = f"generated_components/{category}/{component_type}"
    os.makedirs(base_dir, exist_ok=True)

    # Prepare complete HTML
    complete_html = (
        boilerplate_start.format(title=f"{component_type} - {variation}")
        + "\n"
        + component_code
        + "\n"
        + boilerplate_end
    )

    # Save as single HTML file
    filename = f"{variation}.html"
    with open(os.path.join(base_dir, filename), "w") as f:
        f.write(complete_html)


def generate_and_save_category(category: str, model: str = "o1-mini"):
    results = generate_component_set(category, model)

    # Save results
    for component_type, variants in results.items():
        # Save base
        save_component(variants["base"], category, component_type)

        # Save variations
        for style, code in variants["variations"].items():
            save_component(code, category, component_type, style)


def calculate_total_components():
    """Calculate total number of components and variations"""
    total = {"base_components": 0, "variations": 0, "total": 0, "breakdown": {}}

    for category, config in COMPONENT_CATEGORIES.items():
        components = len(config["components"])
        variations = (
            len(config["variations"]["styles"])
            * len(config["variations"]["features"])
            * len(config["variations"]["layouts"])
        )

        category_total = components * (1 + variations)  # base + variations

        total["base_components"] += components
        total["variations"] += components * variations
        total["total"] += category_total

        total["breakdown"][category] = {
            "base": components,
            "variations": components * variations,
            "total": category_total,
        }

    return total


if __name__ == "__main__":
    # Configuration
    # MODEL = "o1-mini"  # Change model if needed

    # # Option 1: Generate single component with base only
    # CATEGORY = "Navigation"
    # COMPONENT_TYPE = "MainNavbar"
    # base = generate_base_component(CATEGORY, COMPONENT_TYPE, MODEL)
    # save_component(base, CATEGORY, COMPONENT_TYPE, "base")

    # Option 2: Generate single component with all variations
    # CATEGORY = "Navigation"
    # COMPONENT_TYPE = "MainNavbar"
    # base = generate_base_component(CATEGORY, COMPONENT_TYPE, MODEL)
    # save_component(base, CATEGORY, COMPONENT_TYPE, "base")
    #
    # # Generate variations
    # for variation in COMPONENT_CATEGORIES[CATEGORY]["variations"]:
    #     for style in variation["style"]:
    #         variation_config = {
    #             "type": COMPONENT_TYPE,
    #             "style": style,
    #             "features": variation.get("features", ["Basic"])[0],
    #             "layout": variation.get("layout", ["Default"])[0],
    #         }
    #         variant = generate_variation(base, CATEGORY, variation_config, MODEL)
    #         optimized = optimize_component(variant, MODEL)
    #         save_component(optimized, CATEGORY, COMPONENT_TYPE, style)

    # Option 3: Generate all components in a category (base only)
    # CATEGORY = "Navigation"
    # for component_type in COMPONENT_CATEGORIES[CATEGORY]["types"]:
    #     base = generate_base_component(CATEGORY, component_type, MODEL)
    #     save_component(base, CATEGORY, component_type, "base")

    # Option 4: Generate all components in a category with all variations
    # CATEGORY = "Navigation"
    # generate_and_save_category(CATEGORY, MODEL)

    # Option 5: Generate specific variations for a category
    # CATEGORY = "Navigation"
    # STYLES = ["Minimal", "Modern"]  # Only generate these styles
    # for component_type in COMPONENT_CATEGORIES[CATEGORY]["types"]:
    #     base = generate_base_component(CATEGORY, component_type, MODEL)
    #     save_component(base, CATEGORY, component_type, "base")
    #
    #     for variation in COMPONENT_CATEGORIES[CATEGORY]["variations"]:
    #         for style in variation["style"]:
    #             if style in STYLES:  # Only generate specified styles
    #                 variation_config = {
    #                     "type": component_type,
    #                     "style": style,
    #                     "features": variation.get("features", ["Basic"])[0],
    #                     "layout": variation.get("layout", ["Default"])[0],
    #                 }
    #                 variant = generate_variation(base, CATEGORY, variation_config, MODEL)
    #                 optimized = optimize_component(variant, MODEL)
    #                 save_component(optimized, CATEGORY, component_type, style)

    # Option 6: Generate ALL categories and ALL variations
    # for category in COMPONENT_CATEGORIES.keys():
    #     print(f"Generating category: {category}")
    #     generate_and_save_category(category, MODEL)

    # Option 7: Generate ALL categories but base components only
    # for category in COMPONENT_CATEGORIES.keys():
    #     print(f"Generating base components for category: {category}")
    #     for component_type in COMPONENT_CATEGORIES[category]["types"]:
    #         base = generate_base_component(category, component_type, MODEL)
    #         save_component(base, category, component_type, "base")

    # Calculate totals
    totals = calculate_total_components()
    print("\nComponent Counts:")
    print(f"Base Components: {totals['base_components']}")
    print(f"Total Variations: {totals['variations']}")
    print(f"Total Components: {totals['total']}")
    print("\nBreakdown by Category:")
    for category, counts in totals["breakdown"].items():
        print(f"\n{category}:")
        print(f"  Base Components: {counts['base']}")
        print(f"  Variations: {counts['variations']}")
        print(f"  Total: {counts['total']}")
