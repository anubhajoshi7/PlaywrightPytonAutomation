import pytest
from pytest_playwright.pytest_playwright import playwright as playwright

@pytest.fixture(scope="session")
def browser(playwright):
    browser=playwright.chromium.launch(headless=False
                                       )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page1(browser):
    context=browser.new_context()
    page=context.new_page()
    yield page
    context.close()
