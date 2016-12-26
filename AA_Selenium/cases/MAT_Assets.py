# -*- coding: utf-8 -*-
from pages.Administration import SetUpPage,DataList,AttributeForm,AttributeTableForm,AttributeTemplateForm
from pages.LoginPage import *
from pages.AssetsPage import *
from pages.public import *
from unittest import *
import HTMLTestRunner


class  AssetManageTest(unittest.TestCase):
	"""
		Asset Manager Basic Function
	"""
	# Ref frame information
	portlet = "id-data"
	# Admin frame information
	attributePortlet = "id-attribute-admin"
	attrTablePortlet = "id-attrTable-admin"
	templatePortlet = "name-template-admin"


	def setUp(self):
		oginSystem(self)
		self.dashBoard.findPortlet("Assets")
	def tearDown(self):
		endCase(self)

	def test_TC_Assets_001_NewAttributeInAdmin_MAT(self):
		"""New Asset Attribute in Admin"""
		self.dashBoard.accessAdmin()
		# Access Set up page , click assets > Attribute > New 
		# Create new Attribute
		admin = SetUpPage(self.uidriver)
		msg = "The attribute created successfully."
		createAdminData(self,admin,admin.Assets,admin.attribute,DataList,self.attributePortlet,
			AttributeForm,self.attributePortlet,("Number",newAttribute),msg)

	def test_TC_Assets_002_NewAttributeTableInAdmin_MAT(self):
		"""New Asset Attribute Table in Admin"""
		self.dashBoard.accessAdmin()
		# Access Set up page , click assets > Attribute Table > New 
		# Create new Attribute Table
		admin = SetUpPage(self.uidriver)
		msgCreated = "The Attribute Table created successfully."
		createAdminData(self,admin,admin.Assets,admin.attributeTable,DataList,self.attrTablePortlet,
			AttributeTableForm,self.attrTablePortlet,(newAttributeTable,),msgCreated)

		form = AttributeTableForm(self.uidriver,self.attrTablePortlet)
		msgAssociate = "1 record(s) selected successfully."
		associatedDataByLookUp(self,form,form.Attributes,form.LookUp,form.attributeLabel,newAttribute,form.Submit,"attrDef",form.SelectOfAttribute,form.LookUp,msgAssociate) #newAttribute

	def test_TC_Assets_003_NewAttributeTemplateInAdmin_MAT(self):
		"""New Asset Attribute Template in Admin"""
		self.dashBoard.accessAdmin()
		# Access Set up page , click assets > Attribute Template > New 
		admin = SetUpPage(self.uidriver)
		msgCreated = "The template created successfully."
		createAdminData(self,admin,admin.Assets,admin.attributeTemplate,DataList,self.templatePortlet,
			AttributeTemplateForm,self.templatePortlet,(newAttributeTemplate,),msgCreated)

		form = AttributeTemplateForm(self.uidriver,self.templatePortlet)
		# Associated Attribute to Template
		msgAssociateAttr = "1 attribute(s) added to template successfully."
		associatedDataByLookUp(self,form,form.Attributes,form.LookUp,form.attributeLabel,newAttribute,form.SubmitOfAttr,"attrDef",form.Select,form.New,msgAssociateAttr) #newAttribute

		# Associated Attribute Table to Template
		msgAssociateTable = "1 record(s) selected successfully."
		associatedDataByLookUp(self,form,form.AttributeTables,form.LookUp,form.attributeTableName,newAttributeTable,form.SubmitOfAttrTable,"AttrTable",form.Select,form.Delete,msgAssociateTable) #newAttributeTable

	
	def test_TC_Assets_004_NewAsset_MAT(self):
		"""New Reference Assets Record"""
		msgCreated = "The Asset created successfully."		
		createRefData(self,AssetsListView,AssetsDetail,self.portlet,(newAssetID,),msgCreated)
	

	def test_TC_Assets_005_SearchAndUpdateAsset_MAT(self):
		"""Search and Update Reference Assets Record"""
		msgUpdated = "The Asset updated successfully."
		dataList = AssetsListView(self.uidriver,self.portlet)
		searchAtListView(self,dataList,dataList.assetID,newAssetID)
		updateRefData(self,AssetsListView,AssetsDetail,self.portlet,(newAssetID,),msgUpdated)


	
	def test_TC_Assets_006_CloneAsset_MAT(self):	
		"""Clone Reference Asset""" 
		dataList = AssetsListView(self.uidriver,self.portlet)
		searchAtListView(self,dataList,dataList.assetID,newAssetID)
		
		dataList.selectFirstRecordInList()

		# Wait for load over
		detail = AssetsDetail(self.uidriver,self.portlet)
		detail.uidriver.waitForElementPresent(detail.Detail,30)
		self.assertIsNotNone(detail.uidriver.findElement(detail.Detail),msg="Error：Asset detail page didn't load. ")

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


	def test_TC_Assets_007_DeleteAsset_MAT(self):
		"""Delete Asset In The List View """
		deleteRefData(self,AssetsListView,self.portlet,AssetForm)



if __name__=="__main__":
#	unittest.main()
#################################################################################################################################	
	caseList = ("test_TC_Assets_004_NewAsset_MAT",)
 #"test_NewAsset_MAT"m"test_SearchAndUpdateAsset_MAT","test_UpdateAsset_MAT","test_CloneAsset_MAT","test_DeleteAsset_MAT",
	testUnit = unittest.TestSuite()

	for case in caseList:
		testUnit.addTest(AssetManageTest(case))

	reportName = '..\\report\\Asset'+generatNowStr()+'.html'

	fp = file(reportName,'wb')

	runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "Asset MAT Test Results" , description = "Case Execute Results")

	runner.run(testUnit)