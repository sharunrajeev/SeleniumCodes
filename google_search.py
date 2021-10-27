# Python program to demonstrate
# selenium
  
# import webdriver
from selenium import webdriver
  
# create webdriver object
driver = webdriver.Chrome()

question = input()
url = "https://google.co.in/search?q=" + question
  
# get google.co.in
driver.get(url)
