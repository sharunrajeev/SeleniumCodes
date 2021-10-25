# Twitch Login using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
  
print('Enter Twitch Login username and password')
username, password = map(str, input().split())
try:
    driver = webdriver.Chrome()
    driver.get('https://www.twitch.tv/login')
    driver.implicitly_wait(15)
  
    loginBox = driver.find_element(By.XPATH, '//*[@id="login-username"]')
    loginBox.send_keys(username)

    passwordBox = driver.find_element(By.XPATH, '//*[@id="password-input"]')
    passwordBox.send_keys(password)
  
    loginButton = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/button/div/div')
    loginButton.click()
  
    print('Login Successful...!!')
except:
    print('Login Failed')
