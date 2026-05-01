from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



driver.get("https://practice.expandtesting.com/login")

time.sleep(2)
user_name = driver.find_element (by=By.ID, value="username")

password = driver.find_element (by=By.ID, value="password")
submit_button = driver.find_element (by=By.ID, value="submit-login")


user_name.send_keys("practice")
password.send_keys("SuperSecretPassword!")
submit_button.click()
time.sleep(10)
driver.quit()