#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import os
import re


class LoginTest(unittest.TestCase):
	def setUp(self):
		os.system("say i am trying to connect!")
		self.driver =webdriver.PhantomJS()  #PhantomJS() #Chrome() 
		self.driver.get("https://www.facebook.com")
		

	def test_Login(self):
		os.system("say i am at login page!")
		driver = self.driver
		facebookUserName = "caglayanserbetci@gmail.com"
		facebookPassword = "Ca64669295"

		emailFieldID     = "email"
		passwordFieldID  = "pass"
		loginButtonXPath = "//input[@value='Log In']"
		notificationButtonXpath = "//a[@name='notifications']"
		fbLogoXPath      = "(//a[contains(@href,'logo')])[1]"
 
		emailFieldElement  = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldID))
		passFieldElement   = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passwordFieldID))
		loginButtonElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath (loginButtonXPath))

		emailFieldElement.clear()
		emailFieldElement.send_keys(facebookUserName)

		passFieldElement.clear()
		passFieldElement.send_keys(facebookPassword)

		loginButtonElement.click()

		os.system("say i filled login page")

		#WebDriverWait(driver,20).until(lambda driver: driver.find_element_by_xpath (fbLogoXPath))
		#notificationButtonElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath (notificationButtonXpath))

		#notificationButtonElement.click()

		html_source = driver.page_source

		#print html_source
		os.system("say now, i am in!")
		
		matchObj = re.search('id="notificationsCountValue">(.)', html_source, re.M|re.I)

		MessageObj = re.search('id="mercurymessagesCountValue">(.)', html_source, re.M|re.I)

		RequestObj = re.search('id="requestsCountValue">(.)', html_source, re.M|re.I)

		if matchObj:
   			print "match: ", matchObj.group(1)
   			os.system("say you have "+matchObj.group(1)+" notifications")
   			os.system("say "+MessageObj.group(1)+" messages")
   			os.system("say and  "+RequestObj.group(1)+" friends request")

   
		else:
   			print "No match!!"
   			os.system("say problem")
			

	def tearDown(self):
		self.driver.quit()





if __name__ == '__main__':
	os.system("say  checking your facebook account.")
	unittest.main()
