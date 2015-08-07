#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#-*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import os
import re,sys


class LoginTest(unittest.TestCase):
	def setUp(self):
		os.system("say i am trying to connect!")
		self.driver =webdriver.PhantomJS()  #PhantomJS() #Chrome() 
		self.driver.get("https://www.haberturk.com")
		

	def test_Login(self):
		text = "habertürkü açtım"
		os.system("say -v Cem "+text.decode('utf-8').encode(sys.stdout.encoding))
		driver = self.driver
		html_source = driver.page_source

		#print(html_source)

		matchObj = re.search('<a title="(.*?)"', html_source, re.M|re.I)

		HaberArray=re.findall('<a title="(.*?)"', html_source)
		for m in HaberArray:
	        	print "%s" % (m)
	        	os.system("say -v Cem "+m.encode('utf8'))

		#!/usr/bin/env python
		# -*- coding: utf-8 -*- 

		if matchObj:
   			print "match: ", matchObj.group(1)
   			os.system("say -v Cem "+matchObj.group(1).decode('utf-8').encode(sys.stdout.encoding))


		#<a class="owl-numbers" title="Demirtaş hakkında soruşturma" href="/gundem/haber/1109382-demirtas-hakkinda-sorusturma" target="_blank">1</a>
		
	def tearDown(self):
		self.driver.quit()





if __name__ == '__main__':
	os.system("say  checking  news")
	unittest.main()
