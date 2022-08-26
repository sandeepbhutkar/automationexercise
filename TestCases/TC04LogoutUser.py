
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
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
# 5. Verify 'Login to your account' is visible
var1 = driver.find_element(By.XPATH, "//h2[contains(text(),'Login to your account')]").text
try:
    assert var1 == "Login to your account"
except:
    print("Login to your account not visible")
    driver.get_screenshot_as_file("C:\\Users\\sbhutkar\\PycharmProjects\\automationexercise\\Screenshots\\LoginToYourAccountNotVisible.png")
# 6. Enter correct email address and password
driver.find_element(By.CSS_SELECTOR, "input[data-qa=login-email]").send_keys("Ramesh@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[data-qa=login-password]").send_keys("123456")
# 7. Click 'login' button
driver.find_element(By.CSS_SELECTOR, "button[data-qa=login-button]").click()
# 8. Verify that 'Logged in as username' is visible
var2 = driver.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]").text
print(var2)
assert var2 == "Logged in as Ramesh"
# 9. Click 'Logout' button
driver.find_element(By.CSS_SELECTOR, "i.fa.fa-lock").click()
# 10. Verify that user is navigated to login page
assert driver.title == "Automation Exercise - Signup / Login"
driver.close()