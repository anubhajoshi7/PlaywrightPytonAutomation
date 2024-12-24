import tomllib

import pytest

from src.fixtures.session_fixture import page1 as page1
from src.pages.login_page import LoginPage

# Load configuration from TOML file
with open("setup-config.toml", "rb") as data:
    config = tomllib.load(data)

setup_details = config["setup"]

# Extract login credentials
baseurl = setup_details["baseurl"]
actual_username = setup_details["username"]
actual_password = setup_details["password"]


@pytest.mark.parametrize("username,password",
                     [(actual_username,actual_password),
                      ("invalidusername","invalidpassword")])
def test_user_login(page1,username,password):
    loginpage=LoginPage(page1)
    loginpage.go_to_login_page(endpoint="login")
    loginpage.user_login(username,password)

@pytest.mark.parametrize("username,password",
                     [(actual_username,actual_password)])
def test_book_Search(page1,username,password):
    loginpage = LoginPage(page1)
    loginpage.go_to_login_page(endpoint="login")
    loginpage.search_books()

