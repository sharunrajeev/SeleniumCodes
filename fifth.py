# Python program to demonstrate
# selenium
  
# import webdriver
from selenium import webdriver
  
# create webdriver object
driver = webdriver.Chrome()
  
# get google.co.in
driver.get("https://google.co.in/search?q=geeksforgeeks")