# Assignment: Develop a simple automated test script using Python) and a testing 
# framework (e.g., Selenium, Appium) to automate the login process of a sample web application

#Importing the required libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Setting the username and password
username = "Orvil"
password = "password"

#initializing the webdriver 
driver = webdriver.Chrome("d:\Development\Github\chromedriver_win32\chromedriver.exe")

#Opening the website
driver.get("https://mv-i.github.io/me/projects/login/dummy.html")


#send keys to input fields
driver.find_element("id", "loginUsernameEmail").send_keys(username)

driver.find_element("id", "loginPassword").send_keys(password)


# click login button to submit form after filling in username and password
# wait for the button to be clickable
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form__button")))

# Click the button
button.click()


# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
