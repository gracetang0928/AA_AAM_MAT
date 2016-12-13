# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time
import datetime

############################################################################
# Public Function
############################################################################

# Generate Asset ID When new asset
def generatNowStr():
	nowTime = datetime.datetime.now().strftime("%m%d%H%M%S")
	return nowTime

# Random select a record to update or delete
def generatLineNO(numberInfo):
	num = int(generatNowStr())
	lineNO = str(num%numberInfo+1)
	return lineNO


############################################################################
# Every page has this iframe element
############################################################################
	
class BasePage(object):
	containerIframe = (By.ID,"iframe-page-container")

	def __init__(self,uiDriver):
		self.uidriver = uiDriver
	
	def closeEMSE(self,localhandle):
		sleep(8)
		allhandles = self.uidriver.getWindowHandles()
		if (len(allhandles)>1):
			for handle in allhandles:
				if handle!=localhandle:
					self.uidriver.switchToWindow(handle)
					break	
			self.uidriver.closeWindow()	
		self.uidriver.switchToWindow(localhandle)
		sleep(5)

	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	#	Every portlet page contain page container iframe , then every page need the method
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def switchToContainer(self):
		self.uidriver.switchToDefaultContent()
		self.uidriver.waitForElementPresent(BasePage.containerIframe,30)
		# sleep(10)
		self.uidriver.switchToIframe("iframe-page-container")

	"""
		Make the uidriver switch to portlet iframe
		- iframeInfo : iframe entity or id of iframe	
	"""
	def switchToCurrentPortletForm(self,iframeInfo):
		self.switchToContainer()
		self.uidriver.waitForFrameAvailableAndSwitch(iframeInfo,70)
		if ((self.uidriver.getCurrentUrl()).find("server")>0):
			# Local site , just sleep shoter time 
			# Not local site, sleep longer time
			sleep(3)
		else:
			sleep(7)


class BasicListView(BasePage):
	
	searchButton = (By.ID,"a_search")
	newButton = (By.ID,"a_new")
	deleteButton =(By.ID,"delete")

	dataTable = (By.ID,"AccelaMainTable")
	firstLineData = (By.ID,"row1")

	# Message in list view
	errorMsg = (By.ID,"errorMsgPanel")
	
	lineNO = generatLineNO(2)
	lineData = (By.ID,"row"+lineNO)
	lineDataLink = (By.ID,"linkrow"+lineNO)
	noResult = (By.ID,"popNorecord")

	def __init__(self,uiDriver,portlet):
		super(BasicListView,self).__init__(uiDriver)
		self.mainIframe = (By.ID,portlet+"List")
		self.lineDataCheckbox = (By.XPATH, '//input[@name="value(chk_%s,%d)"]'%(portlet,int(BasicListView.lineNO)-1))



	def clickSearch(self):
		self.switchToCurrentPortletForm(self.mainIframe[1])
		self.uidriver.clickElement(BasicListView.searchButton)

	def selectRecordInList(self):
		self.switchToCurrentPortletForm(self.mainIframe[1])
		self.uidriver.waitForElementClickable(BasicListView.searchButton,40)
		deleteDataCheckbox = self.uidriver.findElementInParentElement(self.lineData,self.lineDataCheckbox)
		self.uidriver.clickElementEntity(deleteDataCheckbox)

	def clickNew(self):
		self.switchToCurrentPortletForm(self.mainIframe[1])
		self.uidriver.clickElement(BasicListView.newButton)

	def clickDelete(self):
		self.uidriver.clickElement(BasicListView.deleteButton)




