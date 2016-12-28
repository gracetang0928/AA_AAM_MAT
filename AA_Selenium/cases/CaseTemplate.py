# -*- coding: utf-8 -*-
from pages.Administration import *
from pages.LoginPage import *
from pages.public.UIDriver import UIDriver
from InfoSet import *
import unittest



#################################################################################################################################
# Login System
#################################################################################################################################

def loginSystem(self):
	self.uidriver = UIDriver("IE")
	self.baseUrl = siteInfo["site"]
	self.uidriver.get(self.baseUrl)	
	self.loginPage = LoginPage(self.uidriver)
	self.loginPage.loginSystem(siteInfo["agency"],siteInfo["username"],siteInfo["password"])
	# Access New UI
	#self.uidriver.get(self.baseUrl+"/portlets/switchV360AndNewUI.do?newui=Y")
	self.dashBoard = Dashboard(self.uidriver)
	print "Login system successfully."
	
#################################################################################################################################
# Logout System
#################################################################################################################################
def endCase(self):
	self.dashBoard.logoutSystem()
	self.uidriver.quitDriver()


#################################################################################################################################
# Genneral method , Search data in list view 
# Need instance a list class when use this method
#################################################################################################################################
"""
Search data at list view, steps :
Click search button >wait the search page > fill in search value > submit > check the result 

:Args:
	 - dataList: instance of list class 
	 - searchButton: search button element information
	 - searchField: search field element information
	 - searchValue: search value
	 - submit: submit button element information of search page

:Usage:
	pmList = PMListView(self.uidriver,self.portlet)
	searchAtListView(self,pmList,pmList.scheduleName,PMname)
"""
def searchAtListView(self,dataList,searchField,searchValue):
	# Click search button in the list view 
	dataList.click(dataList.Search)

	# Wait the search page loaded
	dataList.uidriver.waitForElementPresent(searchField,30)
	self.assertIsNotNone(dataList.uidriver.findElement(searchField),msg="Error: Search page did not load.")
	sleep(3)
	# input the search condition , the click submit
	dataList.inputSearchCondition(searchField,searchValue)
	dataList.click(dataList.Submit)

	# Check the result 
	self.assertIsNotNone(dataList.uidriver.findElement(dataList.firstRecord),"Error：No result return. ")


##########################################################################################################################
# Genneral method , Create data in admin
# Need instance a list class when use this method
##########################################################################################################################
"""
Create Admin data

:Args:
	 - item: string , Set Up item , Assets
	 - subItem: string , subItem of item , Assets > Attribute
	 - listFrame: string, list iframe information 
	 - formClass: string , Detail form class name
	 - formFrame: string , Form iframe information
	 - data, tuple, input date parmeter
	 - msgCreated: string, msg of data created 

:Usage:
	admin = SetUpPage(self.uidriver)
	createAdminData(self,admin.Assets,admin.attributeTemplate,self.templatePortlet,AttributeTemplateForm,self.templatePortlet,(newAttributeTemplate,),"The template created successfully.")
"""

def createAdminData(self,admin,item,subItem,DataList,listFrame,formClass,formFrame,data,msgPrompt):
	# Set Up > Item > Subitem
	admin.click(item)
	admin.click(subItem)

	dataList = DataList(self.uidriver,listFrame)
	dataList.uidriver.waitForElementPresent(dataList.New,30)
	dataList.click(dataList.New)

	
	# Input data , the click submit
	form = formClass(self.uidriver,formFrame)
	form.uidriver.waitForElementPresent(form.Submit,30)

	form.inputDetailData(*data)

	form.click(form.Submit)
	form.uidriver.waitForElementPresent(form.Save,30)
	form.uidriver.saveScreenshot("..\\report\\image\\New%s"%(subItem[1])+generatNowStr()+".png")
	self.assertEquals(form.uidriver.getTextOfElement(form.msg),msgPrompt,msg="Error: New %s failed."%subItem[1])




