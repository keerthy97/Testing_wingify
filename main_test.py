import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.url = "https://sakshingp.github.io/assignment/login.html"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_login(self):
        username = "keerthi"
        password = "12345"

        self.driver.get(self.url)

        username_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "form-control")))
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_id("password")
        password_input.send_keys(password)

        login_button = self.driver.find_element_by_id("log-in")
        login_button.click()

        assert "Logged in" in self.driver.page_source, "Login failed"

class TestHomePage:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.url = "https://sakshingp.github.io/assignment/login.html"

        cls.driver.get(cls.url)

        username_input = cls.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "form-control")))
        username_input.send_keys("keerthi")
        password_input = cls.driver.find_element_by_id("password")
        password_input.send_keys("12345")
        login_button = cls.driver.find_element_by_id("log-in")
        login_button.click()

        cls.wait.until(EC.visibility_of_element_located((By.ID, "amount")))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_sort_amounts(self):
        amount_header = self.driver.find_element_by_id("amount")
        amount_header.click()

        amounts = self.driver.find_elements_by_xpath("//table[@id='transaction-table']//tr[position() > 1]/td[5]")
        amounts_text = [amount.text for amount in amounts]

        assert amounts_text == sorted(amounts_text), "Amounts in the transaction table are not sorted"

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
