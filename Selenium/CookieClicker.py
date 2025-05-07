from selenium import webdriver
from selenium.webdriver.common.by import By # locate elements on a web page
import time


# Optional - Keep the browser open

chrome_options = webdriver.ChromeOptions() # instance of ChromeOptions, which allows you to customize how the Chrome browser launches
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options = chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(by = By.ID, value = 'cookie')

# Get upgraade item ids
 
items = driver.find_elements(by = By.CSS_SELECTOR, value = '#store div')
item_ids = [item.get_attribute('id') for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5 minutes

while True:
    cookie.click()
    
    if time.time() > timeout:
        
        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by = By.CSS_SELECTOR, value = '#store b')
        item_prices = []
        
        
        # Convert <b> text into an integer price
        for price in all_prices:
            element_text = price.text
            if element_text != '':
                cost = int(element_text.split('-')[1].strip().replace(',',''))
                item_prices.append(cost)
                
                
        # Get current cookie count
        money_element = driver.find_element(by = By.ID, value = 'money').text
        if "," in money_element:
            money_element = money_element.replace(',','')
        cookie_count = int(money_element)
        
        
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
            
        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgarde = max(affordable_upgrades)
        print(highest_price_affordable_upgarde)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        
        driver.find_element(by = By.ID, value = to_purchase_id).click()
        
        
        # Add another 5 seconds until the next check
        timeout = time.time() + 5
        
        
# After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by = By.ID, value = 'cps').text
        print(cookie_per_s)
        break