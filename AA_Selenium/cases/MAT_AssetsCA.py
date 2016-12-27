# -*- coding: utf-8 -*-
from pages.AssetConditionAssessment import *
from CaseTemplate import *


class  MAT_AssetsCA(unittest.TestCase):
	"""
		Asset Condition Assessment Manager Basic Function
	"""
	ratingTypePortlet = "name-ratingType-admin"
	assetCAPortlet = "id-conditionAssessment-admin"
	assetCARef = "id-assetCA"
	
	def setUp(self):
		loginSystem(self)
		self.dashBoard.findPortlet("Asset Condition Assessment")

	def tearDown(self):
		endCase(self)

	def test_TC_AssetCA_001_NewAssetCAInAdmin_MAT(self):
		"""New Asset Condition Assessment Type in Admin"""
		# Access Administration
		self.dashBoard.accessAdmin()
		admin = SetUpPage(self.uidriver)
		msgCreated = "The condition assessment created successfully."
		# Create Asset Condition Assessment
		createAdminData(self,admin,admin.Assets,admin.conditionAssessment,DataList,self.assetCAPortlet,
			AssetCAForm,self.assetCAPortlet,(newAssetCA,),msgCreated)

		form = AssetCAForm(self.uidriver, self.assetCAPortlet)
		# Associated Attribute
		msgAssociateAttribute = "1 attribute(s) added to condition assessment successfully."
		associatedDataByLookUp(self,form,form.Attribute, form.LookUp,form.attributeName,newAttribute, form.Submit,form.listValue,
		 form.Select,form.DeleteOfAttribute, msgAssociateAttribute) #newAttribute
		# Associated  Obbveration Attribute
		associatedDataByLookUp(self,form,form.observAttribute, form.LookUp,form.attributeName,newAttribute, form.Submit,form.listValue,
		 form.Select,form.DeleteOfAttribute, msgAssociateAttribute)#newAttribute


	def test_TC_AssetCA_002_NewRatingTypeInAdmin_MAT(self):
		"""New Rating Type in Admin"""
		# Access Administration
		self.dashBoard.accessAdmin()
		admin = SetUpPage(self.uidriver)
		msgCreated = "The rating type created successfully."
		# Create Rating Type
		createAdminData(self,admin,admin.Assets,admin.ratingType,DataList,self.ratingTypePortlet,
			RatingTypeForm,self.ratingTypePortlet,(newRatingType,newAssetCA,newAttribute),msgCreated)#newAssetCA,newAttribute

	def test_TC_AssetCA_003_NewRefAssetCA_MAT(self):
		msgCreated ="New asset condition assessment created successfully."
		
		dataList = DataList(self.uidriver,self.assetCARef)
		# Click the New button , Access the new Asset CA page 
		dataList.click(dataList.New)

		# Access the detal page , and wait for load over
		detail = AssetCADetail(self.uidriver,self.assetCARef)
		detail.uidriver.waitForElementPresent(detail.Submit,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.Submit),msg="Error:Select condition Assessment page is still loading.")
		# Select the condition assessment
		detail.selectConditionAssessment(newAssetCA)#
		detail.click(detail.Submit)

		detail.uidriver.waitForElementPresent(detail.Reset,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.Reset),msg="Error:Search asset page is still loading.")
		# Search Asset ID
		sleep(2)
		detail.uidriver.setTextToElement(detail.assetID,newAssetID)#
		detail.click(detail.SubmitOfAsset)
		detail.uidriver.waitForElementPresent(detail.SelectOfAsset,30)
		
		detail.selectAssetInList()
		detail.click(detail.SelectOfAsset)
		detail.uidriver.waitForElementPresent(detail.Submit,30)

		# Input data , the click submit
		detail.inputDetailData()
		detail.click(detail.Submit)

		# Save the screen shot
		detail.uidriver.saveScreenshot("..\\report\\image\\Create%s"%(self.assetCARef)+generatNowStr()+".png")
		self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),msgCreated,msg="Error: new %s failed."%self.assetCARef)
		detail.closeEMSE()	

	def test_TC_AssetCA_004_SearchAndUpdateAssetCA_MAT(self):
		"""Search and Update Reference Asset Condition Assessment Record"""
		msgUpdated = "The asset condition assessment updated successfully."
		dataList = AssetCAListView(self.uidriver,self.assetCARef)
		searchAtListView(self,dataList,AssetCAListView.assetID2,newAssetID)#newAssetID
		updateRefData(self,AssetCAListView,AssetCADetail,self.assetCARef,(newAssetID,),msgUpdated,(By.ID,'editSave'))




