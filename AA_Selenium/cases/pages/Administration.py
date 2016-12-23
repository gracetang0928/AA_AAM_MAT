#-*- coding: utf-8 -*-
from BasePage import *
from public import getDateAfter


class SetUpPage(BasePage):
	setUpFrame = (By.ID,"setup")

	# Assets list
	Assets = (By.ID,"IAssets")
	attribute = (By.ID,"asset_attribute")
	attributeTable =(By.ID,"asset_attr_table")
	attributeTemplate = (By.ID,"asset_template")
	conditionAssessment =(By.ID,"asset_condition_asse")
	ratingType = (By.ID,"asset_rating")
	assetType = (By.ID,"asset_type")


	# Costing
	Costing = (By.ID,"ICosting")
	costGroup = (By.ID,"work_order_cost_group")
	costItem = (By.ID,"work_order_cost_item")

	# Part
	Part = (By.ID,"IPart")
	partContact = (By.ID,"part_contact")
	partLocation = (By.ID,"part_location")

	# Work Order
	WorkOrders = (By.ID,"IWork Orders")
	workOrderTask = (By.ID,"work_order_task")
	workOrderTemplate = (By.ID,"work_order_template")

	# Time Accounting
	TimeAccounting = (By.ID,"ITime Accounting")
	timeGroup = (By.ID,"time_acc_group")
	timeType = (By.ID,"time_acc_type")

class DataList(BaseListView):
	pass
	
class AttributeForm(BaseForm):
	attrFormFrame = (By.ID,"attributeForm")
	# Fields of Attributes--Required Fields
	# Data Typ : Date, Number,Text,Textarea,Time,Y/N
	valueDataType = (By.ID,"value(r1AttributeValueType)")
	valueDataTypeOptions = (By.XPATH,'//select[@id="value(r1AttributeValueType)"]/option')
	attributeName = (By.ID,"value(r1AttributeName)")
	attributeLabel = (By.ID,"value(r1AttributeLabel)")

	# Fields of Attributes--Not Required Fields
	attributeGroup = (By.ID,"value(r1AttributeGroup)")	
	attributeLength = (By.ID,"value(r1AttributeLength)")
	defaultValue = (By.ID,"value(r1AttributeValue)")
	unitType = (By.ID,"value(r1AttributeUnitType)")
	attributeDesc = (By.ID,"value(r1AttributeDesc)")


	def inputDetailData(self,dataType, attributeName):
		# Required fields

		dataTypes = self.uidriver.findElementsInParentElement(AttributeForm.valueDataType,AttributeForm.valueDataTypeOptions)
		for select in dataTypes:
			if select.get_attribute("value")==dataType :
				self.uidriver.clickElementEntity(select)
				break
		sleep(1)

		# Input Attribute Name and Label
		self.uidriver.setTextToElement(AttributeForm.attributeName,attributeName)
		self.uidriver.setTextToElement(AttributeForm.attributeLabel,attributeName)

		# Not Required fields
		if self.uidriver.findElement(AttributeForm.defaultValue) :
			self.uidriver.setTextToElement(AttributeForm.defaultValue,"998")
		if self.uidriver.findElement(AttributeForm.attributeDesc) :
			self.uidriver.setTextToElement(AttributeForm.attributeDesc,"This test by auto , %s : %s"%(dataType,attributeName))

	


	
class AttributeTableForm(BaseForm):

	attrTableFormFrame = (By.ID,"attrTableForm")
	# Fields of Attribute Table --Required Fields
	attributeTableName = (By.ID,"value(r1AttributeTableName)")

	# Fields of Attribute Rable--Not Required Fields
	attrTableDesc = (By.ID,"value(r1AttrTableDesc)")

	# Tabs
	Attributes = (By.ID,"attributelist")

	# Search Attribute Form
	attributeLabel = (By.ID,"value(r1AttributeLabel)")
	SelectOfAttribute = (By.ID,"selectlist")

	def inputDetailData(self,tableName):
		# Required fields
		self.uidriver.setTextToElement(AttributeTableForm.attributeTableName,tableName)
		# Not Required fields		
		self.uidriver.setTextToElement(AttributeTableForm.attrTableDesc,"This is test by auto " +tableName)



