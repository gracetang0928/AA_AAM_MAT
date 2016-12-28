# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
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
	# Dashboard iframe
	containerFrame = (By.ID,"iframe-page-container")
	# Admin Iframe
	adminFrame = (By.ID,"administration")

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
	
	def closeEMSE(self):
		localhandle = self.uidriver.getCurrentWindowHandle()
		allhandles = self.uidriver.getWindowHandles()
		if (len(allhandles)>1):
			sleep(8)
			for handle in allhandles:
				if handle!=localhandle:
					self.uidriver.switchToWindow(handle)
					break	
			self.uidriver.closeWindow()	
		self.uidriver.switchToWindow(localhandle)
		sleep(3)

	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	#	Every portlet page contain page container iframe , then every page need the method
	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	"""
		Make the uidriver switch to portlet iframe
		- iframeInfo : iframe entity or id of iframe	
	"""

	def switchToCurrentContainer(self,containerInfo):
		self.uidriver.switchToDefaultContent()
		self.uidriver.waitForElementPresent(containerInfo,30)
		# sleep(10)
		self.uidriver.switchToIframe(containerInfo[1])

	def switchToCurrentForm(self,containerInfo,iframeInfo):
		self.switchToCurrentContainer(containerInfo)
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
		self.uidriver.waitForElementPresent(elementInfo,30)
		sleep(1)
		self.uidriver.setTextToElement(elementInfo,streetNumberInfo)



class BaseListView(BasePage,BaseElements):

	firstRecord = (By.ID,"row1")

	lineNO = generatLineNO(2)
	lineData = (By.ID,"row"+lineNO)
	lineDataLink = (By.ID,"linkrow"+lineNO)
	noResult = (By.ID,"popNorecord")
	#portlet like :　＂id-part-admin＂
	def __init__(self,uiDriver,portlet):
		super(BaseListView,self).__init__(uiDriver)
		# Portlet Name end With admin, Current Form is administration
		if portlet.endswith("admin"):
			currentFrame = self.adminFrame		
		else:
			currentFrame = self.containerFrame
		self.frame = portlet.split('-')
		portletTemp =(self.frame[0],self.frame[1]+"List")
		self.lineDataCheckbox = (By.XPATH, '//input[@name="value(chk_%s,%d)"]'%(self.frame[1],int(BaseListView.lineNO)-1))
		self.switchToCurrentForm(currentFrame,portletTemp)

	# Click the link of first record 
	def selectFirstRecordInList(self):
		firstData = self.uidriver.findElementInParentElement((By.ID,"row1"),(By.ID,"linkrow1"))
		self.uidriver.clickElementEntity(firstData)

	# Check the checkbox of first record 
	def checkFirstRecordInList(self):
		firstData = self.uidriver.findElementInParentElement((By.ID,"row1"),(By.XPATH, '//input[@name="value(chk_%s,0)"]'%self.frame[1]))
		self.uidriver.clickElementEntity(firstData)
		
	#Random select a record in the list , then checked the checkbox
	def checkRecordInList(self):
		data = self.uidriver.findElementInParentElement(self.lineData,self.lineDataCheckbox)
		self.uidriver.clickElementEntity(data)



class BaseForm(BasePage,BaseElements):

	def __init__(self,uiDriver,portlet):
		super(BaseForm,self).__init__(uiDriver)
		if portlet.endswith("admin"):
			currentFrame = self.adminFrame		
		else:
			currentFrame = self.containerFrame
		frame = portlet.split('-')
		portletTemp =(frame[0],frame[1]+"Form")
		self.switchToCurrentForm(currentFrame,portletTemp)


	# In Tab page , select record to connect
	def checkRecordInResultList(self,resultPortlet):
		dataCheckbox = self.uidriver.findElementInParentElement((By.ID,"row1"),(By.XPATH,'//input[@property="value(chk_%s,0)"]'%resultPortlet))
		self.uidriver.clickElementEntity(dataCheckbox)

###############################################################################################################################
# Public Method
###############################################################################################################################

# Get Date and Time of now
def generatNowStr():
	nowTime = datetime.datetime.now().strftime("%m%d%H%M%S")
	return nowTime



# Get Date after N days
def getDateAfter(n):
	nowDay = datetime.datetime.now()
	afterDays = nowDay + datetime.timedelta(days =n)
	strf = afterDays.strftime("%m/%d/%Y")
	return strf