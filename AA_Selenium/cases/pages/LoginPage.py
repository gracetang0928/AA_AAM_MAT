#-*- coding: utf-8 -*-
from BasePage import *

class LoginPage(BasePage):
	"""docstring for LoginPage"""
	div_loginBox = (By.ID,"login_box")
	loginIframe = (By.XPATH,".//iframe") 
	agencyInput = (By.ID,"servProvCode")
	userNameInput = (By.ID,"username")
	pwordInput = (By.NAME,"password")
	loginButton = (By.ID,"submit_")
	rememberMe = (By.NAME,"rememberMe")
	switchNewUI = (By.LINK_TEXT,"Switch New UI")


	def loginSystem(self,agency,userName,passWord):
		#找到登陆iframe，切换进入
		self.uidriver.waitForElementPresent(LoginPage.div_loginBox,15)
		loginBox = self.uidriver.findElementInParentElement(LoginPage.div_loginBox,LoginPage.loginIframe)
		self.uidriver.switchToIframe(loginBox) 
		#分别输入agency,username,password
		sleep(1)
		self.uidriver.setTextToElement(LoginPage.agencyInput,agency)
		self.uidriver.setTextToElement(LoginPage.agencyInput,Keys.TAB)

		sleep(1)
		#输入用户名，点击login 
		self.uidriver.setTextToElement(LoginPage.userNameInput,userName)
		self.uidriver.setTextToElement(LoginPage.pwordInput,passWord)
		self.uidriver.clickElement(LoginPage.loginButton)
		# if it is old UI 
		sleep(2)
		



class Dashboard(BasePage):
#	globalsearch = 
	mainMenuDiv = (By.ID,"main-menu")
	launchpad = (By.XPATH,".//ul/li[3]/a")
	allPageFooter = (By.XPATH,".//*[@id='launchpad-flyout']/div/div[1]/footer")
	portletSearch =  (By.XPATH,".//*[@id='all-pages']/input")
	searchResult = (By.XPATH,".//*[@id='all-pages']/ul/li[2]/div/div[1]/a")
	listViewButton = (By.XPATH,'//a[@title="list view"]')

#setting enter assess point 
	toggle = (By.XPATH,'//div[@class="settings dropdown"]/a')
	dropdownMenuUl = (By.CSS_SELECTOR,".dropdown-menu")
	administration = (By.XPATH,"//li[2]/div/a")
	signOutLink = (By.XPATH,'//li[5]/div/a')
#portlet
	results_page = (By.ID,"iframe-page-container")

#logout 
	loginBoxDiv = (By.ID,"login_box")
# Admin
	setUpFrame = (By.ID,"setup")

	def findPortlet(self,portletName):

		self.uidriver.waitForElementClickable(Dashboard.listViewButton,30)
		sleep(2)
		launchpadElement = self.uidriver.findElementInParentElement(Dashboard.mainMenuDiv,Dashboard.launchpad)		
		self.uidriver.clickElementEntity(launchpadElement)
		sleep(3)
		allFooter = self.uidriver.waitForElementClickable(Dashboard.allPageFooter,15)
		self.uidriver.clickElementEntity(allFooter)
		
		self.uidriver.waitForElementPresent(Dashboard.portletSearch,10)
		self.uidriver.clearTextEdit(Dashboard.portletSearch)
		self.uidriver.setTextToElement(Dashboard.portletSearch,portletName)
		sleep(1)
#		self.uidriver.waitForElementPresent(Dashboard.searchResult,20)
		self.uidriver.clickElement(Dashboard.searchResult)
		print "Access ",portletName,"successfully."

	def accessAdmin(self):
		self.uidriver.switchToDefaultContent()
		sleep(3)
		self.uidriver.clickElement(Dashboard.toggle)
		sleep(3)
		admin = self.uidriver.findElementInParentElement(Dashboard.dropdownMenuUl,Dashboard.administration)
		self.uidriver.clickElementEntity(admin)
		self.uidriver.waitForElementPresent(Dashboard.setUpFrame,20)
		self.switchToCurrentContainer(Dashboard.setUpFrame)
		print "Access Administration successfully."


	def logoutSystem(self):
		self.uidriver.switchToDefaultContent()
		sleep(3)
		self.uidriver.clickElement(Dashboard.toggle)
		sleep(3)
		signOut = self.uidriver.findElementInParentElement(Dashboard.dropdownMenuUl,Dashboard.signOutLink)
		self.uidriver.clickElementEntity(signOut)
		self.uidriver.waitForElementPresent(Dashboard.loginBoxDiv,5)
		print "Logout successfully."




		