class AttributeTemplateForm(BaseForm):

	attrTableFormFrame = (By.ID,"attrTableForm")
	# Fields of Attribute Template --Required Fields
	templateId = (By.ID,"value(r1AssetTemplateId)")

	# Fields of Attribute Template--Not Required Fields
	templateDesc = (By.ID,"value(r1TemplateDesc)")

	# Tabs
	Attributes = (By.ID,"TemplateAttribute")
	AttributeTables = (By.ID,"AttributeTables")
	
	# Search Attribute Form
	attributeLabel = (By.ID,"value(r1AttributeLabel)")
	# Search Attribute Table Form
	attributeTableName = (By.ID,"value(r1AttributeTableName)")
	# Buttons 
	SubmitOfAttrTable = (By.ID,"templtablelookup")
	SubmitOfAttr = (By.ID,"result")
	

	def inputDetailData(self,templateName):
		# Required fields
		self.uidriver.setTextToElement(AttributeTemplateForm.templateId,templateName)
		# Not Required fields		
		self.uidriver.setTextToElement(AttributeTemplateForm.templateDesc,"This is test by auto " +templateName)


class CostGroupForm(BaseForm):

	
	# Required Fields
	groupName = (By.ID,"value(groupName)")

	# Not Required Fields
	groupDesc = (By.ID,"value(description)")

	# Tabs
	CostItem = (By.ID,"costItemlist")
	Recipient = (By.ID,"Recipient")
	
	# Search cost item Form
	SubmitOfItem = (By.ID,"submit4Group")
	costItem = (By.ID,"value(r1CostItem)")

	SelectOfItem= (By.ID,"selectItem")
	DeleteOfItem = (By.ID,"unAssociateGroupItem")
	# List Check Value
	itemValue = "costitemDef"

	# Buttons 
	AssignAgency = (By.ID,"a_Add_agency")
	AssignModule = (By.ID,"a_Add_module")
	

	def inputDetailData(self,groupName):
		# Required fields
		self.uidriver.setTextToElement(CostGroupForm.groupName,groupName)
		# Not Required fields		
		self.uidriver.setTextToElement(CostGroupForm.groupDesc,"This is test by auto " +groupName)

class CostItemForm(BaseForm):

	# Fields of Attribute Template --Required Fields
	costType = (By.ID,"value(r1CostType)")
	costTypeOption = (By.XPATH,"//option")
	costItem = (By.ID,"value(r1CostItem)")
	# Fields of Attribute Template--Not Required Fields
	CostDesc = (By.ID,"value(r1CostDesc)")

	# Tabs
	CostRates = (By.ID,"CostRates")
	Recipient = (By.ID,"Recipient")
	
	# Cost Rate Form
	activeDate = (By.ID,"value(activeDate)")
	expiredDate = (By.ID,"value(expiredDate)")
	fixedRate = (By.ID,"value(fixedCost)")
	unitRate = (By.ID,"value(unitCost)")
	costFactor = (By.ID,"value(costFactor)")

	# Buttons 
	AssignAgency = (By.ID,"a_Add_agency")
	AssignModule = (By.ID,"a_Add_module")

	def inputDetailData(self,costItem):
		# Required fields
		# Select cost type 
		typeSelectors = self.uidriver.findElementsInParentElement(CostItemForm.costType,CostItemForm.costTypeOption)
		self.uidriver.clickElementEntity(typeSelectors[1])
		sleep(1)

		self.uidriver.setTextToElement(CostItemForm.costItem,costItem)
		
		# Not Required fields		
		self.uidriver.setTextToElement(CostItemForm.CostDesc,"This is test by auto " +costItem)

	def inputCostRate(self,fixedRate,unitRate):
		self.uidriver.setTextToElement(CostItemForm.activeDate,getDateAfter(1))
		self.uidriver.setTextToElement(CostItemForm.expiredDate,getDateAfter(10))
		self.uidriver.setTextToElement(CostItemForm.fixedRate,fixedRate)
		self.uidriver.setTextToElement(CostItemForm.unitRate,unitRate)


class TimeGroupForm(BaseForm):
	# Fields of Attribute Template --Required Fields
	timeGroupName = (By.ID,"value(timeGroupModel*timeGroupName)")
	timeGroupDesc = (By.ID,"value(timeGroupModel*timeGroupDesc)")

	msgCreated = "1 record(s) added successfully."

	# Tabs
	permissions = (By.ID,"permissions")


	def inputDetailData(self,groupName):
		# Input type Name
		self.uidriver.setTextToElement(TimeGroupForm.timeGroupName,groupName)
		# input desc
		self.uidriver.setTextToElement(TimeGroupForm.timeGroupDesc,"This is test by auto "+ groupName)

		

