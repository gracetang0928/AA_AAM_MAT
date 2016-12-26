# -*- coding: utf-8 -*-
from pages.Administration import DataList,CostGroupForm,CostItemForm,SetUpPage
from pages.LoginPage import *
from pages.public import *
import unittest 
import HTMLTestRunner


class  CostingTest(unittest.TestCase):
	"""Costing Basic Function """

	costGroupPortlet = "name-costGroup-admin"
	costItemPortlet = "name-costItem-admin"


	def setUp(self):
		loginSystem(self)
		self.dashBoard.accessAdmin()
		
	def tearDown(self):
		endCase(self)


	def test_TC_Costing_001_NewCostItemInAdmin_MAT(self):
		"""Create Cost Item In Admin"""
		# Access Set up page , click Costing > Cost Item > New 
		admin = SetUpPage(self.uidriver)
		msgCreated ="The cost item created successfully." 
		# Create Cost Item
		createAdminData(self,admin,admin.Costing,admin.costItem,DataList,self.costItemPortlet,
			CostItemForm,self.costItemPortlet,(newCostItem,),msgCreated)
		form = CostItemForm(self.uidriver, self.costItemPortlet)
		msgAssociateRate = "The cost rate created successfully."
		# Create Cost Rate
		associatedDataByNew(self,form, form.CostRates, form.New,form.inputCostRate,("8","10"), form.Submit, msgAssociateRate)


	def test_TC_Costing_002_NewCostGroupInAdmin_MAT(self):
		"""Create Cost Group In Admin"""
		# Access Set up page , click Costing > Cost Group > New 
		admin = SetUpPage(self.uidriver)
		msgCreated = "The Cost Group created successfully."
		# New Costing Group
		createAdminData(self,admin,admin.Costing,admin.costGroup,DataList,self.costGroupPortlet,
			CostGroupForm,self.costGroupPortlet,(newCostGroup,),msgCreated)

		form = CostGroupForm(self.uidriver, self.costGroupPortlet)
		msgAssociateItem = "1 Cost Item(s) added to Cost Group successfully."
		# Associated Cost Item to Group
		associatedDataByLookUp(self,form, form.CostItem, form.LookUp,form.costItem,"newCostItem", form.SubmitOfItem,form.itemValue,
		 form.SelectOfItem,form.DeleteOfItem, msgAssociateItem) #newCostItem