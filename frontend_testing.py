# Frontend testing script

# Libraries: selenium webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service("C:\ChromeDriver\chromedriver.exe"))
# Driver navigates to url and providing ID value
driver.get("http://127.0.0.1:5001/users/get_user_data/1")
# Try to find element by ID "user", if succeeded, print the user_name
try:
    print(driver.find_element(By.ID, value="user").text)
# If failed above attempt, raise "test failed" error
except:
    raise Exception("test failed")