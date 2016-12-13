# -*- coding: utf-8 -*-
from pages.LoginPage import *
from pages.PMSchdulePage import *
from pages.public import *
import unittest 

class  PMScheduleTest(unittest.TestCase):
	"""PM Schedules Basic Function """
	def setUp(self):
		loginAndFindPortlet(self,"PM Schedules")
	def tearDown(self):
		endCase(self)


	def test_NewPM_MAT(self):

		pmList = PMListViewPage(self.uidriver,"pmschedule")
		pmList.clickNew()





	def test_SearchPM_MAT(self):
		pmList = PMListViewPage(self.uidriver,"pmschedule")
		pmList.clickSearch()
		pmSearchPage = PMSearchPage(self.uidriver)
		self.assertIsNotNone(pmSearchPage.uidriver.findElement(pmSearchPage.scheduleName),msg="Error：PM search page did not load.")
		pmSearchPage.fillInSearchCondition("Grace test")
		pmSearchPage.clickSubmit()
		pmSearchPage.uidriver.waitForElementPresent(pmSearchPage.searchButton,20)
		pmSearchPage.uidriver.saveScreenshot("..\\report\\image\\PM-Search"+generatNowStr()+".png")
		self.assertIsNone(pmList.uidriver.findElement(pmList.noResult),msg="Error：No result return　when search PM. ")



if __name__=="__main__":
	unittest.main()