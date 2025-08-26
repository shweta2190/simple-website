import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestWebpageString(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f'--user-data-dir=/tmp/chrome-user-data-{time.time()}')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8000/")
        time.sleep(2)  # Wait for page to load

    def test_string_present(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.assertIn("Programming and for Policymakers [DPI-691M]", body.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
