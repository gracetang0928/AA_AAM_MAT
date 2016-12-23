# -*- coding: utf-8 -*-
from pages.LoginPage import *
from pages.Administration import *
from pages.public import *
import unittest 
import HTMLTestRunner

class  AdminTest(unittest.TestCase):
	"""Administration Function """

	timeGroupPortlet = "name-timeGroup-admin"
	timeTypePortlet = "name-timetype-admin"

	
	def setUp(self):
		loginAndFindPortlet(self)
		self.dashBoard.accessAdmin()
	def tearDown(self):
		endCase(self)


	def test_TC_Admin_006_NewTimeType_MAT(self):
		""" Create Time Type In Admin"""
		# Access Set up page , click Costing > Cost Group > New 
		admin = SetUpPage(self.uidriver)
		msgCreated = "1 record(s) added successfully."
		createAdminData(self,admin,admin.TimeAccounting,admin.timeType,DataList,self.timeTypePortlet,
			TimeTypeForm,self.timeTypePortlet,(newTimeType,"grace"),msgCreated)


	def test_TC_Admin_007_NewTimeGroup_MAT(self):
		""" Create Time Group In Admin"""
		# Access Set up page , click Costing > Cost Group > New 
		admin = SetUpPage(self.uidriver)
		msgCreated = "1 record(s) added successfully."
		createAdminData(self,admin,admin.TimeAccounting,admin.timeGroup,DataList,self.timeGroupPortlet,
			TimeGroupForm,self.timeGroupPortlet,(newTimeGroup,),msgCreated)


if __name__=="__main__":

	caseList = ("test_TC_Admin_009_NewRatingType_MAT",)
	#"test_NewAttribute_MAT","test_NewAttributeTable_MAT","test_NewAttributeTemplate_MAT"
	testUnit = unittest.TestSuite()

	for case in caseList:
		testUnit.addTest(AdminTest(case))

	reportName = '..\\report\\AssetAdmin'+generatNowStr()+'.html'

	fp = file(reportName,'wb')

	runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "Asset Admin MAT Test Results" , description = "Case Execute Results")

	runner.run(testUnit)