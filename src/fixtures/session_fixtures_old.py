import os
import pytest
from playwright.sync_api import sync_playwright

storage_state_file = "storage_state_file.json"


@pytest.fixture(scope="module")  # or "session", based on your needs
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        yield browser
    browser.close()


@pytest.fixture(scope="module")
def context(browser):
    # Create a browser context
    context = browser.new_context(ignore_https_errors=True)
    yield context
    context.close()

@pytest.fixture(scope="function")
def save_session_storage(context):
    # This fixture provides a callable to save session storage
    def save_session(base_url, username, password, endpoint):
        if os.path.exists(storage_state_file):
            os.remove(storage_state_file)
        print(f"Saving the session state for user: {username}")

        # Navigate and perform login
        page = context.new_page()
        actual_url=base_url + "/" + endpoint
        print(f"actual url {actual_url}")
        page.goto(actual_url)
        page.locator("#userName").fill(username)
        page.locator("#password").fill(password)
        page.locator("#login").click()
        page.wait_for_url("https://demoqa.com/profile")

        # Save the browser's storage state
        #context.storage_state(path=storage_state_file)
        session = context.storage_state(path=storage_state_file)
        print(f"printing session {session}")
    return save_session


@pytest.fixture(scope="function")
def use_session_storage(context):
    def use_session(base_url, username, password, endpoint):
        try:
            # Load existing session state or create a new one
            if os.path.exists(storage_state_file):
                print(f"Found existing session state for user: {username}")
                new_context = context.browser.new_context(
                    storage_state=storage_state_file,
                    ignore_https_errors=True
                )
            else:
                print(f"No existing session state found for user: {username}. Creating a new one.")
                new_context = context.browser.new_context(ignore_https_errors=True)
                page = new_context.new_page()
                actual_url = f"{base_url}/{endpoint}"
                print(f"Navigating to: {actual_url}")
                page.goto(actual_url)
                page.wait_for_url(actual_url)
                new_context.storage_state(path=storage_state_file)
                page.close()

            # Open a new page with the current context
            page = new_context.new_page()
            return page
        except Exception as e:
            print(f"Error in using session storage: {e}")
            return None
    return use_session
