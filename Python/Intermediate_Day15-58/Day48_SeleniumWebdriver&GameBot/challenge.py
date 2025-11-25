from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# # Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
# search.click()
first_name.send_keys("Bruce")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Wayne")

email_address = driver.find_element(By.NAME, value="email")
email_address.send_keys("Bruce.Wayne@WayneEnterprises.com")

# Either of the below submit_button find_element lines below will work
submit_button = driver.find_element(By.CLASS_NAME, value="btn-primary")
# submit_button2 = driver.find_element(By.CSS_SELECTOR, value="form button")
submit_button.click()













