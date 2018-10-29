
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie("IEDriverServer.exe")
driver.get("https://www.google.co.in/?gws_rd=ssl")

elem = driver.find_element_by_id("lst-ib")
elem.click()


