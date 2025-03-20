from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome Options (to bypass bot detection)
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open Login Page
    driver.get("https://mticket.pythonanywhere.com/users/login/")  # Update if needed
    time.sleep(2)  # Let page load

    # Step 2: Locate Input Fields & Enter Credentials
    username_field = driver.find_element(By.NAME, "username")  # Update selector
    password_field = driver.find_element(By.NAME, "password")  # Update selector

    username_field.send_keys("geethika")  # Replace with your username
    password_field.send_keys("Akhil@456")  # Replace with your password
    password_field.send_keys(Keys.RETURN)  # Press Enter to submit

    # Step 3: Verify Login Success
    time.sleep(3)  # Wait for response
    print("✅ Login attempt completed!")

except Exception as e:
    print(f"❌ Test Failed: {e}")

finally:
    driver.quit()  # Close the browser