class TimeTypeForm(BaseForm):
	# Required Fields
	timeGroups = (By.ID,"value(timeGroups)")
	groupOption = (By.XPATH,'//select[@id="value(timeGroups)"]/option')
	timeTypeName = (By.ID,"value(timeTypeModel*timeTypeName)")
	hourlyRate = (By.ID,"value(timeTypeModel*defaultRate)")
	percentageAdjustment = (By.ID,"value(timeTypeModel*defaultPctAdj)")
	recordType = (By.ID,"AppTypePicker")

	allRecordType = (By.XPATH,'.//*[@id="AccelaDijit_accela_dojo__TreeNode_0"]/div[1]/span[2]')

	timeTypeDesc = (By.ID,"value(timeTypeModel*timeTypeDesc)")

	def inputDetailData(self,typeName,groupName):
		# Input type Name
		self.uidriver.setTextToElement(TimeTypeForm.timeTypeName,typeName)
		# Input Desc
		self.uidriver.setTextToElement(TimeTypeForm.timeTypeDesc,"This is test by auto "+typeName)

		# Input Hourly Rate, Percentage Adjustment
		self.uidriver.setTextToElement(TimeTypeForm.hourlyRate,"30")
		self.uidriver.setTextToElement(TimeTypeForm.percentageAdjustment,"0")
		# Select time group 
		dataGroups = self.uidriver.findElementsInParentElement(TimeTypeForm.timeGroups,TimeTypeForm.groupOption)
		for select in dataGroups:
			if select.get_attribute("title")== groupName:
				self.uidriver.clickElementEntity(select)
				break
		sleep(1)

		# Select Record Type
		self.uidriver.clickElement(TimeTypeForm.recordType)
		sleep(1)
		self.uidriver.clickElement(TimeTypeForm.allRecordType)
		sleep(1)


class WOTemplateForm(BaseForm):
	# Required Fields
	wOTemplateName = (By.ID,"value(WOTemplateName)")
	groupOption = (By.XPATH,'//select[@id="value(timeGroups)"]/option')

	wOTypegroup = (By.ID,"value(WOType*group)")
	groupOption = (By.XPATH,'//select[@id="value(WOType*group)"]/option')
	wOTypetype = (By.ID,"value(WOType*type)")
	typeOption = (By.XPATH,'//select[@id="value(WOType*type)"]/option')
	wOTypesubType = (By.ID,"value(WOType*subType)")
	subTypeOption = (By.XPATH,'//select[@id="value(WOType*subType)"]/option')
	wOTypecategory = (By.ID,"value(WOType*category)")
	categoryOption = (By.XPATH,'//select[@id="value(WOType*category)"]/option')

	currentUser = (By.LINK_TEXT,"Current User")
	currentDepartment = (By.LINK_TEXT,"Current Department")

	WODescription = (By.ID,"value(WODescription)")
	comments = (By.ID,"value(comments)")

	# Tabs
	Costing = (By.ID,"woTemplateCosting")
	Part = (By.ID,"wotPart")

	# Cost item form
	costItem = (By.ID,"value(r1CostItem)")
	SubmitOfWO = (By.ID,"submit4WOT")
	costListValue = "costitemDef"
	SelectOfWO = (By.ID,"submit4WOT")
	# Part Form
	partNumber = (By.ID,"value(partNumber)")
	partListValue = "part"

	# Part List field
	partLocationName = (By.ID,"locationSeq")
	partQuantity = (By.ID,"quantity")
	partComments = (By.ID,"comments")

	SaveOfPart = (By.ID,"submit4WOTSecond")
	

	def inputDetailData(self,woName):
		# Input wo template Name
		self.uidriver.setTextToElement(WOTemplateForm.wOTemplateName,woName)
		# Input Desc
		self.uidriver.setTextToElement(WOTemplateForm.WODescription,"This is test by auto "+woName)


		# Select WO Type
		groupSelectors = self.uidriver.findElementsInParentElement(WOTemplateForm.wOTypegroup,WOTemplateForm.groupOption)
		self.uidriver.clickElementEntity(groupSelectors[1])
		sleep(1)

		typeSelectors = self.uidriver.findElementsInParentElement(WOTemplateForm.wOTypetype,WOTemplateForm.typeOption)
		self.uidriver.clickElementEntity(typeSelectors[1])
		sleep(1)

		subTypeSelectors = self.uidriver.findElementsInParentElement(WOTemplateForm.wOTypesubType,WOTemplateForm.subTypeOption)
		self.uidriver.clickElementEntity(subTypeSelectors[1])
		sleep(1)

		categotySelectors = self.uidriver.findElementsInParentElement(WOTemplateForm.wOTypecategory,WOTemplateForm.categoryOption)
		self.uidriver.clickElementEntity(categotySelectors[1])

		sleep(1)
		self.uidriver.clickElement(WOTemplateForm.currentDepartment)
		self.uidriver.clickElement(WOTemplateForm.currentUser)

	def inputPartData(self,numberPart):	
		locationSelectors = self.uidriver.findElementsInParentElement(WOTemplateForm.partLocationName,(By.XPATH,'//option'))
		self.uidriver.clickElementEntity(locationSelectors[1])
		sleep(1)

		self.uidriver.setTextToElement(WOTemplateForm.partQuantity,numberPart)
		# Input Desc
		self.uidriver.setTextToElement(WOTemplateForm.partComments,"This is test by auto ")										
