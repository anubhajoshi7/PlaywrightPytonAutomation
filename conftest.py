import pytest

from src.pages.login_page import LoginPage

@pytest.fixture()
def setup_tear_down(page1,username,password):
    loginpage = LoginPage(page1)
    loginpage.go_to_login_page(endpoint="login")
    loginpage.user_login(username,password)