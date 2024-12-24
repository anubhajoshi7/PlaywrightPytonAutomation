import tomllib
import requests

class LoginPage:
    with open("setup-config.toml", "rb") as data:
        config = tomllib.load(data)
        setup_details = config["setup"]
        # Extract login credentials
        baseurl = setup_details["baseurl"]

    @property
    def url(self):
        return self.page.url

    def content(self):
        return self.page.content()

    def __init__(self,page):
        self.page=page

        self.username=self.page.locator("#userName")
        self.password=self.page.locator("#password")
        self.login=self.page.locator("#login")
        self.new_user=self.page.locator("#newUser")
        self.book_store_application=self.page.locator('//*[@id="app"]/div/div/div/div[1]/div/div/div[6]/span/div/div[2]/div[2]')
        self.book_store=self.page.locator('(//*[@id="item-2"]/span)[5]')
        self.forms=self.page.locator('//*[@id="app"]/div/div/div/div[1]/div/div/div[2]/span/div/div[2]/div[2]')
        self.practice_form=self.page.locator('(//*[@id="item-0"]/span)[2]')
        self.login_error=self.page.locator("//p[text()='Invalid username or password!']")
        self.logout = self.page.locator("//button[text()='Log out']")
        self.search_books=self.page.get_by_placeholder("Type to search")
        self.delete_book=self.page.locator("//span[@id='delete-record-undefined']")

    def go_to_login_page(self,endpoint:str):
        url=self.baseurl+"/"+endpoint
        self.page.goto(url)

    '''
    def user_login(self,username:str,password:str):
        print(f"Login with username {username} and password {password}")
        self.username.type(username)
        self.password.type(password)
        self.login.scroll_into_view_if_needed()
        assert self.login.is_enabled()
        with self.page.expect_response("**/Login") as response_info:
            self.login.click(force=True)
        response = response_info.value  # Get the actual Response object
        print(f"response: {response}")
        print(f"status code: {response.status}")

        #self.page.wait_for_navigation(timeout=5000)
        response = response_info.value
        print(f"Response URL: {response.url}, Status code: {response.status}")

        if response.status == 200:
            self.page.wait_for_url("**/profile")
            print(f"Current URL: {self.page.url}")
            assert "profile" in self.page.url
        else:
            print("Invalid login response detected.")
            assert "invalid" in self.page.content()

        #self.page.wait_for_navigation(timeout=5000)
        return self.page,response.status

    def user_login(self, username: str, password: str):
        print(f"Login with username {username} and password {password}")
        self.username.type(username)
        self.password.type(password)
        self.login.scroll_into_view_if_needed()

        # Track if API was triggered
        api_response_handled = False

        try:
            with self.page.expect_response("**/Login", timeout=10000) as response_info:
                self.login.click(force=True)
            response = response_info.value
            print(f"response: {response}")
            print(f"status code: {response.status}")
            api_response_handled = True
        except TimeoutError:
            print("Login API not triggered, likely invalid credentials.")

        # Wait for UI-based validation (in case of invalid credentials)
        if api_response_handled:
            # Check for valid login
            self.page.wait_for_url("**/profile")
            print(f"Current URL after login: {self.page.url}")
            assert "profile" in self.page.url, "Valid login failed to redirect"
        else:
            # Handle invalid login (check for error message on page)
            error_message_locator = self.page.locator("//p[text()='Invalid username or password!']")  # Replace with actual selector
            assert error_message_locator.is_visible(), "Invalid username or password!"
            print(f"Error message displayed: {error_message_locator.text_content()}")

        return self.page'''

    def user_login(self, username: str, password: str):
        print(f"Login with username {username} and password {password}")
        self.username.type(username)
        self.password.type(password)
        self.login.scroll_into_view_if_needed()

        # Trigger the login button click
        self.login.click(force=True)
        self.page.wait_for_timeout(5000)
        #self.page.wait_for_load_state('domcontentloaded')

        if self.logout.is_visible():
            #Check if the profile page is navigated to (valid login)
            self.page.wait_for_url("**/profile", timeout=10000)
            print(f"Login successful. Current URL: {self.page.url}")
            assert "profile" in self.page.url, "Valid login failed to redirect to profile"
        else:
            # If login failed, check for the error message (invalid login)
            print("Login failed, checking for error message.")
            error_message_locator = self.page.locator(
                "p:has-text('Invalid username or password!')")  # Use the actual selector
            if error_message_locator.is_visible():
                print(f"Error message displayed: {error_message_locator.text_content()}")
                assert "Invalid username or password!" in error_message_locator.text_content(), "Unexpected error message"
            else:
                print("Unexpected behavior: No error message displayed.")
                assert False, "Invalid login did not trigger an error message"

        return self.page

    def new_user(self):
        self.new_user().is_enabled()
        self.new_user().click()
        return self.page

    def book_Search(self):
        self.search_books.type("Speaking")
        self.delete_book.click()

    def book_store_application(self):
        self.book_store_application.click()
        return self.page



    def book_store(self):
        self.book_store().click()
        return self.page



    def forms(self):
        self.forms().click()
        return self.page



    def practice_form(self):
        self.practice_form().click()
        return self.page
