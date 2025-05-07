from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Create and configure the chrome webdriver
driver = webdriver.Chrome(options = chrome_options)

# Navigate to the Wikipedia
driver.get('https://secure-retreat-92358.herokuapp.com/')


article_count = driver.find_element(By.CSS_SELECTOR, value = '#articlecount a')
article_count.click()


# Find the Search input by name
first_name = driver.find_element(By.NAME, value = 'fName')
last_name = driver.find_element(By.NAME, value = 'lName')
email = driver.find_element(By.NAME, value = 'email')


first_name.send_keys('Neeraj')
last_name.send_keys('Mn')
email.send_keys('Neerajmn20@gmail.com')


submit = driver.find_element(By.CSS_SELECTOR, value = 'form button')
submit.click()