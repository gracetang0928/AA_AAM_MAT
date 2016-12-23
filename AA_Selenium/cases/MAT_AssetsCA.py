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
	
	def setUp(self):
		loginAndFindPortlet(self)
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