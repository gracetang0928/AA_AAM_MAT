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
	newAssetID  = generatNowStr()
	def setUp(self):
		loginAndFindPortlet(self,"Assets")
	def tearDown(self):
		endCase(self)
	def test_NewAsset_MAT(self):

		assetList = AssetsListView(self.uidriver)
		assetList.clickNew()
		assetDetailPage = AssetDetailPage(self.uidriver)
		assetDetailPage.selectAssetDetailTab()

		self.assertIsNotNone(assetDetailPage.uidriver.findElement(assetDetailPage.submitButton),msg = "Error：Asset detail page didn't load. Can't find submit button.")

		assetDetailPage.fillInData(self.newAssetID)
		assetDetailPage.clickSubmit()
		msgText = assetDetailPage.uidriver.getTextOfElement(assetDetailPage.msg)
		assetDetailPage.uidriver.saveScreenshot("..\\report\\image\\createAsset"+generatNowStr()+".png")
		self.assertEquals(msgText,"The Asset created successfully.",msg =  "Error：Create Asset failed.")
		localWindow = self.uidriver.getCurrentWindowHandle()
		assetDetailPage.closeEMSE(localWindow)		

	def test_SearchAsset_MAT(self):		
		assetList = AssetsListView(self.uidriver)
		assetList.clickSearch()
		searchPage = SearchAssetPage(self.uidriver)
		searchPage.fillInSearchCondition(self.newAssetID)
		self.assertIsNotNone(searchPage.uidriver.findElement(searchPage.submitButton),"Error：Asset search page didn't load. Can't find submit button. ")
		searchPage.clickSubmit()
		assetList.uidriver.saveScreenshot("..\\report\\image\\searchAsset"+generatNowStr()+".png")
		self.assertIsNone(assetList.uidriver.findElement(assetList.noResult),"Error：No Results return.")


	def test_CloneAsset_MAT(self):		
		assetList = AssetsListView(self.uidriver)
		assetList.selectRecordsInList()
		assetList.uidriver.waitForElementNotPresent(assetList.searchButton,20)
		assetDetailTab = AssetDetailPage(self.uidriver)
		assetDetailTab.selectAssetDetailTab()

		self.assertIsNotNone(assetDetailTab.uidriver.findElement(assetDetailTab.cloneButton),msg = "Error：Asset detail page didn't load. Can't find clone button.")

		assetDetailTab.clickClone()

		self.assertIsNotNone(assetDetailTab.uidriver.findElement(assetDetailTab.cloneSubmit),msg = "Error：Asset clone page didn't load.Can't find submit button of clone page")

		assetDetailTab.fillInCloneData("AA","2")
		assetDetailTab.clickSubmitOfClone()

		assetDetailTab.uidriver.waitForElementPresent(assetDetailTab.msg,20)
		assetDetailTab.uidriver.saveScreenshot("..\\report\\image\\cloneAsset"+generatNowStr()+".png")
		msgText = assetDetailTab.uidriver.getTextOfElement(assetDetailTab.cloneMsg)

		self.assertTrue((msgText.find("added successfully")>0),msg = "Error：Clone Asset Failed.")

		assetDetailTab.clickComplete()
		assetDetailTab.uidriver.waitForElementNotPresent(assetDetailTab.msg,20)


	def test_UpdateAsset_MAT(self):			
		assetList = AssetsListView(self.uidriver)
		assetList.selectRecordsInList()
		assetList.uidriver.waitForElementNotPresent(assetList.searchButton,40)
		assetDetailTab = AssetDetailPage(self.uidriver)

		assetDetailTab.selectAssetDetailTab()

		self.assertIsNotNone(assetDetailTab.uidriver.findElement(assetDetailTab.saveButton),msg = "Error：Asset detail page didn't load. Can't find clone button.")

		assetDetailTab.fillInUpdateDesc("Test update 12/8")
		assetDetailTab.clickSave()		
		assetDetailTab.uidriver.waitForElementPresent(assetDetailTab.msg,20)

		updateMsg = assetDetailTab.uidriver.getTextOfElement(assetDetailTab.msg)
		assetDetailTab.uidriver.saveScreenshot("..\\report\\image\\updateAsset"+generatNowStr()+".png")
		self.assertEquals(updateMsg,"The Asset updated successfully.",msg = "Error：Update Asset failed.")


	def test_DeleteAsset_MAT(self):
		assetList = AssetsListView(self.uidriver)
		
		# Select a record then click delete		
		assetList.selectRecordsInList()
		assetList.clickDelete()

		deleteMsg = assetList.uidriver.getTextOfElement(assetList.errorMsg)
		deleteMsg.uidriver.saveScreenshot("..\\report\\image\\deleteAsset"+generatNowStr()+".png")
		self.assertEquals(deleteMsg,"1 record(s) deleted successfully.",msg = "Error：Delete asset failed.")





if __name__=="__main__":
#	unittest.main()
#################################################################################################################################	
	caseList = ("test_NewAsset_MAT",\
 "test_SearchAsset_MAT","test_DeleteAsset_MAT","test_UpdateAsset_MAT","test_CloneAsset_MAT")
	testUnit = unittest.TestSuite()

	for case in caseList:
		testUnit.addTest(AssetManageTest(case))

	reportName = '..\\report\\testResult'+generatNowStr()+'.html'

	fp = file(reportName,'wb')

	runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "Asset MAT Test Results" , description = "Case Execute Results")

	runner.run(testUnit)