#########################################################################################
# Genneral method , Create data in Daily side
# Need instance a list class when use this method
#########################################################################################

"""
Create Ref data

Search data at list view, steps :
Click search button >wait the search page > fill in search value > submit > check the result 

:Args:
	 - dataList: instance of list class 
	 - detailClass：detail class name
	 - portletName: portlet name
	 - data:tuple, data parmeter
	 - msgCreated: string, msg of data created 
	 - msgUpdate: string .msg after update detail
:Usage:
	createRefData(self,PMListView,PMDetail,"id-pmschedule",data,msgCreated)
"""

def createRefData(self,listClass,detailClass,portletName,data,msgCreated):
	dataList = listClass(self.uidriver,portletName)
	# Click the New button , Access the new PM page 
	dataList.click(dataList.New)

	# Access the detal page , and wait for load over
	detail = detailClass(self.uidriver,portletName)
	detail.uidriver.waitForElementPresent(detail.Submit,30)
	self.assertIsNotNone(detail.uidriver.findElement(detail.Submit),msg="Error: %s detail page is still loading."%portletName)
 
	# Input data , the click submit
	detail.inputDetailData(*data)
	detail.click(detail.Submit)

	# Save the screen shot
	detail.uidriver.saveScreenshot("..\\report\\image\\Create%s"%(portletName)+generatNowStr()+".png")
	self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),msgCreated,msg="Error: new %s failed."%portletName)

	detail.closeEMSE()	

#########################################################################################
# Genneral method , Create data in Daily side
# Need instance a list class when use this method
#########################################################################################

"""
Update Ref data

Search data at list view, steps :
Click search button >wait the search page > fill in search value > submit > check the result 

:Args:
	 - listClass: list class name
	 - detailClass：detail class name
	 - portletName: portlet name
	 - data:tuple, data parmeter
	 - msgUpdate: string .msg after update detail
:Usage:
	createRefData(self,PMListView,PMDetail,"id-pmschedule",data,msgCreated)
"""
def updateRefData(self,listClass,detailClass,portletName,data,msgUpdate,saveButton=(By.ID,"save")):
	dataList = listClass(self.uidriver,portletName)
	dataList.selectFirstRecordInList()

	# Wait for load over
	detail = detailClass(self.uidriver,portletName)
	detail.uidriver.waitForElementPresent(detail.Detail,30)
	self.assertIsNotNone(detail.uidriver.findElement(detail.Detail),msg="Error: Deatail page is still loading.")

	# Input the comment, Save
	detail.updateDetail(*data)
	detail.click(saveButton)

	# Save the screen shot
	detail.uidriver.saveScreenshot("..\\report\\image\\Update%s"%(portletName)+generatNowStr()+".png")
	self.assertEquals(detail.uidriver.getTextOfElement(detail.msg),msgUpdate,msg="Error: Update %s failed."%(portletName))
	detail.closeEMSE()	

	

#########################################################################################
# Genneral method , Create data in Daily side
# Need instance a list class when use this method
#########################################################################################

"""
Associate record data on tab by Look Up

steps :
Click Tab >wait the tab page > Click Look up button >　fill in search value > submit > check the result > select

:Args:
	 - form: instance of form class 
	 - tab: tab of form
	 - lookup: lookup button on the tab
	 - searchField: search field element information
	 - searchValue: search value
	 - submit: submit button element information of search page
	 - resultValue: result list value checkbox value
	 - select: select button element information
	 - waitButton: button of tab ,For confirm page loaded.
	 - msgPrompt: msg after Associated
:Usage:
	msgAssociateTable = "1 record(s) selected successfully."
	associatedDataByLookUp(self,form,form.AttributeTables,form.LookUp,form.attributeTableName,newAttributeTable,form.SubmitOfAttrTable,"AttrTable",form.Select,form.Delete,msgAssociateTable)
"""

