import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Register(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://courses.letskodeit.com/register")

    def test_register(self):
        self.driver.find_element_by_id("name").clear()
        self.driver.find_element_by_id("name").send_keys("Md Maksud Hossain")
        self.driver.find_element_by_id("last_name").clear()
        self.driver.find_element_by_id("last_name").send_keys("Pranto")
        self.driver.find_element_by_id("email").clear()
        mail = self.driver.find_element_by_id("email").send_keys("abc@mail.com")
        self.driver.find_element_by_id("password").clear()
        password = self.driver.find_element_by_id("password").send_keys("167532")
        self.driver.find_element_by_id("password_confirmation").clear()
        self.driver.find_element_by_id("password_confirmation").send_keys("167532")
        self.driver.find_element_by_xpath(
            "//body/div[@id='page']/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[7]/div[1]/input[1]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
