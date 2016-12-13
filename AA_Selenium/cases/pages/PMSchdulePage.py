from BasePage import *

class PMListViewPage(BasicListView):
	"""
		PM Schedule List View Page
	"""
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Elements of  PM Schedule list view
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	generateButton = (By.ID,"userEnter")
	def clickGenerate(self):
		self.switchToCurrentPortletForm(PMListViewPage.mainIframe[1])
		self.uidriver.clickElement(PMListViewPage.generateButton)



class PMDetailElements(object):
	"""
		PM Schedule Detail Page
	"""
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Elements of  PM Schedule detail
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	# Information Elements

	scheduleName = (By.ID,"value(scheduleName)")
	startDate = (By.ID,"date(startDate)")
	template = (By.ID,"value(templateID)")
	scheduleStatus = (By.ID,"value(scheduleStatus)")
	triggerBy = (By.ID,"value(triggerBy)")
	nextScheduleDate = (By.ID,"date(triggerDate)")
	timeIntervalInput = (By.ID,"value(timeInterval)")
	timeIntervalType = (By.ID,"value(timeIntervalType)")
	usageIntervalInput = (By.ID,"value(usageInterval)")
	usageIntervalType = (By.ID,"value(usageIntervalType)")
	comments = (By.ID,"value(comments)")

	# CheckBox of detai, not all 
	singleWOAllAssets = (By.ID,"value(singleWOFlag)")
	linkAssetAddressToWO = (By.ID,"value(linkAssetAddresses)")

	# Buttons on menu
	submitButton = (By.ID,"acsubmit")
	resetButton = (By.ID,"accelareset")

	def clickSubmit(self):
		self.uidriver.clickElement(PMDetailElements.submitButton)
		sleep(1)

	def clickRest(self):
		self.uidriver.clickElement(PMDetailElements.resetButton)



class PMSearchPage(BasePage,PMDetailElements):
	# Elements of search
	mainIframe = (By.ID,"pmscheduleList")	

	def fillInSearchCondition(self,pmName):
		self.switchToCurrentPortletForm(PMSearchPage.mainIframe[1])
		sleep(2)
		self.uidriver.setTextToElement(PMSearchPage.scheduleName,pmName)
		



class PMSchedulDetailPage(BasePage,PMDetailElements):
	# Buttons Elements
	saveButton = (By.ID,"save")



	def clickSave(self):
		self.uidriver.clickElement(PMDetailElements.saveButton)










