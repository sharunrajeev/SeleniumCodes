from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.implicitly_wait(1)

browser.get('https://www.instagram.com/')

sleep(1)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("Sharun")
password_input.send_keys("ThisIsPassword")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(9999999)

browser.close()