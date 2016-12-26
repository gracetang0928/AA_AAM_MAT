# -*- coding: utf-8 -*-
from pages.Administration import DataList,AssetCAForm,RatingTypeForm,SetUpPage
from pages.LoginPage import *
from pages.public import *
from unittest import *
import HTMLTestRunner


class  AssetCATest(unittest.TestCase):
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
		msg ="New asset condition assessment created successfully."
		"The asset condition assessment updated successfully."
		dataList = DataList(self.uidriver,self.assetCARef)
		# Click the New button , Access the new Asset CA page 
		dataList.click(dataList.New)

		# Access the detal page , and wait for load over
		detail = detailClass(self.uidriver,portletName)
		detail.uidriver.waitForElementPresent(detail.Submit,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.Submit),msg="Error: %s detail page is still loading."%portletName)
	 
		# Input data , the click submit
		detail.inputDetailData(*data)
		detail.click(detail.Submit)

		# Save the screen shot
		detail.uidriver.saveScreenshot("..\\report\\image\\Create%s"%(portletName)+generatNowStr()+".png")
		self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),msgCreated,msg="Error: new %s failed."%portletName)

		detail.closeEMSE()	



if __name__=="__main__":
#	unittest.main()
#################################################################################################################################	
	caseList = ("test_NewAsset_MAT","test_SearchAndUpdateAsset_MAT","test_CloneAsset_MAT","test_DeleteAsset_MAT")
 #"test_NewAsset_MAT"m"test_SearchAndUpdateAsset_MAT","test_UpdateAsset_MAT","test_CloneAsset_MAT","test_DeleteAsset_MAT",
	testUnit = unittest.TestSuite()

	for case in caseList:
		testUnit.addTest(AssetCATest(case))

	reportName = '..\\report\\Asset'+generatNowStr()+'.html'

	fp = file(reportName,'wb')

	runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "Asset MAT Test Results" , description = "Case Execute Results")

	runner.run(testUnit)