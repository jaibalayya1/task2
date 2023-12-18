import unittest
from selenium import webdriver

class TestATGWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # You may need to download and set the path for the WebDriver (e.g., ChromeDriver)

    def test_website_loads(self):
        self.driver.get("https://atg.world")
        self.assertIn("ATG", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
