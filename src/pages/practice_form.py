class PracticeForm:
    def __init__(self,page):
        self.page=page

        self.forms=self.page.locator("(//div[@class='header-right'])[2]")
        self.practice_form=self.page.locator("(//li[@id='item-0'])[2]")

        self.first_name=self.page.locator("#firstName")
        self.last_name = self.page.locator("#lastName")
        self.submit=self.page.locator("#submit")

    def fill_firstname_lastname_submit(self,firstname,lastname):
        self.forms.click()
        self.practice_form.click()
        self.first_name.type(firstname)
        self.last_name.type(lastname)
        print("Typed First and Last name")