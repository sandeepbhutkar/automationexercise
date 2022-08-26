from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
# Test Case 5: Register User with existing email

# 1. Launch browser
driver = webdriver.Chrome(service=Service(executable_path="C:\\Users\\sbhutkar\\PycharmProjects\\automationexercise\\Driver\\chromedriver.exe"))

# 2. Navigate to url 'http://automationexercise.com'
driver.get("http://automationexercise.com")

# 3. Verify that home page is visible successfully
try:
    assert driver.title == "Automation Exercise"
except:
    print("Title mismatched, Home page not loaded successfully")
    driver.get_screenshot_as_file("C:\\Users\\sbhutkar\\PycharmProjects\\automationexercise\\Screenshots\\HomePageNotVisible.png")

# 4. Click on 'Signup / Login' button
driver.find_element(By.LINK_TEXT, "Signup / Login").click()

# 5. Verify 'New User Signup!' is visible
var1 = driver.find_element(By.XPATH, "//h2[contains(text(),'New User Signup!')]").text
try:
    assert var1 == "New User Signup!"
except:
    print("New User Signup! text is not visible")
    driver.get_screenshot_as_file("C:\\Users\\sbhutkar\\PycharmProjects\\automationexercise\\Screenshots\\NewUserSignUpTextNotVisible.png")

# 6. Enter name and already registered email address
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ramesh")
driver.find_element(By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[3]").send_keys("Ramesh@gmail.com")

# 7. Click 'Signup' button
driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()


# 8. Verify error 'Email Address already exist!' is visible
assert driver.find_element(By.XPATH, "//p[contains(text(),'Email Address already exist!')]").text == "Email Address already exist!"

driver.close()