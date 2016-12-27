#-*- coding: utf-8 -*-
from public.BasePage import *

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
	Detail = (By.ID,"Detail")
	# New Asset CA Page
	conditionAssessment = (By.ID,"value(conditionAssessment)")
	caoption = (By.XPATH,'//option') # select[@id="value(conditionAssessment)"]
	# Search Asset Page
	assetID = (By.ID,"value(g1AssetID)")
	SubmitOfAsset = (By.ID,"submit4CA")
	assetRadio = (By.NAME,"value(chk_asset)")
	SelectOfAsset = (By.ID,"select4CA")

	# Asset CA detail element
	comments = (By.ID,"value(comments)")
	currentUser = (By.LINK_TEXT,"Current User")
	currentDepartment = (By.LINK_TEXT,"Current Department")
	inspDate = (By.ID,"date(inspDate)")
	inspTime = (By.ID,"EBAComboBoxTextinspTime")
	SaveOfCA = (By.ID,'editSave')

	# List View search Asset ID 
	assetID2 = (By.ID,"value(assetID)")




class AssetCAListView(BaseListView,AssetCADetailElement):
	pass
##############################################################################
# Asset new page class
# Also Asset detail page 
##############################################################################
class AssetCADetail(BaseForm,AssetCADetailElement):

	# Elements in the asset detail tab page
	
	Clone = (By.ID,"enterClone")
	
	# Elements of clone form
	cloneAssetIDPrefix = (By.ID,"value(assetidPrefix)")
	cloneAssetNO = (By.ID,"value(cloneNumber)")
	SubmitOfClone= (By.ID,"clone")

	def selectConditionAssessment(self,caInfo):#
		#self.uidriver.clickElement(AssetCADetail.conditionAssessment)
		sleep(1)
		CAselectors = self.uidriver.findElementsInParentElement(AssetCADetail.conditionAssessment,AssetCADetail.caoption)

		for select in CAselectors:
			if select.get_attribute("value") ==caInfo:
				self.uidriver.clickElementEntity(select)
				break
		sleep(2)
	
	def inputDetailData(self):

		self.uidriver.clickElement(AssetCADetail.currentUser)
		sleep(1)
		self.uidriver.setTextToElement(AssetCADetail.inspDate,getDateAfter(1))
		self.uidriver.setTextToElement(AssetCADetail.inspTime,"01:00 AM")

	def selectAssetInList(self):
		radio = self.uidriver.findElementInParentElement((By.ID,"row1"),(By.ID,"ac360_list_id"))
		self.uidriver.clickElementEntity(radio)

	def updateDetail(self,dataInfo):
		sleep(2)
		self.uidriver.setTextToElement(AssetCADetail.comments,getDateAfter(0)+" Update By Auto "+dataInfo)


class AssetForm(BaseForm):
	# Tab Elements
	AssetDetail = (By.ID,"AssetDetail")
	Address =(By.ID,"Address")
	Contact = (By.ID,"Contact")
	LinkedAssets = (By.ID,"AssetRelationships")

	