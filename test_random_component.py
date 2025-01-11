import os
import time
from function_app import fetch_random_component, supabase
from datetime import datetime


def test_random_component(category: str, num_tests: int = 5):
    """
    Test the randomness of component selection by fetching multiple times
    using the actual production function
    """
    print(f"\nTesting random component selection for category: {category}")
    print("-" * 50)

    results = []
    total_start_time = time.time()
    fetch_times = []

    for i in range(num_tests):
        try:
            fetch_start_time = time.time()
            component = fetch_random_component(category)
            fetch_end_time = time.time()
            fetch_duration = fetch_end_time - fetch_start_time
            fetch_times.append(fetch_duration)

            results.append(component)
            print(f"Test {i+1}:")
            print(f"  ID: {component['id']}")
            print(f"  Component ID: {component['component_id']}")
            print(f"  Fetch Duration: {fetch_duration:.3f} seconds")
            print()

            # Small delay to ensure different random seeds
            time.sleep(0.5)

        except Exception as e:
            print(f"Error in test {i+1}: {str(e)}")

    total_duration = time.time() - total_start_time

    # Print timing statistics
    print("\nTiming Statistics:")
    print("-" * 50)
    print(f"Total Duration: {total_duration:.3f} seconds")
    if fetch_times:
        print(f"Average Fetch Time: {sum(fetch_times)/len(fetch_times):.3f} seconds")
        print(f"Fastest Fetch: {min(fetch_times):.3f} seconds")
        print(f"Slowest Fetch: {max(fetch_times):.3f} seconds")

    # Check for uniqueness
    unique_ids = len(set(r["id"] for r in results))
    print(f"\nNumber of unique components returned: {unique_ids} out of {num_tests}")


if __name__ == "__main__":
    while True:
        category = input("\nEnter component category to test (or 'quit' to exit): ")
        if category.lower() == "quit":
            break

        num_tests = input("Enter number of tests to run (default=5): ")
        num_tests = int(num_tests) if num_tests.isdigit() else 5

        test_random_component(category, num_tests)
