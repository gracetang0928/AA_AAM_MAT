#-*- coding: utf-8 -*-
from BasePage import *
##############################################################################
# Assets portlet related pages class , include :
# AssetDetailElement
# AssetsListView
# SearchAssetPage
# NewAssetPage
##############################################################################



##############################################################################
# Asset detail page elements set
##############################################################################

class AssetDetailElement(object):
	"""
	Asset detail main elements set
	"""
	assetGroup = (By.ID,"value(g1AssetGroup)")
	assetType = (By.ID,"value(g1AssetType)")
	assetID = (By.ID,"value(g1AssetID)")
	assetName = (By.NAME,"value(g1AssetName)")
	assetComment = (By.NAME,"value(g1AssetComments)")
	assetDesc = (By.ID,"value(g1Description)")
	assetSize = (By.ID,"value(assetSize)")
	groupSelect = (By.XPATH,"//option")
	typeSelect = (By.XPATH,'//select[@id="value(g1AssetType)"]/option')

	


##############################################################################
# Asset list view page elements set
##############################################################################
class AssetsListView(BasePage):

	dataListIframe = (By.ID,"dataList")
	menubar = (By.ID,"menu_Bar")
	searchButton = (By.ID,"a_search")
	newButton = (By.ID,"a_new")
	deleteButton =(By.ID,"delete")
	viewlogButton = (By.ID,"a_conditionLog")
	newWOButton = (By.ID,"a_addWOFromAssetList")

	dataTable = (By.ID,"AccelaMainTable")
	firstLineData = (By.ID,"row1")
	#
	lineNO = generatLineNO(5)
	lineData = (By.ID,"row"+lineNO)
	lineDataCheckbox = (By.XPATH,'//input[@name="value(chk_asset,%d)"]'%(int(lineNO)-1))
	lineDataLink = (By.ID,"linkrow"+lineNO)

	noResult = (By.ID,"popNorecord")

	# Message in list view
	errorMsg = (By.ID,"errorMsgPanel")


	def clickNew(self):
		self.switchToCurrentPortletForm(AssetsListView.dataListIframe[1])	
		new = self.uidriver.waitForElementClickable(AssetsListView.newButton,40)
		self.uidriver.clickElementEntity(new)

	def clickSearch(self):
		self.switchToCurrentPortletForm(AssetsListView.dataListIframe[1])
		search = self.uidriver.waitForElementClickable(AssetsListView.searchButton,40)
		self.uidriver.clickElementEntity(search)
	
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Random select a record in the list , then checked the checkbox
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def selectRecordsInList(self):	
		self.switchToCurrentPortletForm(AssetsListView.dataListIframe[1])	
		self.uidriver.waitForElementClickable(AssetsListView.deleteButton,40)
		sleep(2)
		deleteDataCheckbox = self.uidriver.findElementInParentElement(AssetsListView.lineData,AssetsListView.lineDataCheckbox)
		self.uidriver.clickElementEntity(deleteDataCheckbox)

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Click delete button
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def clickDelete(self):
		# Click delete button	
		self.uidriver.clickElement(AssetsListView.deleteButton)


##############################################################################
# Asset search page class
##############################################################################
class SearchAssetPage(BasePage,AssetDetailElement):
	searchIframe = (By.ID,"dataList")
	searchMenu = (By.ID,"menu_Bar")
	submitButton = (By.ID,"acsubmit")
	searchReset = (By.ID,"accelareset")

	def fillInSearchCondition(self,assetIDInfo):
		self.switchToCurrentPortletForm(SearchAssetPage.searchIframe[1])
		self.uidriver.waitForElementPresent(SearchAssetPage.searchMenu,20)
		self.uidriver.setTextToElement(SearchAssetPage.assetID,assetIDInfo)

	def clickSubmit(self,):
		submit = self.uidriver.findElementInParentElement(SearchAssetPage.searchMenu,SearchAssetPage.submitButton)
		self.uidriver.clickElementEntity(submit)

