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

# 5. Verify 'New User Signup!' is visible
var1 = driver.find_element(By.XPATH, "//h2[contains(text(),'New User Signup!')]").text
try:
    assert var1 == "New User Signup!"
except:
    print("New User Signup! text is not visible")
    driver.get_screenshot_as_file("C:\\Users\\sbhutkar\\PycharmProjects\\automationexercise\\Screenshots\\NewUserSignUpTextNotVisible.png")

# 6. Enter name and email address
var2 = driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ramesh")
var3 = driver.find_element(By.XPATH, "//body/section[@id='form']/div[1]/div[1]/div[3]/div[1]/form[1]/input[3]").send_keys("Ramesh@gmail.com")

# 7. Click 'Signup' button
driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()

# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
driver.find_element(By.ID,"name").is_displayed()
driver.find_element(By.CSS_SELECTOR,"input[data-qa=email]").is_displayed()

# 9. Fill details: Title, Name, Email, Password, Date of birth
driver.find_element(By.CSS_SELECTOR, "#id_gender1").click()
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
Select(driver.find_element(By.CSS_SELECTOR,"#days")).select_by_visible_text("1")
Select(driver.find_element(By.CSS_SELECTOR,"#months")).select_by_visible_text("July")
Select(driver.find_element(By.CSS_SELECTOR,"#years")).select_by_visible_text("1983")
# 10. Select checkbox 'Sign up for our newsletter!'
driver.find_element(By.CSS_SELECTOR, "#newsletter").click()
# 11. Select checkbox 'Receive special offers from our partners!'
driver.find_element(By.CSS_SELECTOR, "#optin").click()
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
driver.find_element(By.CSS_SELECTOR, "#first_name").send_keys("Ramesh")
driver.find_element(By.CSS_SELECTOR, "#last_name").send_keys("Kumar")
driver.find_element(By.CSS_SELECTOR, "#company").send_keys("CGCGCGC")
driver.find_element(By.CSS_SELECTOR, "#address1").send_keys("address1")
driver.find_element(By.CSS_SELECTOR, "#address2").send_keys("address2")
Select(driver.find_element(By.CSS_SELECTOR, "#country")).select_by_visible_text("India")
driver.find_element(By.CSS_SELECTOR, "#state").send_keys("Maha")
driver.find_element(By.CSS_SELECTOR, "#city").send_keys("Pune")
driver.find_element(By.CSS_SELECTOR, "#zipcode").send_keys("542552")
driver.find_element(By.CSS_SELECTOR, "#mobile_number").send_keys("9977665544")

# 13. Click 'Create Account button'
driver.find_element(By.CSS_SELECTOR, "button[data-qa=create-account]").click()
# 14. Verify that 'ACCOUNT CREATED!' is visible
var4 = driver.find_element(By.XPATH, "/html/body/section/div/div/div/h2/b").text
print(var4)
try:
    assert var4 == "ACCOUNT CREATED!"
except:
    print("Account not created")
    driver.get_screenshot_as_file("C:\\Users\\sbhutkar\\PycharmProjects\\automationexercise\\Screenshots\\AccountNotCreated.png")
# 15. Click 'Continue' button
driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary").click()
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
driver.find_element(By.LINK_TEXT, "Delete Account").click()
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
time.sleep(3)
driver.close()

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and email address
# 7. Click 'Signup' button
# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button


