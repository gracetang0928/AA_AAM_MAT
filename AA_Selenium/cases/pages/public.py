# -*- coding: utf-8 -*-

import unittest
from LoginPage import LoginPage,Dashboard
from UIDriver import UIDriver
import datetime




# Generate Asset ID When new asset
def generatNowStr():
	nowTime = datetime.datetime.now().strftime("%m%d%H%M%S")
	return nowTime


def getDateAfter(n):
	nowDay = datetime.datetime.now()
	afterDays = nowDay + datetime.timedelta(days =n)
	strf = afterDays.strftime("%m/%d/%Y")
	return strf


def loginAndFindPortlet(self,portletName):
	self.uidriver = UIDriver("Firefox")
	#　self.baseUrl =  "https://vm-server28.missionsky.com:24443"
	self.baseUrl = "https://av.test.accela.com"
	#self.baseUrl = "https://qa-server1.missionsky.com:13443"
	# self.baseUrl = "https://vm-server28.missionsky.com:24443"
	self.uidriver.get(self.baseUrl)	
	self.loginPage = LoginPage(self.uidriver)
	self.loginPage.loginSystem("qa","tang","tang")
	# self.loginPage.loginSystem("lexky","tang","tang")
	self.dashBoard = Dashboard(self.uidriver)
	print "Login system successfully."
	self.dashBoard.findPortlet(portletName)

def endCase(self):
	self.dashBoard.logoutSystem()
	self.uidriver.quitDriver()

############################################################################
# Public var
############################################################################
newAssetID  = generatNowStr()
newPMName =newPartID = newAssetID[-6:]



		
		
