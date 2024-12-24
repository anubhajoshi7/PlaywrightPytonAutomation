import tomllib
import pytest
from src.fixtures.session_fixtures_old import save_session_storage

# Load configuration from TOML file
with open("setup-config.toml", "rb") as data:
    config = tomllib.load(data)

setup_details = config["setup"]

# Extract login credentials
baseurl = setup_details["baseurl"]
username = setup_details["username"]
password = setup_details["password"]


@pytest.mark.parametrize(
    "username, password, endpoint",
    [(username, password, "login")],
)
def test_set_session(username, password, endpoint, save_session_storage):
    # Testing if able to save session storage in a file
    save_session_storage(baseurl, username, password, endpoint)












'''
@pytest.mark.parametrize(
    "username, password, endpoint",
    [(username, password, "profile")],
)
def test_use_session(username, password, endpoint, use_session_storage):
    # Testing if able to save session storage in a file
    use_session_storage(baseurl, username, password, endpoint)'''