import unittest
from Batch_Testing.Registration.register import Register
from Batch_Testing.Login.login import Login
from Batch_Testing.Purchase.purchase_course import PurchaseCourse
from HtmlTestRunner import HTMLTestRunner


class MyTestSuite(unittest.TestCase):
    def test_suite(self):
        self.test1 = unittest.TestLoader().loadTestsFromTestCase(Register)
        self.test2 = unittest.TestLoader().loadTestsFromTestCase(Login)
        self.test3 = unittest.TestLoader().loadTestsFromTestCase(PurchaseCourse)
        suite = unittest.TestSuite([self.test1, self.test2, self.test3])
        runner = HTMLTestRunner(output="Report", title="Unit Test Report", open_in_browser=True)
        runner.run(suite)


if __name__ == "__main__":
    test_suite()
print("""
All Test Cases Executed Successfully !!
""")