##############################################################################
# Asset new page class
# Also Asset detail page 
##############################################################################
class AssetDetailPage(BasePage,AssetDetailElement):

	dataIframe = (By.ID,"dataForm")

	#new asset menu
	menubar = (By.ID,"menu_bar_")
	submitButton = (By.ID,"acsubmit")
	resetButton = (By.ID,"accelareset")

	#message
	msg = (By.XPATH,'//div[@id="err_msg"]')

	# Elements in the asset detail tab page
	saveButton = (By.ID,"save")
	cloneButton = (By.ID,"enterClone")
	
	# Elements of clone form
	cloneAssetIDPrefix = (By.ID,"value(assetidPrefix)")
	cloneAssetNO = (By.ID,"value(cloneNumber)")
	cloneSubmit = (By.ID,"clone")
	cloneMsg = (By.ID,"errorMsgPanel")
	completeButton = (By.ID,"CloneComplete")

	# Asset information tabs elements
	assetDeatilTab = (By.ID,"AssetDetail")

	def selectAssetDetailTab(self):
		self.switchToCurrentPortletForm(AssetDetailPage.dataIframe[1])
		#sleep(3)
		detailTab = self.uidriver.waitForElementClickable(AssetDetailPage.assetDeatilTab,30)
		sleep(2)
		self.uidriver.clickElementEntity(detailTab)
		self.uidriver.waitForElementPresent(AssetDetailPage.assetDeatilTab,30)
		sleep(3)

	def fillInData(self,assetIDInfo):
		self.uidriver.waitForElementClickable(AssetDetailPage.assetGroup,30)
		# Select asset group
		self.uidriver.clickElement(AssetDetailPage.assetGroup)
		groupSelectors = self.uidriver.findElementsInParentElement(AssetDetailPage.assetGroup,AssetDetailPage.groupSelect)
		self.uidriver.clickElementEntity(groupSelectors[3])
		sleep(5)
		self.uidriver.waitForElementClickable(AssetDetailPage.assetType,30)
		sleep(3)
		# Select asset type
		self.uidriver.clickElement(AssetDetailPage.assetType)
		typeSelectors = self.uidriver.findElementsInParentElement(AssetDetailPage.assetType,AssetDetailPage.typeSelect)
		self.uidriver.clickElementEntity(typeSelectors[1])
		sleep(5)
		self.uidriver.waitForElementClickable(AssetDetailPage.assetID,30)
		# Generate a random number string to fill asset ID
		sleep(3)
		self.uidriver.setTextToElement(AssetDetailPage.assetID,assetIDInfo)
		self.uidriver.setTextToElement(AssetDetailPage.assetName,"T"+assetIDInfo)
		self.uidriver.setTextToElement(AssetDetailPage.assetComment,"this is test by grace auto "+ assetIDInfo)
		self.uidriver.setTextToElement(AssetDetailPage.assetSize,assetIDInfo[5:7])

		sleep(2)

	def clickSubmit(self):
		# Click submit
		submit = self.uidriver.findElementInParentElement(AssetDetailPage.menubar,AssetDetailPage.submitButton)
		self.uidriver.clickElementEntity(submit)
		sleep(10)

	def clickReset(self):
		# Input asset id then click reset
		self.uidriver.setTextToElement(AssetDetailPage.assetID,"SLT-0015")
		self.uidriver.setTextToElement(AssetDetailPage.assetName,"test015")
		self.uidriver.clickElement(AssetDetailPage.resetButton)

	def fillInUpdateDesc(self,updateInfo):
		sleep(2)
		self.uidriver.setTextToElement(AssetDetailPage.assetDesc,updateInfo+generatNowStr())

	def clickSave(self):
		self.uidriver.clickElement(AssetDetailPage.saveButton)

	def fillInCloneData(self,assetIDPrefixInfo,cloneNumberInfo):
		self.switchToCurrentPortletForm(AssetDetailPage.dataIframe[1])
		self.uidriver.waitForElementClickable(AssetDetailPage.cloneSubmit,30)
		self.uidriver.setTextToElement(AssetDetailPage.cloneAssetIDPrefix,assetIDPrefixInfo)
		self.uidriver.setTextToElement(AssetDetailPage.cloneAssetNO,cloneNumberInfo)
		# Click submit

	def clickSubmitOfClone(self):
		self.uidriver.clickElement(AssetDetailPage.cloneSubmit)

	def clickClone(self):
		clone = self.uidriver.waitForElementClickable(AssetDetailPage.cloneButton,30)
		sleep(2)
		self.uidriver.clickElementEntity(clone)

		
	def clickComplete(self):
		sleep(1)
		complete = self.uidriver.waitForElementClickable(AssetDetailPage.completeButton,30)
		sleep(2)
		self.uidriver.clickElementEntity(complete)
		sleep(5)






