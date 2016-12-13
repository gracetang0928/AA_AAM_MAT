# -*- coding: utf-8 -*-

import sys
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class UIDriver:
	"""Base Page Class Description"""
	def __init__(self,browser="Firefox"):
		"""initialize selenium webdriver, use Firefox as default webdriver"""
		if browser=="Firefox":
			self._driver=webdriver.Firefox()
		elif browser=="Chrome":
			self._driver = webdriver.Chrome()
		elif browser=="IE":
			self._driver=webdriver.Ie()
		else:
			print browser,"can't recognize, will use firefox start testing "
			self._driver = webdriver.Firefox()
			
	def quitDriver(self):
		if(self._driver):
			self._driver.quit()
	"""
	Open web url

	Usage:
	self.openURL(url)
	"""
	def get(self,url):

		if url !="":
			self._driver.get(url)
		else:
			raise ValueError("Please provide a correct base url. ")
	"""
	Maximize current browser window
	"""
	def maxWindow(self):
		if(self._driver):
			self._driver.maximize_window()

	"""
	Get window title
	"""
	def getTitle(self):
		return self._driver.title

	"""
	Get current url
	"""
	def getCurrentUrl(self):
		return self._driver.current_url
	"""
	保存当前的屏幕截图到电脑上指定位置

	:Args:
		 - targetPath: 电脑上保存图片的位置

	:Usage:
		self.saveScreenshot("c:\test_POI1.jpg")
	"""
	def saveScreenshot(self,targetPath):
		self._driver.get_screenshot_as_file(targetPath)
	"""
	Refresh current page
	"""
	def F5(self):
		self._driver.refresh()

	"""
	Get element attribute

	"""
	def getAttribute(self, element, attribute):
		return element.get_attribute(attribute)
	"""
	给定控件的xpatch, id 或者name来查找控件

	:Args:
		- controlInfo: 控件的信息，可以是xpath,id或者其他属性

	:Return:
		如果找到控件，返回第一个

	:Usage:
		self.findElement(elementInfo)
	"""
	def findElement(self, elementInfo):
		element = None
		try:
			element = self._driver.find_element(*elementInfo)          
		except :
			print "Error : Can't find element ", elementInfo                    
		return element

	"""
	给定控件的xpatch, id 或者name来查找控件

	:Args:
		- controlInfo: 控件的信息，可以是xpath,id或者其他属性

	:Return:
		返回所有满足条件的控件，返回的类型是一个列表

	:Usage:
		self.findElements(controlInfo)
	"""
	def findElements(self, controlInfo):
		elements = None
		try :
			elements = self._driver.find_element(*controlInfo)          
		except:	
			print "Error : Can't find elements ", controlInfo                      
		return element

	"""
	在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件

	:Args:
		- parentElement: 父控件，是一个已知的WebElement
		- childElementInfo: 子控件的信息，可以是xpath,id或者其他属性

	:Return:
		如果找到控件，返回第一个

	:Usage:
		self.findElement(controlInfo)
	"""
	def findElementInParentElement(self, parentElementInfo, childElementInfo):
		element = None
		try:
			parentElement = self.findElement(parentElementInfo)
			element = parentElement.find_element(*childElementInfo)
		except:
                #如果通过名称不能找到则通过class name查找
			print parentElementInfo,childElementInfo ,": Can't find such element. Please check the element information"

		return element

	"""
	在一个已知的控件中通过给定控件的xpatch, id 或者name来查找子控件

	:Args:
		- parentElement: 父控件，是一个已知的WebElement
		- childElementInfo: 子控件的信息，可以是xpath,id或者其他属性

	:Return:
		如果找到控件，返回所有符合条件的控件

	:Usage:
		self.findElementsInParentElement(parentElement, controlInfo)
	"""
	def findElementsInParentElement(self, parentElementInfo, childElementInfo):
		elements = ""
		try:
			parentElement = self.findElement(parentElementInfo)
			elements = parentElement.find_elements(*childElementInfo)
		except:
                #如果通过名称不能找到则通过class name查找
			print parentElementInfo, childElementInfo, ": Can't find such element. Please check the element information"

		return elements

	"""
	点击某一个控件，如果改控件不存在则会抛出异常

	:Args:
		- elementInfo: 控件的信息，可以是xpath,id或者其他属性

	:Usage:
		self.clickElement(elementInfo)
	"""
	def clickElement(self, elementInfo):
		element = self.findElement(elementInfo)
		element.click()

	def clickElementEntity(self,element):
		element.click()

	def getTextOfElement(self, elementInfo):
		element = self.findElement(elementInfo)
		return element.text

	def getTextOfElementEntity(self,element):
		return element.text
	"""
	清除文本框里面的文本

	:Usage:
		self.clearTextEdit(elementInfo)
	"""
	def clearTextEdit(self, elementInfo):
		element = self.findElement(elementInfo)
		element.clear()
	"""
	切换到iframe，以便查找元素
	:Args:
		- windowName: window的信息
	:Usage:
		self.switchToWindow(window)
	"""

	def switchToWindow(self, windowName):
		self._driver.switch_to_window(windowName)

	"""
	切换到iframe，以便查找元素
	:Args:
		- iframeInfo: iframe的信息，可以是xpath,id或者其他属性
	:Usage:
		self.swithToIframe("1frame2")
	"""

	def switchToIframe(self,iframeInfo):
		self._driver.switch_to_frame(iframeInfo)
	"""
	切换到默认主窗口

	:Usage:
		self.swithToDefaultContent()
	"""

	def swithToDefaultContent(self):
		self._driver.switch_to_default_content()
	"""
	切换到提示框

	:Usage:
		self.switchToAlert()
	"""
	def switchToAlert(self):
		sef._driver.switch_to_alert()


	def switchToDefaultContent(self):
		self._driver.switch_to_default_content()