class PartLocationForm(BaseForm):
	# Required Fields
	locationName = (By.ID,"value(locationName)")
	
	locationType = (By.ID,"value(locationType)")
	typeOption = (By.XPATH,'//option')

	comments = (By.ID,"value(comments)")

	def inputDetailData(self,locationName):
		# Input type Name
		self.uidriver.setTextToElement(PartLocationForm.locationName,locationName)
		# Input Desc
		if self.uidriver.findElement(PartLocationForm.comments):
			self.uidriver.setTextToElement(PartLocationForm.comments,"This is test by auto "+locationName)

		# Select time group 
		if self.uidriver.findElement(PartLocationForm.locationType):
			typeSelectors = self.uidriver.findElementsInParentElement(PartLocationForm.locationType,PartLocationForm.typeOption)
			self.uidriver.clickElementEntity(typeSelectors[1])

class AssetCAForm(BaseForm):
	conditionAssessment = (By.ID,"value(conditionAssessment)")
	desc = (By.ID,"value(templateDesc)")

	# Tabs
	observAttribute = (By.ID,"ObservAttribute") 
	Attribute = (By.ID,"caAttribute")

	# Attribute Form
	attributeName = (By.ID,"value(r1AttributeName)")
	listValue = "attrDef"
	DeleteOfAttribute = (By.ID,"delAttribute")

	def inputDetailData(self,caName):
		# Input type Name
		self.uidriver.setTextToElement(AssetCAForm.conditionAssessment,caName)
		# Input Desc
		if self.uidriver.findElement(AssetCAForm.desc):
			self.uidriver.setTextToElement(AssetCAForm.desc,"This is test by auto "+caName)


class RatingTypeForm(BaseForm):
	# Reqired Field
	ratingType = (By.ID,"value(ratingType)")
	assetGroup = (By.ID,"value(assetGroup)")
	groupSelect = (By.XPATH,"//option")
	assetType = (By.ID,"value(assetType)")
	typeSelect = (By.XPATH,'//select[@id="value(assetType)"]/option')
	conditionAssessment = (By.ID,"value(conditionAssessment)")
	caSelect = (By.XPATH,'//select[@id="value(conditionAssessment)"]/option') 
	upperLimit = (By.ID,"value(upperLimit)")
	lowerLimit = (By.ID,"value(lowerLimit)")
	formula = (By.ID,"formula")

	CAFields = (By.XPATH,".//*[@id='caTree']/div[2/]div[1]/img")
	CAFieldsItem = (By.XPATH,".//*[@id='caTree']/div[2]/div[2]/div[1]/div[1]/span[2]/span")

	mathAdd = (By.XPATH,".//*[@id='AccelaDijit_accela_dojo_TreeNode2_6']/div[1]/span[2]/span")

	# Button
	Validate = (By.ID,"validateAll")

	def inputDetailData(self,ratingName,caName,attrName):
		# Input type Name
		self.uidriver.setTextToElement(RatingTypeForm.ratingType,ratingName)
		self.uidriver.setTextToElement(RatingTypeForm.upperLimit,"10")
		self.uidriver.setTextToElement(RatingTypeForm.lowerLimit,"1")

		groupSelectors = self.uidriver.findElementsInParentElement(RatingTypeForm.assetGroup,RatingTypeForm.groupSelect)
		self.uidriver.clickElementEntity(groupSelectors[1])
		sleep(2)
		# Select asset type
		typeSelectors = self.uidriver.findElementsInParentElement(RatingTypeForm.assetType,RatingTypeForm.typeSelect)
		self.uidriver.clickElementEntity(typeSelectors[1])
		sleep(1)

		caSelectors = self.uidriver.findElementsInParentElement(RatingTypeForm.assetType,RatingTypeForm.caSelect)
		for select in caSelectors:
			if select.get_attribute("value")== caName:
				self.uidriver.clickElementEntity(select)
				break
		sleep(1)

		self.uidriver.setTextToElement(RatingTypeForm.formula,"[CA::"+attrName+"]*2")
		sleep(1)      