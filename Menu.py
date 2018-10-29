from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver: WebDriver = webdriver.Chrome("../chromedriver.exe")  #to open chrome browser
#driver: WebDriver = webdriver.Firefox(executable_path="../geckodriver.exe")
driver.get("https://ybl-robot-staging-widget.payjo.co/")
#driver.get("https://www.yesbank.in/")
delay = 60

myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"//div[@class='payjo-image-container']"))) #to find the location of the bot
myElem.click()    #clicking on the bot