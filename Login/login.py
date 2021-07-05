import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://courses.letskodeit.com/login")

    def test_login(self):
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys("abc@mail.com")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("167532")
        self.driver.find_element_by_xpath(
            "//body/div[@id='page']/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/input[1]").click()
        self.assertEqual("All Courses", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