def associatedDataByLookUp(self,form,tab,lookup,searchField,searchValue,submit,resultValue,select,waitButton,msgPrompt):
	# Click the Attributes Tab > look up attribute > Fill in data > Submit > select
	form.click(tab)
	form.uidriver.waitForElementPresent(lookup,30)
	form.click(lookup)
	# Wait for the searched field present
	form.uidriver.waitForElementPresent(searchField,30)
	self.assertIsNotNone(form.uidriver.findElement(searchField),msg="Error: Look up %s form did not load."%tab[1])
	
	# Associated Attribute to Attribute Table
	form.inputSearchCondition(searchField,searchValue)
	form.click(submit)
	form.uidriver.waitForElementPresent(lookup,30)
	sleep(1)
	form.checkRecordInResultList(resultValue)
	form.click(select)
	form.uidriver.waitForElementClickable(waitButton,30)
	form.uidriver.saveScreenshot("..\\report\\image\\Associated%s"%(tab[1])+generatNowStr()+".png")
	self.assertEquals(form.uidriver.getTextOfElement(form.msg),msgPrompt,msg="Error: Associated %s failed."%tab[1])
	sleep(1)


#########################################################################################
# Genneral method , Create data in Daily side
# Need instance a list class when use this method
#########################################################################################

"""
New record data on tab 

steps :
Click Tab >wait the tab page > Click New button >　fill in  value > submit > check the msg

:Args:
	 - form: instance of form class 
	 - tab: tab of form
	 - new: new button on the tab
	 - inputDataMethod: Method of fill in data
	 - data: tuple-parameters of inputDataMethod
	 - submit: submit button element information of form page
	 - msgPrompt: msg after new data
:Usage:
	msgAssociateTable = "1 record(s) selected successfully."
	associatedDataByNew(self,form,form.AttributeTables,form.LookUp,form.attributeTableName,newAttributeTable,form.SubmitOfAttrTable,"AttrTable",form.Select,form.Delete,msgAssociateTable)
"""

def associatedDataByNew(self,form,tab,new,inputDataMethod,data,submit,msgPrompt):

	# Click the Link Asset Tab after page load over
	form.uidriver.waitForElementPresent(tab,30)
	form.click(tab)
	form.uidriver.waitForElementPresent(new,30)

	# New > Fill in data > Submit
	form.click(new)
	form.uidriver.waitForElementPresent(submit,30)
	self.assertIsNotNone(form.uidriver.findElement(submit),msg="Error: Page did not load.")

	# click submit
	inputDataMethod(*data)
	form.click(submit)

	# Wait for the  result
	form.uidriver.waitForElementPresent(new,30)

	form.uidriver.saveScreenshot("..\\report\\image\\Add%s"%tab[1] + generatNowStr()+".png")
	self.assertEquals(form.uidriver.getTextOfElement(form.msg),msgPrompt,msg="Error: Add %s failed."%tab[1])




#########################################################################################
# Genneral method , Create data in Daily side
# Need instance a list class when use this method
#########################################################################################

"""
Delete record data on the list view 

:Args:
	 - listViewClass: listView Class name
	 - portlet: portlet name
	 - formClass: form class name

:Usage:
	deleteRefData(self,PartListView,"id-part",PartForm)
"""
def deleteRefData(self,listViewClass,portlet,formClass):
	dataList = listViewClass(self.uidriver,portlet)
	dataList.checkFirstRecordInList()

	form = formClass(self.uidriver,portlet)
	form.click(form.backArrow)

	dataList = AssetsListView(self.uidriver,self.portlet)
	dataList.uidriver.waitForElementPresent(dataList.Delete,20)
	dataList.click(dataList.Delete)


	dataList.uidriver.saveScreenshot("..\\report\\image\\Delete%s"%portlet+generatNowStr()+".png")
	deleteMsg = dataList.uidriver.getTextOfElement(dataList.msg)
	self.assertEquals(deleteMsg,"1 record(s) deleted successfully.",msg = "Error: Delete data failed. ")



