# -*- coding: utf-8 -*-
from pages.Administration import PartLocationForm,DataList,SetUpPage
from pages.LoginPage import *
from pages.Part import *
from pages.public import *
import unittest 
import HTMLTestRunner

class  PartTest(unittest.TestCase):
	"""Part Inventory Basic Function """
	portlet = "id-part"
	partLocationPortlet = "id-partLocation-admin"

	def setUp(self):
		loginAndFindPortlet(self)
		
		
	def tearDown(self):
		endCase(self)

	def test_TC_Part_001_NewPartLocationInAdmin_MAT(self):
		""" Create New Part Location in Administration"""
		self.dashBoard.accessAdmin()
		admin = SetUpPage(self.uidriver)
		msgCreated = "The part location created successfully."
		createAdminData(self,admin,admin.Part,admin.partLocation,DataList,self.partLocationPortlet,
			PartLocationForm,self.partLocationPortlet,(newPartLocation,),msgCreated)


	def test_TC_Part_002_NewPart_MAT(self):
		""" New Reference Part """
		self.dashBoard.findPortlet("Part Inventory")
		msgCreated = "The part created successfully."		
		createRefData(self,PartListView,PartDetail,self.portlet,(newPartID,),msgCreated)


	def test_TC_Part_003_SearchAndUpdatePart_MAT(self):
		""" Search and Update Part Record"""
		self.dashBoard.findPortlet("Part Inventory")
		msgUpdated = "The part updated successfully."
		dataList = PartListView(self.uidriver,self.portlet)
		searchAtListView(self,dataList,dataList.partNumber,newPartID)
		updateRefData(self,PartListView,PartDetail,self.portlet,(newPartID,),msgUpdated)


	def addPartTransaction(self,transactionType,quantityInfo):
		self.dashBoard.findPortlet("Part Inventory")
		dataList = PartListView(self.uidriver,self.portlet)
		searchAtListView(self,dataList,dataList.partNumber,"NPA234")#newPartID
		dataList = PartListView(self.uidriver,self.portlet)
		dataList.selectFirstRecordInList()
		form = PartForm(self.uidriver,self.portlet)
		msgPrompt = "The Part Transaction created successfully."
		associatedDataByNew(self,form,form.PartTransaction,form.New,form.inputTransactionData,(transactionType,quantityInfo),form.submitOfTransaction,msgPrompt)
	 

	def test_TC_Part_004_ReceiveToPartTransaction_MAT(self):
		"""Receive Part to Inventory"""
		self.addPartTransaction("RECEIVE","50")


	def test_TC_Part_005_IssueToPartTransaction_MAT(self):
		"""Issue Part"""
		self.addPartTransaction("ISSUE","10")


	def test_TC_Part_006_TransferToPartTransaction_MAT(self):
		"""Transfer Part From a Location to Another Location"""
		self.addPartTransaction("TRANSFER","10")


	def test_TC_Part_007_CheckSupply_MAT(self):
		"""Check the Supply Of the Part"""
		self.dashBoard.findPortlet("Part Inventory")
		# Search the Part and access the form
		dataList = PartListView(self.uidriver,self.portlet)
		searchAtListView(self,dataList,dataList.partNumber,newPartID)
		dataList = PartListView(self.uidriver,self.portlet)
		dataList.selectFirstRecordInList()

		# Click the Link Asset Tab after page load over
		form = PartForm(self.uidriver,self.portlet)
		form.uidriver.waitForElementPresent(form.PartSupply,30)
		form.click(form.PartSupply)
		form.uidriver.waitForElementPresent(form.table,30)

		form.uidriver.saveScreenshot("..\\report\\image\\Part-Supply"+ generatNowStr()+".png")
		self.assertEquals(form.uidriver.getTextOfElement(form.msg),"The Part Transaction created successfully.",msg="Error: Add part transaction failed.")
		
	def test_TC_Part_008_DeletaPart_MAT(self):
		"""Delete a Part From Inventory"""
		self.dashBoard.findPortlet("Part Inventory")
		deleteRefData(self,PartListView,self.portlet,PartForm)

		