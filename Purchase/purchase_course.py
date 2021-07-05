from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Batch_Testing.Login.login import Login
import unittest


class PurchaseCourse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://courses.letskodeit.com/login")

    def test_course(self):
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys("abc@mail.com")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("167532")
        self.driver.find_element_by_xpath(
            "//body/div[@id='page']/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/input[1]").click()
        self.driver.find_element_by_xpath("//h4[contains(text(),'Selenium WebDriver With Python 3.x')]").click()
        self.driver.find_element_by_xpath("//button[contains(text(),'Enroll in Course')]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