######################################################################################################################3
#	"""
#	等待某个控件显示
#
#	:Args:
#		- elementInfo: 控件的信息，可以是xpath,id或者其他属性
#		- period：等待的秒数
#
#	:Usage:
#		self.waitForElement(elementInfo, 3)
#	"""
#	def waitForElement(self, elementInfo, period):
#		try:
#			element = WebDriverWait(self._driver,period).until(EC.element_to_be_clickable(elementInfo))
#		except:
#			raise Exception("Cannot find %s in %d seconds" %(elementInfo,period))
#
#
######################################################################################################################3
#		for i in range (0, period):
#			sleep(1)
#			try:
#				self.checkElementIsShown(elementInfo)
#				return
#			except:
#				continue
#######################################################################################################################
#		
#
#	"""
#	等待某个控件不再显示
#
#	:Args:
#		- elementInfo: 控件的信息，可以是xpath,id或者其他属性
#		- period：等待的秒数
#
#	:Usage:
#		self.waitForElementNotPresent(elementInfo, 3)
#	"""
#	def waitForElementNotPresent(self, elementInfo, period):
#		for i in range (0, period):
#			sleep(1)
#           #不存在了则返回
#			if(not self.checkElementIsShown(elementInfo)):
#				return
#			else:
#				continue
#
#		raise Exception("Cannot find %s in %d seconds" %(elementInfo,period))
#######################################################################################################################
	"""
	判断某个控件是否显示

	:Args:
		- elementInfo: 控件的信息，可以是xpath,id或者其他属性
	:Return:
		True: 如果当前画面中期望的控件能被找到

	:Usage:
		self.checkElementIsShown(elementInfo)
	"""

	def checkElementIsShown(self, elementInfo):
		try:
			element = self.findElement(elementInfo)
			if(element.is_display()):
				return True
			else:
				return False
		except:
			return False
	"""
	设置某个控件显示的文本，如果该控件不能找到则会抛出异常

	:Args:
		- elementInfo: 控件的信息，可以是xpath,id或者其他属性
		- textInfo: 输入的文本信息

	:Return:
		返回该控件显示的文本

	:Usage:
		self.setTextToElement(elementInfo,"Hello")

	"""
	def setTextToElement(self,elementInfo,textInfo):
		element = self.findElement(elementInfo)
		if (textInfo!=Keys.TAB):
			element.clear()
		element.send_keys(textInfo)

	"""
	判断某个控件是否显示在另外一个控件中

	:Args:
		- parentElement: 父控件，是一个已知的WebElement
		- childElementInfo: 子控件的信息，可以是xpath,id或者其他属性
	:Return:
		True: 如果当前画面中期望的控件能被找到

	:Usage:
		self.checkElementShownInParentElement(elementInfo)
	"""
	def checkElementShownInParentElement(self, parentElement, childElementInfo):
		try:
			self.findElementInParentElement(parentElement, childElementInfo)
			return True
		except:
			return False

	"""
	判断某个控件是否被选中

	:Args:
		- elementInfo: 控件的信息，可以是xpath,id或者其他属性
	:Return:
		True: 如果当前画面中期望的控件能被选中

	:Usage:
		self.checkElementIsSelected(elementInfo)
	"""
	def checkElementIsSelected(self, elementInfo):
		element = self.findElement(elementInfo)
		return element.is_selected()

	"""
	判断某个开关控件是否被选中

	:Args:
		- elementInfo: 控件的信息，可以是xpath,id或者其他属性
	:Return:
		True: 如果当前画面中期望的控件能被选中

	:Usage:
		self.checkElementIsChecked(elementInfo)
	"""
	def checkElementIsChecked(self, elementInfo):
		element = self.findElement(elementInfo)
		if(element.get_attribute("checked") == "false"):
			return False
		else:
			return True
	"""
	判断摸个控件是否enabled
	:Args:
		- elementInfo: 控件的信息，可以是xpath,id或者其他属性
	:Return:
		True: 如果当前画面中期望的控件enabled

	:Usage:
		self.checkElementIsEnabled(elementInfo)
	"""
	def checkElementIsEnabled(self, elementInfo):
		element = self.findElement(elementInfo)
		return element.get_attribute("enabled")

	def getWindowHandles(self):
		return self._driver.window_handles

	def getCurrentWindowHandle(self):
		return self._driver.current_window_handle

	def getCurrentUrl(self):
		return self._driver.current_url

	def closeWindow(self):
		self._driver.close()

	def waitForElementPresent(self, elementInfo, period):
		element = None
		try:
			element = WebDriverWait(self._driver,period).until(EC.presence_of_element_located(elementInfo))
			
		except:
			print ("Error :　Cannot find %s in %d seconds" %(elementInfo,period))
		return element

	def waitForElementNotPresent(self, elementInfo, period):
		try:
			element = WebDriverWait(self._driver,period).until_not(EC.presence_of_element_located(elementInfo))
		except:
			pass


	def waitForElementClickable(self, elementInfo, period):
		element = None
		try:
			element = WebDriverWait(self._driver,period).until(EC.element_to_be_clickable(elementInfo))
		except:
			print ("Error : Cannot find %s in %d seconds" %(elementInfo,period))
		return element

	def waitForFrameAvailableAndSwitch(self, frameInfo,period):
		try:
			element = WebDriverWait(self._driver,period).until(EC.frame_to_be_available_and_switch_to_it(frameInfo))
		except:
			print ("Error : Cannot find %s in %d seconds" %(frameInfo,period))
