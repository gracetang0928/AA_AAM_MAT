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

class AssetCADetailElement(object):
	"""
	Asset detail main elements set
	"""
	# Asset  Tab elements
	Detail = (By.ID,"AssetDetail")

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
class AssetListView(BaseListView,AssetDetailElement):

	ViewLog = (By.ID,"a_conditionLog")
	NewWO = (By.ID,"a_addWOFromAssetList")

	
	def checkAssetRecord(self,lineNumber):
		data = self.uidriver.findElementInParentElement((By.ID,"row%d"%lineNumber),(By.XPATH, '//input[@name="value(chk_asset,%d)"]'%lineNumber))
		self.uidriver.clickElementEntity(data)



##############################################################################
# Asset new page class
# Also Asset detail page 
##############################################################################
class AssetDetail(BaseForm,AssetDetailElement):

	# Elements in the asset detail tab page
	
	Clone = (By.ID,"enterClone")
	
	# Elements of clone form
	cloneAssetIDPrefix = (By.ID,"value(assetidPrefix)")
	cloneAssetNO = (By.ID,"value(cloneNumber)")
	SubmitOfClone= (By.ID,"clone")
	Complete = (By.ID,"CloneComplete")


	def inputDetailData(self,assetIDInfo):
		self.uidriver.waitForElementClickable(AssetDetail.assetGroup,30)
		# Select asset group
		groupSelectors = self.uidriver.findElementsInParentElement(AssetDetail.assetGroup,AssetDetail.groupSelect)
		self.uidriver.clickElementEntity(groupSelectors[1])
		sleep(5)
		self.uidriver.waitForElementClickable(AssetDetail.assetType,30)
		sleep(3)
		# Select asset type
		typeSelectors = self.uidriver.findElementsInParentElement(AssetDetail.assetType,AssetDetail.typeSelect)
		self.uidriver.clickElementEntity(typeSelectors[1])
		sleep(5)
		self.uidriver.waitForElementClickable(AssetDetail.assetID,30)
		# Generate a random number string to fill asset ID
		sleep(3)
		self.uidriver.setTextToElement(AssetDetail.assetID,assetIDInfo)
		self.uidriver.setTextToElement(AssetDetail.assetName,"T"+assetIDInfo)
		self.uidriver.setTextToElement(AssetDetail.assetComment,"this is test by grace auto "+ assetIDInfo)
		self.uidriver.setTextToElement(AssetDetail.assetSize,assetIDInfo[5:7])

		sleep(2)

	def updateDetail(self,updateInfo):
		sleep(2)
		self.uidriver.setTextToElement(AssetDetail.assetDesc,updateInfo+" Update By Auto")

	def inputCloneData(self,assetIDPrefixInfo,cloneNumberInfo):
		self.uidriver.setTextToElement(AssetDetail.cloneAssetIDPrefix,assetIDPrefixInfo)
		self.uidriver.setTextToElement(AssetDetail.cloneAssetNO,cloneNumberInfo)

class AssetForm(BaseForm):
	# Tab Elements
	AssetDetail = (By.ID,"AssetDetail")
	Address =(By.ID,"Address")
	Contact = (By.ID,"Contact")
	LinkedAssets = (By.ID,"AssetRelationships")

	