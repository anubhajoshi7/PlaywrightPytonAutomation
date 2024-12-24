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
username = setup_details["username"]
password = setup_details["password"]

@pytest.mark.parametrize("username,password",
                     [(username,password)])
def test_book_store_table(page1, username, password, setup_tear_down):
    print(f"Login succeeded with username {username} and password {password}")
