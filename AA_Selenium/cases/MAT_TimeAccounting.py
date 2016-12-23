# -*- coding: utf-8 -*-
from pages.LoginPage import *
from pages.Administration import *
from pages.public import *
import unittest 
import HTMLTestRunner

class  TimeAccountingTest(unittest.TestCase):
	"""Time Accounting Function """

	timeGroupPortlet = "name-timeGroup-admin"
	timeTypePortlet = "name-timetype-admin"

	
	def setUp(self):
		loginAndFindPortlet(self)
		self.dashBoard.accessAdmin()
	def tearDown(self):
		endCase(self)

	def test_TC_TimeAccount_001_NewTimeGroupInAdmin_MAT(self):
		""" Create Time Group In Admin"""
		# Access Set up page , click Costing > Cost Group > New 
		admin = SetUpPage(self.uidriver)
		msgCreated = "1 record(s) added successfully."
		createAdminData(self,admin,admin.TimeAccounting,admin.timeGroup,DataList,self.timeGroupPortlet,
			TimeGroupForm,self.timeGroupPortlet,(newTimeGroup,),msgCreated)

	def test_TC_TimeAccount_002_NewTimeTypeInAdmin_MAT(self):
		""" Create Time Type In Admin"""
		# Access Set up page , click Costing > Cost Group > New 
		admin = SetUpPage(self.uidriver)
		msgCreated = "1 record(s) added successfully."
		createAdminData(self,admin,admin.TimeAccounting,admin.timeType,DataList,self.timeTypePortlet,
			TimeTypeForm,self.timeTypePortlet,(newTimeType,newTimeGroup),msgCreated)



if __name__=="__main__":

	caseList = ("test_TC_TimeAccount_001_NewTimeGroupInAdmin_MAT","test_TC_TimeAccount_002_NewTimeTypeInAdmin_MAT")
	#"test_NewAttribute_MAT","test_NewAttributeTable_MAT","test_NewAttributeTemplate_MAT"
	testUnit = unittest.TestSuite()

	for case in caseList:
		testUnit.addTest(TimeAccountingTest(case))

	reportName = '..\\report\\AssetAdmin'+generatNowStr()+'.html'

	fp = file(reportName,'wb')

	runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "Asset Admin MAT Test Results" , description = "Case Execute Results")

	runner.run(testUnit)