# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import time
import datetime

############################################################################
# Public Function
############################################################################



# Random select a record to update or delete
def generatLineNO(numberInfo):
	num = int(datetime.datetime.now().strftime("%d%H%M%S"))
	lineNO = str(num%numberInfo+1)
	return lineNO


############################################################################
# Every page has this iframe element
############################################################################

class BaseElements(object):
	# List view element
	Search = (By.ID,"a_search")
	New = (By.ID,"a_new")
	Delete = (By.ID,"delete")

	# Search and detail page element
	Submit = (By.ID,"acsubmit")
	Reset = (By.ID,"accelareset")

	# Detail page element
	Save = (By.ID,"save")

	LookUp = (By.ID,"a_lookup")
	Select = (By.ID,"select")

	# Message Panel
	msg = (By.ID,"errorMsgPanel")

	backArrow = (By.CSS_SELECTOR,".arrow-back")

	
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


	# Click Button or tab
	def click(self,buttonInfo):
		tab = self.uidriver.waitForElementClickable(buttonInfo,40)
		self.uidriver.clickElementEntity(tab)

	def acceptAlert(self):
		self.uidriver.acceptAlert()
		self.uidriver.switchToDefaultContent()

	def inputSearchCondition(self,elementInfo,streetNumberInfo):
		self.uidriver.setTextToElement(elementInfo,streetNumberInfo)



class BaseListView(BasePage,BaseElements):

	firstRecord = (By.ID,"row1")

	lineNO = generatLineNO(2)
	lineData = (By.ID,"row"+lineNO)
	lineDataLink = (By.ID,"linkrow"+lineNO)
	noResult = (By.ID,"popNorecord")

	def __init__(self,uiDriver,portlet):
		super(BaseListView,self).__init__(uiDriver)
		self.portlet = portlet
		self.mainIframe = (By.ID,portlet+"List")
		self.lineDataCheckbox = (By.XPATH, '//input[@name="value(chk_%s,%d)"]'%(portlet,int(BaseListView.lineNO)-1))
		self.switchToCurrentPortletForm(self.mainIframe[1])

	# Click the link of first record 
	def selectFirstRecordInList(self):
		firstData = self.uidriver.findElementInParentElement((By.ID,"row1"),(By.ID,"linkrow1"))
		self.uidriver.clickElementEntity(firstData)

	# Check the checkbox of first record 
	def checkFirstRecordInList(self):
		firstData = self.uidriver.findElementInParentElement((By.ID,"row1"),(By.XPATH, '//input[@name="value(chk_%s,0)"]'%self.portlet))
		self.uidriver.clickElementEntity(firstData)

	
	
	#Random select a record in the list , then checked the checkbox
	def checkRecordInList(self):
		data = self.uidriver.findElementInParentElement(self.lineData,self.lineDataCheckbox)
		self.uidriver.clickElementEntity(data)

class BaseFormPage(BasePage,BaseElements):

	def __init__(self,uiDriver,portlet):
		super(BaseFormPage,self).__init__(uiDriver)
		self.mainIframe = (By.ID,portlet+"Form")
		self.switchToCurrentPortletForm(self.mainIframe[1])

	# In Tab page , select record to connect
	def checkRecordInResultList(self,resultPortlet):
		dataCheckbox = self.uidriver.findElementInParentElement((By.ID,"row1"),(By.XPATH,'//input[@property="value(chk_%s,0)"]'%resultPortlet))
		self.uidriver.clickElementEntity(dataCheckbox)

