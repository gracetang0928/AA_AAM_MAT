# -*- coding: utf-8 -*-
from CaseTemplate import *

class  MAT_TimeAccounting(unittest.TestCase):
	"""Time Accounting Function """

	timeGroupPortlet = "name-timeGroup-admin"
	timeTypePortlet = "name-timetype-admin"

	
	def setUp(self):
		loginSystem(self)
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

