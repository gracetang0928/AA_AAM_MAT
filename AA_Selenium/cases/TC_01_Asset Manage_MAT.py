# -*- coding: utf-8 -*-

from pages.LoginPage import *
from pages.AssetPage import *
from pages.public import *
from unittest import *
import HTMLTestRunner


class  AssetManageTest(unittest.TestCase):
	"""
		Asset Manager Basic Function
	"""

	portlet = "data"
	def setUp(self):
		loginAndFindPortlet(self,"Assets")
	def tearDown(self):
		endCase(self)

	def searchAsset(self,assetIDInfo):

		# Find the created PM record
		aList = AssetsListView(self.uidriver,self.portlet)
		aList.click(aList.Search)

		# Wait the search page and Asset the page is loaded
		aList.uidriver.waitForElementPresent(aList.assetID,30)
		self.assertIsNotNone(aList.uidriver.findElement(aList.assetID),msg="Error：Asset search page did not load.")

		# input the search condition , the click submit
		aList.inputSearchCondition(aList.assetID,assetIDInfo)
		aList.click(aList.Submit)

		# Check the result 
		self.assertIsNotNone(aList.uidriver.findElement(aList.firstRecord),"Error：No result return　when search PM. ")

		# Click the link of PM record 

	def test_NewAsset_MAT(self):
		# Click the New button , Access the new asset page 
		aList = AssetsListView(self.uidriver,self.portlet)
		aList.click(aList.New)

		
		# Access the detail page , and wait for load over
		detail = AssetDetailPage(self.uidriver,self.portlet)
		detail.uidriver.waitForElementPresent(detail.Submit,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.Submit),msg="Error：Asset detail page didn't load.")

		# Input data , the click submit
		detail.inputDetailData(newAssetID)
		detail.click(detail.Submit)

		# Save the screen shot
		detail.uidriver.saveScreenshot("..\\report\\image\\CreateAsset"+generatNowStr()+".png")
		self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),"The Asset created successfully.",msg="Error: New Asset failed.")

		# if pop up EMSE window , close ot
		localWindow = self.uidriver.getCurrentWindowHandle()
		detail.closeEMSE(localWindow)		

	def test_SearchAndUpdateAsset_MAT(self):

		# Find the new Asset
		self.searchAsset(newAssetID)#newAssetID

		# Access the detail page
		aList = AssetsListView(self.uidriver,self.portlet)
		aList.selectFirstRecordInList()

		# Wait for load over
		detail = AssetDetailPage(self.uidriver,self.portlet)
		detail.uidriver.waitForElementPresent(detail.AssetDetail,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.AssetDetail),msg="Error: Update Asset page is still loading.")

		# Input the comment, Save
		detail.inputDesc(newAssetID)
		detail.click(detail.Save)

		# Save the screen shot
		detail.uidriver.saveScreenshot("..\\report\\image\\Asset-Update"+generatNowStr()+".png")
		self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),"The Asset updated successfully.",msg="Error: Update Asset failed.")


		
	def test_CloneAsset_MAT(self):	
		# Find the new Asset
		self.searchAsset(newAssetID)

		# Access the detail page
		aList = AssetsListView(self.uidriver,self.portlet)
		aList.selectFirstRecordInList()

		# Wait for load over
		detail = AssetDetailPage(self.uidriver,self.portlet)
		detail.uidriver.waitForElementPresent(detail.AssetDetail,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.AssetDetail),msg="Error：Asset detail page didn't load. ")

		# Click Clone
		detail.click(detail.Clone)
		self.assertIsNotNone(detail.uidriver.findElement(detail.SubmitOfClone),msg = "Error：Asset clone page didn't load.")

		# Input clone data
		detail.inputCloneData("S","2")
		detail.click(detail.SubmitOfClone)

		# Waite for clone infomation page
		detail.uidriver.waitForElementPresent(detail.Complete,20)
		self.assertIsNotNone(detail.uidriver.findElement(detail.Complete),msg = "Error：Asset clone page didn't load.")

		detail.uidriver.saveScreenshot("..\\report\\image\\CloneAsset"+generatNowStr()+".png")
		self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),"2 record(s) added successfully.",msg="Error:Clone Asset failed.")

		detail.click(detail.Complete)


	def test_DeleteAsset_MAT(self):
		aList = AssetsListView(self.uidriver,self.portlet)
		aList.checkAssetRecord(1)
		form = AssetFormPage(self.uidriver,self.portlet)
		form.click(form.backArrow)
		aList.switchToCurrentPortletForm("dataList")
		aList.uidriver.waitForElementPresent(aList.Delete,20)
		aList.click(aList.Delete)
		aList.uidriver.saveScreenshot("..\\report\\image\\DeleteAsset"+generatNowStr()+".png")
		deleteMsg = aList.uidriver.getTextOfElement(aList.msg)
		self.assertEquals(deleteMsg,"1 record(s) deleted successfully.",msg = "Error: Delete asset failed. " +deleteMsg)





if __name__=="__main__":
#	unittest.main()
#################################################################################################################################	
	caseList = ("test_NewAsset_MAT","test_SearchAndUpdateAsset_MAT","test_CloneAsset_MAT","test_DeleteAsset_MAT")
 #"test_NewAsset_MAT"m"test_SearchAndUpdateAsset_MAT","test_UpdateAsset_MAT","test_CloneAsset_MAT","test_DeleteAsset_MAT",
	testUnit = unittest.TestSuite()

	for case in caseList:
		testUnit.addTest(AssetManageTest(case))

	reportName = '..\\report\\Asset'+generatNowStr()+'.html'

	fp = file(reportName,'wb')

	runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "Asset MAT Test Results" , description = "Case Execute Results")

	runner.run(testUnit)