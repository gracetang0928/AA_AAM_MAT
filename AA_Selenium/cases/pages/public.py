# -*- coding: utf-8 -*-

import unittest
from LoginPage import LoginPage,Dashboard
from UIDriver import UIDriver


def loginAndFindPortlet(self,portletName):
	self.uidriver = UIDriver("Firefox")
	#　self.baseUrl =  "https://vm-server28.missionsky.com:24443"
	# self.baseUrl = "https://av.test.accela.com"
	#self.baseUrl = "https://qa-server1.missionsky.com:13443"
	self.baseUrl = "https://vm-server28.missionsky.com:24443"
	self.uidriver.get(self.baseUrl)	
	self.loginPage = LoginPage(self.uidriver)
	self.loginPage.loginSystem("chesapeake","tang","tang")
	# self.loginPage.loginSystem("lexky","tang","tang")
	self.dashBoard = Dashboard(self.uidriver)
	print "Login system successfully."
	self.dashBoard.findPortlet(portletName)

def endCase(self):
	self.dashBoard.logoutSystem()
	self.uidriver.quitDriver()



		
		
