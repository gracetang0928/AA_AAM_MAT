from BasePage import *
from public import getDateAfter


class PMDetailElements(object):
	"""
		PM Schedule Detail Page
	"""
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Elements of  PM Schedule detail
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	Detail = (By.ID,"PMScheduleDetail")
	# Information Elements

	scheduleName = (By.ID,"value(scheduleName)")
	startDate = (By.ID,"date(startDate)")
	template = (By.ID,"value(templateID)")
	templateOptions = (By.XPATH,"//option")

	scheduleStatus = (By.ID,"value(scheduleStatus)")
	nextScheduleDate = (By.ID,"date(triggerDate)")

	triggerBy = (By.ID,"value(triggerBy)")
	triggerByOptions = (By.XPATH,'//select[@id="value(triggerBy)"]/option')


	timeIntervalInput = (By.ID,"value(timeInterval)")
	timeIntervalType = (By.ID,"value(timeIntervalType)")
	timeTypeOptions = (By.XPATH,'//select[@id="value(timeIntervalType)"]/option')

	usageIntervalInput = (By.ID,"value(usageInterval)")
	usageIntervalType = (By.ID,"value(usageIntervalType)")
	usageTypeOptons = (By.XPATH,'//select[@id="value(usageIntervalType)"]/option')
	comments = (By.ID,"value(comments)")


	# CheckBox of detai, not all 
	singleWOAllAssets = (By.ID,"value(singleWOFlag)")
	linkAssetAddressToWO = (By.ID,"value(linkAssetAddresses)")

	# Message Panel
	msg = (By.ID,"errorMsgPanel")


# Search and  Other function in the list

class PMListView(BaseListView,PMDetailElements):
	"""
		PM Schedule List View Page
	"""
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Elements of  PM Schedule list view
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	GenerateEnter = (By.ID,"userEnter")

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Generate PM page element
	thoughDate = (By.ID,"date(throughDate)")

	Preview = (By.ID,"preview")
	Generate = (By.ID,"generate")
	Complete = (By.ID,"a_CompleteGeneration")

	def acceptPMAlert(self):
		self.acceptAlert()	
		self.switchToCurrentPortletForm("pmscheduleList")


class PMForm(BaseForm):
	# Tab Elements
	PMDetail = (By.ID,"PMScheduleDetail")

	assetID =(By.ID,"value(g1AssetID)")
	streetNumber = (By.ID,"value(houseNumberStart)")
	
	LinkedAddress = (By.ID,"address")
	SelectOfAddress = (By.ID,"add")

	LinkedAsset = (By.ID,"LinkedAsset")
	SubmitOfAsset = (By.ID,"submit4pmschedule")



##############################################################################################
# Update and new PM form
##############################################################################################
class PMDetail(BaseForm,PMDetailElements):

	def updateDetail(self,commentData):
		self.uidriver.setTextToElement(PMDetail.comments,"Update by auto "+commentData)

	def inputDetailData(self,scheduleNameInfo,woTemplate):
		# Fill In Schedule Name
		self.uidriver.setTextToElement(PMDetail.scheduleName,scheduleNameInfo)
		# Select Template
		self.uidriver.clickElement(PMDetail.template)
		templateSelectors = self.uidriver.findElementsInParentElement(PMDetail.template,PMDetail.templateOptions)
		for select in templateSelectors:
			if select.get_attribute("value")==woTemplate:
				self.uidriver.clickElementEntity(select)
				break
		sleep(1)

		# Fill In Start Date, current date
		self.uidriver.setTextToElement(PMDetail.startDate,scheduleNameInfo[-2:])

		# Select Trigger By
		triggerBySelectors = self.uidriver.findElementsInParentElement(PMDetail.triggerBy,PMDetail.triggerByOptions)
		self.uidriver.clickElementEntity(triggerBySelectors[1])
		sleep(2)


		# Select Time Interval Type and Fill In Time 
		self.uidriver.setTextToElement(PMDetail.timeIntervalInput,scheduleNameInfo[-1])

		sleep(1)
		timeTypeSelectors = self.uidriver.findElementsInParentElement(PMDetail.timeIntervalType,PMDetail.timeTypeOptions)
		self.uidriver.clickElementEntity(timeTypeSelectors[1])
		sleep(1)


		# Select Usage Interval Type and Fill In Usage
		self.uidriver.setTextToElement(PMDetail.usageIntervalInput,scheduleNameInfo[-2:])

		usageTypeSelectors = self.uidriver.findElementsInParentElement(PMDetail.usageIntervalType,PMDetail.usageTypeOptons)
		self.uidriver.clickElementEntity(usageTypeSelectors[1])
		sleep(1)

		# Fill In Next Schedule Date
		self.uidriver.setTextToElement(PMDetail.nextScheduleDate,getDateAfter(1))

		# Check checkbox 
		self.uidriver.clickElement(PMDetail.singleWOAllAssets)
		self.uidriver.clickElement(PMDetail.linkAssetAddressToWO)

		sleep(2)










