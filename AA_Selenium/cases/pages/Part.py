from BasePage import *

class PartDetailElements(BaseElements):
	"""
		PM Schedule Detail Page
	"""
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Elements of  PM Schedule detail
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	# Required Field Elements
	Detail = (By.ID,"partDetail")
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

class PartDetail(BaseForm,PartDetailElements):

	def updateDetail(self,partNumber):
		self.uidriver.setTextToElement(PartDetail.comments,"Update part by auto "+partNumber)


	def inputDetailData(self,partNumber):
				# Fill In Schedule Name
		self.uidriver.setTextToElement(PartDetail.partNumber,partNumber)
		# Select Unit Of Measure
#		self.uidriver.clickElement(PartDetail.unitOfMeasure)
		unitSelectors = self.uidriver.findElementsInParentElement(PartDetail.unitOfMeasure,PartDetail.unitOfMeasureOptions)
		self.uidriver.clickElementEntity(unitSelectors[1])
		sleep(1)

		# Select Calculate Type
#		self.uidriver.clickElement(PartDetail.calculateType)
		calculateSelectors = self.uidriver.findElementsInParentElement(PartDetail.calculateType,PartDetail.calculateTypeOptions)
		self.uidriver.clickElementEntity(calculateSelectors[1])
		sleep(1)

		# Fill In Unit Cost
		self.uidriver.setTextToElement(PartDetail.unitCost,partNumber[-2:])


		# Fill In brand name
		self.uidriver.setTextToElement(PartDetail.brand,"Grace")


		# Fill in desc
		self.uidriver.setTextToElement(PartDetail.partDesc,"This is test by grace. "+partNumber)



class PartListView(BaseListView,PartDetailElements):
	"""
		Part List View Page
	"""
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Elements of  PM Schedule list view
	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	pass

class PartForm(BaseForm):	

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
	transLocationOptions =  (By.XPATH,'//select[@id="value(toLocationSeq)"]/option')

	comments = (By.ID,"value(comments)")

	# Part Contact Tab Button: Look Up , Delete
	# Look Up Contact Form Element

	# Part Supply Table
	table = (By.ID,"content_main_table")	
	
	# Look up address info

	#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# Transaction Type : ISSUE, RECEIVE, TRANSFER, ADJUST, RESERVE
	def inputTransactionData(self,transType,quantityInfo):
		# Select Type
		typeSelectors = self.uidriver.findElementsInParentElement(PartForm.transactionType,(By.XPATH,'//option'))
		for select in typeSelectors:
			if select.get_attribute("value")==transType :
				self.uidriver.clickElementEntity(select)
				break
		sleep(1)

		# Select Location 
		locationSelectors = self.uidriver.findElementsInParentElement(PartForm.locationName,PartForm.locationNameOptions)
		for select in locationSelectors:
			if (select.get_attribute("value")).startswith("NPL"):
				self.uidriver.clickElementEntity(select)
				break
		sleep(1)

		
		sleep(1)

		# Select Transfer To Location
		if(transType=="TRANSFER") :
			transferSelectors = self.uidriver.findElementsInParentElement(PartForm.transferToLocation,PartForm.transLocationOptions)
			self.uidriver.clickElementEntity(transferSelectors[2])
			sleep(1)

		self.uidriver.setTextToElement(PartForm.quantity,quantityInfo)
		self.uidriver.setTextToElement(PartForm.comments,transType + quantityInfo + "parts")














