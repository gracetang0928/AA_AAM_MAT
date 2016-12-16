# -*- coding: utf-8 -*-
from pages.LoginPage import *
from pages.Part import *
from pages.public import *
import unittest 
import HTMLTestRunner

class  PartTest(unittest.TestCase):
	"""PM Schedules Basic Function """
	newPMName  = generatNowStr()
	portlet = "part"

	def setUp(self):
		loginAndFindPortlet(self,"Part Inventory")
	def tearDown(self):
		endCase(self)

	def searchPart(self,partName):
		# Find the created PM record
		paList = PartListViewPage(self.uidriver,self.portlet)
		paList.click(paList.Search)

		# Wait the search page and Asset the page is loaded
		paList.uidriver.waitForElementPresent(paList.partNumber,30)
		self.assertIsNotNone(paList.uidriver.findElement(paList.partNumber),msg="Error：part page did not load.")

		# input the search condition , the click submit
		paList.inputSearchCondition(paList.partNumber,partName)
		paList.click(paList.Submit)

		# Check the result 
		self.assertIsNotNone(paList.uidriver.findElement(paList.firstRecord),"Error：No result return　when search part. ")

		# Click the link of PM record 
	
	

	def test_NewPart_MAT(self):
		# Click the New button , Access the new PM page 
		paList = PartListViewPage(self.uidriver,self.portlet)
		paList.click(paList.New)

		# Access the detal page , and wait for load over
		detail = PartDetailPage(self.uidriver,self.portlet)
		detail.uidriver.waitForElementPresent(detail.Submit,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.Submit),msg="Error: New Part page is still loading.")

		# Input data , the click submit
		detail.inputDetailData(newPartID)
		detail.click(detail.Submit)

		# Save the screen shot
		detail.uidriver.saveScreenshot("..\\report\\image\\CreatePart"+generatNowStr()+".png")
		self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),"The part created successfully.",msg="Error: New part failed.")


	def test_SearchAndUpdatePart_MAT(self):
		# Find the new PM record
		self.searchPart(newPartID)

		# Access the detail page
		paList = PartListViewPage(self.uidriver,self.portlet)
		paList.selectFirstRecordInList()

		# Wait for load over
		detail = PartDetailPage(self.uidriver,self.portlet)
		detail.uidriver.waitForElementPresent(detail.partDetail,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.partDetail),msg="Error: Update part page is still loading.")

		# Input the comment, Save
		detail.inputComment(newPartID)
		detail.click(detail.Save)

		# Save the screen shot
		detail.uidriver.saveScreenshot("..\\report\\image\\Part-Update"+generatNowStr()+".png")
		self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),"The part updated successfully.",msg="Error: Update part failed.")



	def test_ReceiveToPartTransaction_MAT(self):
		self.searchPart(newPartID)

		# Access the detail page
		paList = PartListViewPage(self.uidriver,self.portlet)
		paList.selectFirstRecordInList()


		# Click the Link Asset Tab after page load over
		form = PMFormPage(self.uidriver,self.portlet)
		form.uidriver.waitForElementPresent(form.PartTransaction,30)
		form.click(form.PartTransaction)
		form.uidriver.waitForElementPresent(form.New,30)

		# Look up Asset
		form.click(form.New)
		form.uidriver.waitForElementPresent(form.Calculate,30)
		self.assertIsNotNone(form.uidriver.findElement(form.Calculate),msg="Error: search Part page did not load..")
		# Input asset ID ,click submit
		form.inputSearchCondition(form.assetID,"1207124710")#newAssetID
		form.click(form.SubmitOfAsset)
		# Wait for the search result
		form.uidriver.waitForElementPresent(form.Select,30)
		self.assertIsNotNone(form.uidriver.findElement(form.Select),msg="Error: search Part result page did not load..")
		# Select the first record
		form.checkRecordInResultList("asset")

		form.click(form.Select)
		form.uidriver.waitForElementPresent(form.Save,30)
		form.uidriver.saveScreenshot("..\\report\\image\\linkAssetToPM"+generatNowStr()+".png")
		self.assertEquals(form.uidriver.getTextOfElement(form.msg),"1 asset(s) added to the PM schedule successfully.",msg="Error: Link Asset to PM failed.")

	def test_IssueToPartTransaction_MAT(self):
		# Find the new PM record
		self.searchPart(newPMName)

		# Access the detail page
		paList = PartListViewPage(self.uidriver,self.portlet)
		paList.selectFirstRecordInList()


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
	def test_TransferToPartTransaction_MAT(self):
		# Find the new PM record
		self.searchPart(newPMName)

		# Check the checkbox of first record
		paList = PartListViewPage(self.uidriver,self.portlet)
		paList.checkFirstRecordInList()
		# Click generate button
		paList.click(paList.GenerateEnter)

		# Wait for page load over
		paList.uidriver.waitForElementPresent(paList.Preview,30)
		self.assertIsNotNone(paList.uidriver.findElement(paList.Previre),"Error: Generate Work Order page did not load.")

		# Input Though Date, click preview
		paList.uidriver.setTextToElement(paList.thoughDate,getDateAfter(3))
		paList.click(paList.Preview)
		paList.uidriver.saveScreenshot("..\\report\\image\\PM_Preview"+generatNowStr()+".png")
		
		paList.click(paList.Generate)

		paList.acceptPMAlert()
#		paList.switchToCurrentPortletForm("pmscheduleList")
		paList.uidriver.waitForElementPresent(paList.Complete,30)
		self.assertIsNotNone(paList.uidriver.findElement(paList.Complete),msg="Error: Can't generate Work Order by this PM.")
		paList.uidriver.saveScreenshot("..\\report\\image\\generatePMComplete"+generatNowStr()+".png")

		paList.click(paList.Complete)

	def test_DeletePart_MAT(self):
		aList = PartListViewPage(self.uidriver,self.portlet)
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


	caseList = ("test_NewPart_MAT","test_SearchAndUpdatePart_MAT")
	#"test_NewPart_MAT",","test_SearchAndUpdatePart_MAT",,"test_ReceiveToPartTransaction_MAT",,"test_GeneratePMRecord_MAT","test_NewPM_MAT","test_DeletePM_MAT"
	testUnit = unittest.TestSuite()

	for case in caseList:
		testUnit.addTest(PartTest(case))

	reportName = '..\\report\\Part'+generatNowStr()+'.html'

	fp = file(reportName,'wb')

	runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "Part MAT Test Results" , description = "Case Execute Results")

	runner.run(testUnit)