# Python program to demonstrate
# selenium
  
# import webdriver
from selenium import webdriver
  
question = input("Enter Question to be searched - ")

# create webdriver object
driver = webdriver.Chrome()

url = "https://google.co.in/search?q=" + question
print(url)
  
# get google.co.in
driver.get(url)
