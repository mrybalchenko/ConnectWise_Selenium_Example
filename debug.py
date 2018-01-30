from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.connectwise.com")
driver.maximize_window()
driver.find_element_by_css_selector("li[data-node='86625e09-631a-4e54-8a53-560b8e98269a']").click()

sleep(1)


#driver.find_element_by_xpath("//*[contains(@class, 'Title') and contains(@title, 'Need Help?')]").click()
#//a[contains(@id, 'ctl00_btnAircraftMapCell') and contains(@title, 'Select Seat')]

driver.find_element_by_xpath("//P[contains(text(),'Get support now ')]").click()

#driver.find_element_by_css_selector("a[href='https://www.connectwise.com:443/services/support']").click()

FirstName = "field0"
LastName = "field1"
Company = "field2"

driver.find_element_by_id(FirstName).send_keys("Mikhail")
driver.find_element_by_id(LastName).send_keys("Rybalchenko")
driver.find_element_by_id(Company).send_keys("TestCompany")

driver.find_element_by_id("fileUploader").send_keys("C:/Users/mrybalchenko/Desktop/test-img.png")

