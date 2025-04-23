from selenium import webdriver
from selenium.webdriver.common.by import By


# # Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# # Create and configure the Chrome webdriver
# driver = webdriver.Chrome(options=chrome_options)

# # driver.get("https://www.amazon.com")
# driver.get("https://www.amazon.ca/JBL-Vibe-Beam-Wireless-Earbuds/dp/B0BQPNMXQV?pd_rd_w=5DnvZ&content-id=amzn1.sym.39526d57-066e-456c-bc01-eab1026394a8&pf_rd_p=39526d57-066e-456c-bc01-eab1026394a8&pf_rd_r=TEM4HH6BC2EMM8F3RSF7&pd_rd_wg=Lw9c1&pd_rd_r=c3ab5c3c-5138-4d75-bd08-a51d889369e3&pd_rd_i=B0BQPNMXQV&ref_=pd_hp_d_btf_unk_B0BQPNMXQV&th=1")


# # To close the active tab in the browser you just opened use the following
# driver.close()


# # This will close out of the browser it's self
# driver.quit()


# The below code will show to how do the project for day 47

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"${price_dollar.text}.{price_cents.text}")


# Further examples of using selenium webdriver

driver2 = webdriver.Chrome(options=chrome_options)

driver2.get("https://www.python.org/")

search_bar = driver2.find_element(By.NAME, value="q")

print(search_bar.tag_name)

# OR

print(search_bar.get_attribute("placeholder"))

# OR
button = driver2.find_element(By.ID, value="submit")

print(button.size)

# OR

python_docs = driver2.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

print(python_docs.text)

# Using XPATH to find a specific HTML element
bug_link = driver2.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

print(bug_link.text)

# Finding multiple elements
tier_1 = driver2.find_elements(By.CLASS_NAME, value="tier-1")

# Challenge: Print the event dates from python.org
event_times = driver2.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver2.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

# for time in event_times:
#     print(time.text)

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver2.quit()




