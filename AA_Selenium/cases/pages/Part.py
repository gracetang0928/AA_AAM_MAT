from BasePage import *

class PartDetailElements(BaseElements):
	"""
		PM Schedule Detail Page
	"""
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Elements of  PM Schedule detail
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	# Required Field Elements
	partDetail = (By.ID,"partDetail")
	partNumber = (By.ID,"value(partNumber)")
	
	unitOfMeasure = (By.ID,"value(unitOfMeasure)")
	unitOfMeasureOptions = (By.XPATH,'//select[@id="value(unitOfMeasure)"]/option')
	calculateType = (By.ID,"value(calculateType)")
	calculateTypeOptions = (By.XPATH,'//select[@id="value(calculateType)"]/option')


	# Not Required Fields
	partDesc = (By.ID,"value(description)")
	comments = (By.ID,"value(comments)")
	unitCost = (By.ID,"value(unitCost)")
	partStatus = (By.ID,"value(partStatus)")
	brand = (By.ID,'value(brand)')

class PartDetailPage(BaseFormPage,PartDetailElements):

	def inputComment(self,partNumber):
		self.uidriver.setTextToElement(PartDetailPage.comments,"Update part by auto "+partNumber)


	def inputDetailData(self,partNumber):
				# Fill In Schedule Name
		self.uidriver.setTextToElement(PartDetailPage.partNumber,partNumber)
		# Select Unit Of Measure
#		self.uidriver.clickElement(PartDetailPage.unitOfMeasure)
		unitSelectors = self.uidriver.findElementsInParentElement(PartDetailPage.unitOfMeasure,PartDetailPage.unitOfMeasureOptions)
		self.uidriver.clickElementEntity(unitSelectors[1])
		sleep(1)

		# Select Calculate Type
#		self.uidriver.clickElement(PartDetailPage.calculateType)
		calculateSelectors = self.uidriver.findElementsInParentElement(PartDetailPage.calculateType,PartDetailPage.calculateTypeOptions)
		self.uidriver.clickElementEntity(calculateSelectors[1])
		sleep(1)

		# Fill In Unit Cost
		self.uidriver.setTextToElement(PartDetailPage.unitCost,partNumber[-2:])


		# Fill In brand name
		self.uidriver.setTextToElement(PartDetailPage.brand,"Grace")


		# Fill in desc
		self.uidriver.setTextToElement(PartDetailPage.partDesc,"This is test by grace. "+partNumber)



class PartListViewPage(BaseListView,PartDetailElements):
	"""
		Part List View Page
	"""
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Elements of  PM Schedule list view
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	pass

class PartFormPage(BaseFormPage):	

	# Tab Elements
	PartTransaction = (By.ID,"partTransaction")
	PartContact = (By.ID,"partXContact")
	PartSupply = (By.ID,"partSupply")

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Part Transaction element : 
	# Button : Search , New ,Void
	Void = (By.ID,"a_delete")

	# Transaction Form ----Common Type Buttons
	submitOfTransaction =(By.ID,"a_saveTransaction")
	Calculate = (By.ID,"a_Calculate")
	# Transaction Form ----Common Type Required Fields

	transactionType = (By.ID,"value(transactionType)")
	locationName = (By.ID,"value(locationSeq)")
	locationNameOptions = (By.XPATH,'//select[@id="value(locationSeq)"]/option')
	quantity = (By.ID,"value(quantity)")
	# Transaction Form Elements----Transfer Type Required Fields
	transferToLocation = (By.ID,"value(toLocationSeq)")

	# Part Contact Tab Button: Look Up , Delete
	# Look Up Contact Form Element


	
	# Look up Asset page elements
	
	
	# Look up address info

	def inputReceivePart(self,quantityInfo):

		# Select Location 
		locationSelectors = self.uidriver.findElementsInParentElement(PartFormPage.locationName,PartFormPage.locationNameOptions)
		self.uidriver.clickElementEntity(locationSelectors[1])
		sleep(1)
		self.uidriver.setTextToElement(PartFormPage.quantity,quantityInfo)

	def inputIssuePart(self,streetNumberInfo):
		self.uidriver.setTextToElement(PMFormPage.streetNumber,streetNumberInfo)

	def inputTransferPart(self,resultPortlet):
		sleep(1)
		dataCheckbox = self.uidriver.findElementInParentElement((By.ID,"row1"),(By.XPATH,'//input[@property="value(chk_%s,0)"]'%resultPortlet))
		self.uidriver.clickElementEntity(dataCheckbox)















