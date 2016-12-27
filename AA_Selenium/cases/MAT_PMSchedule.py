# -*- coding: utf-8 -*-
from pages.PMSchdulePage import *
from CaseTemplate import *

class  MAT_PMSchedule(unittest.TestCase):
	"""PM Schedules Basic Function """
	portlet = "id-pmschedule"
	wOTemplatePortlet = "name-woTemplate-admin"

	def setUp(self):
		loginSystem(self)
		self.dashBoard.findPortlet("PM Schedules")
	def tearDown(self):
		endCase(self)


	def test_TC_PM_001_NewWOTemplateInAdmin_MAT(self):
		"""New Work Order Template In Admin """
		# Access Administration
		self.dashBoard.accessAdmin()
		admin = SetUpPage(self.uidriver)
		msgCreated = "The work order template created successfully."
		createAdminData(self,admin,admin.WorkOrders,admin.workOrderTemplate,DataList,self.wOTemplatePortlet,
			WOTemplateForm,self.wOTemplatePortlet,(newWOTemplate,),msgCreated)
		form = WOTemplateForm(self.uidriver, self.wOTemplatePortlet)
		# Associated cost item
		msgAssociateCost = "1 costing(s) added successfully to the work order template."
		associatedDataByLookUp(self,form, form.Costing, form.LookUp,form.costItem,"NCI1130", form.SubmitOfWO,form.costListValue,
		 form.SelectOfWO,form.Delete, msgAssociateCost) #newCostItem
		# Associated part
		msgAssociatePart = "1 Part(s) selected successfully."
		associatedDataByLookUp(self,form, form.Part, form.LookUp,form.partNumber,"NPA234", form.SubmitOfWO,form.partListValue,
		 form.SelectOfWO,form.SaveOfPart, msgAssociatePart) #newCostItem
		# Input part information
		form.inputPartData("3")
		form.click(form.SaveOfPart)
		msgSavePart = "1 Part(s) added to Work Order Template."
		self.assertEquals(form.uidriver.getTextOfElement(form.msg), msgSavePart,msg="Error: Associated Part to WO Template Failed.")


	def test_TC_PM_002_NewPM_MAT(self):
		"""Create New PM Schedules"""
		msgCreated = "The pm schedule created successfully."		
		createRefData(self,PMListView,PMDetail,self.portlet,(newPMName,newWOTemplate),msgCreated)


	def test_TC_PM_003_SearchAndUpdatePM_MAT(self):
		"""Search and Update PM Schedules"""
		msgUpdated = "The pm schedule updated successfully."
		dataList = PMListView(self.uidriver,self.portlet)
		searchAtListView(self,dataList,dataList.scheduleName,newPMName)
		updateRefData(self,PMListView,PMDetail,self.portlet,(newPMName,),msgUpdated)



	def test_TC_PM_004_LinkAssetToPM_MAT(self):
		"""Link Asset To The PM Schedules"""
		msgAssociateAsset = "1 asset(s) added to the PM schedule successfully."
		pmList = PMListView(self.uidriver,self.portlet)
		searchAtListView(self,pmList,pmList.scheduleName,newPMName)
		pmList.selectFirstRecordInList()
		form = PMForm(self.uidriver,self.portlet)
		associatedDataByLookUp(self,form,form.LinkedAsset,form.LookUp,form.assetID,newAssetID,form.SubmitOfAsset,"asset",form.Select,form.Save,msgAssociateAsset)

	def test_TC_PM_005_LinkAddressToPM_MAT(self):
		"""Link Address To the PM Schedules"""
		msgAssociateAddress = "1 selected records added successfully."
		pmList = PMListView(self.uidriver,self.portlet)
		searchAtListView(self,pmList,pmList.scheduleName,newPMName)
		pmList.selectFirstRecordInList()
		form = PMForm(self.uidriver,self.portlet)
		associatedDataByLookUp(self,form,form.LinkedAddress,form.LookUp,form.streetNumber,"2",form.Submit,"RefAddress",form.SelectOfAddress,form.Delete,msgAssociateAddress) 

	# Generate Work Order by PM
	def test_TC_PM_006_GeneratePMRecord_MAT(self):
		pass
#		"""Generate a WO by PM Schedules"""
#		pmList = PMListView(self.uidriver,self.portlet)
#		searchAtListView(self,pmList,pmList.scheduleName,newPMName)
#		pmList.selectFirstRecordInList()

#		pmList.checkFirstRecordInList()
		# Click generate button
#		pmList.click(pmList.GenerateEnter)

		# Wait for page load over
#		pmList.uidriver.waitForElementPresent(pmList.Preview,30)
#		self.assertIsNotNone(pmList.uidriver.findElement(pmList.Previre),"Error: Generate Work Order page did not load.")

		# Input Though Date, click preview
#		pmList.uidriver.setTextToElement(pmList.thoughDate,getDateAfter(3))
#		pmList.click(pmList.Preview)
#		pmList.uidriver.saveScreenshot("..\\report\\image\\PM_Preview"+generatNowStr()+".png")
		
#		pmList.click(pmList.Generate)

#		pmList.acceptPMAlert()
		#		pmList.switchToCurrentPortletForm("pmscheduleList")
#		pmList.uidriver.waitForElementPresent(pmList.Complete,30)
#		self.assertIsNotNone(pmList.uidriver.findElement(pmList.Complete),msg="Error: Can't generate Work Order by this PM.")
#		pmList.uidriver.saveScreenshot("..\\report\\image\\generatePMComplete"+generatNowStr()+".png")

#		pmList.click(pmList.Complete)

	def test_TC_PM_007_DeletePM_MAT(self):
		"""Delete a PM Schedules Record"""
		deleteRefData(self,PMListView,self.portlet,PMForm)
		