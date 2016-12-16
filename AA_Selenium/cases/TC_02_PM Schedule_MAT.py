# -*- coding: utf-8 -*-
from pages.LoginPage import *
from pages.PMSchdulePage import *
from pages.public import *
import unittest 
import HTMLTestRunner

class  PMScheduleTest(unittest.TestCase):
	"""PM Schedules Basic Function """
	newPMName  = generatNowStr()
	portlet = "pmschedule"

	def setUp(self):
		loginAndFindPortlet(self,"PM Schedules")
	def tearDown(self):
		endCase(self)

	def searchAndAccessPM(self,PMname):
		# Find the created PM record
		pmList = PMListViewPage(self.uidriver,self.portlet)
		pmList.click(pmList.Search)

		# Wait the search page and Asset the page is loaded
		pmList.uidriver.waitForElementPresent(pmList.scheduleName,30)
		self.assertIsNotNone(pmList.uidriver.findElement(pmList.scheduleName),msg="Error：PM search page did not load.")
		sleep(3)
		# input the search condition , the click submit
		pmList.inputSearchCondition(pmList.scheduleName,PMname)
		pmList.click(pmList.Submit)

		# Check the result 
		self.assertIsNotNone(pmList.uidriver.findElement(pmList.firstRecord),"Error：No result return　when search PM. ")

		# Click the link of PM record 
	
	

	def test_NewPM_MAT(self):
		# Click the New button , Access the new PM page 
		pmList = PMListViewPage(self.uidriver,self.portlet)
		pmList.click(pmList.New)

		# Access the detal page , and wait for load over
		detail = PMDetailPage(self.uidriver,self.portlet)
		detail.uidriver.waitForElementPresent(detail.Submit,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.Submit),msg="Error: New PM Schedule page is still loading.")

		# Input data , the click submit
		detail.inputDetailData(newPMName)
		detail.click(detail.Submit)

		# Save the screen shot
		detail.uidriver.saveScreenshot("..\\report\\image\\CreatePM"+generatNowStr()+".png")
		self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),"The pm schedule created successfully.",msg="Error: New PM Schedule failed.")


	def test_SearchAndUpdatePM_MAT(self):
		# Find the new PM record
		self.searchAndAccessPM(newPMName)

		# Access the detail page
		pmList = PMListViewPage(self.uidriver,self.portlet)
		pmList.selectFirstRecordInList()

		# Wait for load over
		detail = PMDetailPage(self.uidriver,self.portlet)
		detail.uidriver.waitForElementPresent(detail.PMDetail,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.PMDetail),msg="Error: Update PM Schedule page is still loading.")

		# Input the comment, Save
		detail.inputComment(self.newPMName)
		detail.click(detail.Save)

		# Save the screen shot
		detail.uidriver.saveScreenshot("..\\report\\image\\PM-Update"+generatNowStr()+".png")
		self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),"The pm schedule updated successfully.",msg="Error: Update PM Schedule failed.")



	def test_LinkAssetToPM_MAT(self):
		# Find the new PM record
		self.searchAndAccessPM(newPMName)

		# Access the detail page
		pmList = PMListViewPage(self.uidriver,self.portlet)
		pmList.selectFirstRecordInList()


		# Click the Link Asset Tab after page load over
		form = PMFormPage(self.uidriver,self.portlet)
		form.uidriver.waitForElementPresent(form.LinkedAsset,30)
		form.click(form.LinkedAsset)
		form.uidriver.waitForElementPresent(form.LookUp,30)

		# Look up Asset
		form.click(form.LookUp)
		form.uidriver.waitForElementPresent(form.assetID,30)
		self.assertIsNotNone(form.uidriver.findElement(form.assetID),msg="Error: search Asset page did not load..")
		# Input asset ID ,click submit
		form.inputSearchCondition(form.assetID,newAssetID)#newAssetID
		form.click(form.SubmitOfAsset)
		# Wait for the search result
		form.uidriver.waitForElementPresent(form.Select,30)
		self.assertIsNotNone(form.uidriver.findElement(form.Select),msg="Error: search Asset  result page did not load..")
		# Select the first record
		form.checkRecordInResultList("asset")

		form.click(form.Select)
		form.uidriver.waitForElementPresent(form.Save,30)
		form.uidriver.saveScreenshot("..\\report\\image\\linkAssetToPM"+generatNowStr()+".png")
		self.assertEquals(form.uidriver.getTextOfElement(form.msg),"1 asset(s) added to the PM schedule successfully.",msg="Error: Link Asset to PM failed.")

	def test_LinkAddressToPM_MAT(self):
		# Find the new PM record
		self.searchAndAccessPM(newPMName)

		# Access the detail page
		pmList = PMListViewPage(self.uidriver,self.portlet)
		pmList.selectFirstRecordInList()


		# Click the Link Asset Tab after page load over
		form = PMFormPage(self.uidriver,self.portlet)
		form.uidriver.waitForElementPresent(form.LinkedAddress,30)
		form.click(form.LinkedAddress)
		form.uidriver.waitForElementPresent(form.LookUp,30)

		# Look up Asset
		form.click(form.LookUp)
		form.uidriver.waitForElementPresent(form.streetNumber,30)
		self.assertIsNotNone(form.uidriver.findElement(form.streetNumber),msg="Error: search address page did not load..")
		# Input asset ID ,click submit
		form.inputSearchCondition(form.streetNumber,"2")
		form.click(form.Submit)
		# Wait for the search result
		form.uidriver.waitForElementPresent(form.SelectOfAddress,30)
		self.assertIsNotNone(form.uidriver.findElement(form.SelectOfAddress),msg="Error: search address  result page did not load..")
		# Select the first record
		form.checkRecordInResultList("RefAddress")

		form.click(form.SelectOfAddress)
		form.uidriver.waitForElementPresent(form.Delete,30)
		form.uidriver.saveScreenshot("..\\report\\image\\linkAddressToPM"+generatNowStr()+".png")
		self.assertEquals(form.uidriver.getTextOfElement(form.msg),"1 selected records added successfully.",msg="Error: Link Address to PM failed.")

	# Generate Work Order by PM
	def test_GeneratePMRecord_MAT(self):
		# Find the new PM record
		self.searchAndAccessPM(newPMName)

		# Check the checkbox of first record
		pmList = PMListViewPage(self.uidriver,self.portlet)
		pmList.checkFirstRecordInList()
		# Click generate button
		pmList.click(pmList.GenerateEnter)

		# Wait for page load over
		pmList.uidriver.waitForElementPresent(pmList.Preview,30)
		self.assertIsNotNone(pmList.uidriver.findElement(pmList.Previre),"Error: Generate Work Order page did not load.")

		# Input Though Date, click preview
		pmList.uidriver.setTextToElement(pmList.thoughDate,getDateAfter(3))
		pmList.click(pmList.Preview)
		pmList.uidriver.saveScreenshot("..\\report\\image\\PM_Preview"+generatNowStr()+".png")
		
		pmList.click(pmList.Generate)

		pmList.acceptPMAlert()
