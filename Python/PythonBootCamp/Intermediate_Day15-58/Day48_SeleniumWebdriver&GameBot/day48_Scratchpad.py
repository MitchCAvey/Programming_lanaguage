from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.ca/dp/B096N8CNBZ/?coliid=I1FMO25TRIQ4O7&colid=2EZCDJT7FQY4R&ref_=list_c_wl_lv_ov_lig_dp_it&th=1")

price_dollor = driver.find_element(By.CLASS_NAME, value='a-price-whole')
price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')

print(f"Current Price is: {price_dollor.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


# driver.close()
driver.quit()