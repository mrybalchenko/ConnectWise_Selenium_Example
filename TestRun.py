import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

class ConnectWise_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_CreateSupportTicket(self):
        driver = self.driver
        driver.get("https://www.connectwise.com")
        driver.maximize_window()
        driver.find_element_by_css_selector("li[data-node='86625e09-631a-4e54-8a53-560b8e98269a']").click()
        driver.find_element_by_xpath("//P[contains(text(),'Get support now ')]").click()

        FirstName = "field0"
        LastName = "field1"
        Company = "field2"
        EmailAddress = "field3"
        BusinessPhone = "field4"
        Product = "field5"
        Summary = "field6"
        IssueDetails = "field7"

        driver.find_element_by_id(FirstName).send_keys("Mikhail")
        driver.find_element_by_id(LastName).send_keys("Rybalchenko")
        driver.find_element_by_id(Company).send_keys("TestCompany")
        driver.find_element_by_id(EmailAddress).send_keys("mrybalchenko93@gmail.com")
        driver.find_element_by_id(BusinessPhone).send_keys("555-555-5555")
        driver.find_element_by_id(Product).send_keys("ConnectWise Automate")
        driver.find_element_by_id(Summary).send_keys("Test")
        driver.find_element_by_id(IssueDetails).send_keys("No Issues")
        driver.find_element_by_id("fileUploader").send_keys("C:/Users/mrybalchenko/Desktop/test-img.png")
        #driver.find_element_by_css_selector("input[value='Submit']").click()
        sleep (10)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()