#		pmList.switchToCurrentPortletForm("pmscheduleList")
		pmList.uidriver.waitForElementPresent(pmList.Complete,30)
		self.assertIsNotNone(pmList.uidriver.findElement(pmList.Complete),msg="Error: Can't generate Work Order by this PM.")
		pmList.uidriver.saveScreenshot("..\\report\\image\\generatePMComplete"+generatNowStr()+".png")

		pmList.click(pmList.Complete)

	def test_DeletePM_MAT(self):
		aList = PMListViewPage(self.uidriver,self.portlet)
		aList.checkFirstRecordInList()
		form = PMFormPage(self.uidriver,self.portlet)
		form.click(form.backArrow)
		aList.switchToCurrentPortletForm(self.portlet+"List")
		aList.uidriver.waitForElementPresent(aList.Delete,20)
		aList.click(aList.Delete)
		aList.uidriver.saveScreenshot("..\\report\\image\\DeletePM"+generatNowStr()+".png")
		deleteMsg = aList.uidriver.getTextOfElement(aList.msg)
		self.assertEquals(deleteMsg,"1 record(s) deleted successfully.",msg = "Error: Delete asset failed. " +deleteMsg)

		
if __name__=="__main__":


	caseList = ("test_NewPM_MAT","test_SearchAndUpdatePM_MAT","test_LinkAssetToPM_MAT","test_LinkAddressToPM_MAT","test_DeletePM_MAT",)
	#"test_SearchAndUpdatePM_MAT","test_LinkAssetToPM_MAT","test_LinkAddressToPM_MAT","test_GeneratePMRecord_MAT",,"test_DeletePM_MAT"
	testUnit = unittest.TestSuite()

	for case in caseList:
		testUnit.addTest(PMScheduleTest(case))

	reportName = '..\\report\\PM'+generatNowStr()+'.html'

	fp = file(reportName,'wb')

	runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "PM Schedule MAT Test Results" , description = "Case Execute Results")

	runner.run(testUnit)