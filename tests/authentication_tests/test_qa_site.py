import os

from playwright.sync_api import sync_playwright
storage_state_file = "storage_state_file.json"

def test_demoqa_session_storage():
    with sync_playwright() as p:
        if os.path.exists(storage_state_file):
            os.remove(storage_state_file)
        print(f"Saving the session state for user: testuser")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to the login page
        page.goto("https://demoqa.com/login")

        # Fill in the login form
        page.locator("#userName").fill("testuser")
        page.locator("#password").fill("Test@123")
        page.locator("#login").click()

        # Wait for navigation after login
        page.wait_for_url("https://demoqa.com/profile")

        # Retrieve the stored session data from localStorage
        user_data = page.evaluate("() => localStorage.getItem('user')")
        print(f"User data stored in localStorage: {user_data}")

        # Save storage state for future use
        context.storage_state(path=storage_state_file)

        # Close the browser
        browser.close()
