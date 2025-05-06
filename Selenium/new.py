from selenium import webdriver
from selenium.webdriver.common.by import By

# To keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options = chrome_options)
driver.get('https://www.python.com')

price_dollar = driver.find_element(By.CLASS_NAME, value = 'a-price-whole')
price_cents = driver.find_elements(By.CLASS_NAME, value = 'a-price-fraction')

print(f'The price is {price_dollar}.{price_cents}')

search_bar = driver.find_element(By.NAME, value = 'q')
print(search_bar)

# Challenge: Print the event dates from python.org
event_times = driver.find_elements(By.CSS_selector, value = '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value = '.event-idget li a')
events = {}

for item in range(len(event_times)):
    events[item] = {
        'time': event_times[item].text,
        'name': event_names[item].text,
    }


for time in event_times:
    print(time.text)

driver.close() # Close will close the particular tab
driver.quit() # Quit will the entire browser