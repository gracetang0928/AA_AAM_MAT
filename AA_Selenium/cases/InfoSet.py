#-*- coding: utf-8 -*-
import csv
from pages.public.BasePage import generatNowStr
#################################################################################################################################
# Get site info and login info
#################################################################################################################################
def getSiteInfo():
	siteInfo = None
	with open('C:\\Users\\grace.tang\\Desktop\\ps\\AA_Selenium\\data\\UserInfo.csv','rb') as csvfile:
		infoReader = csv.DictReader(csvfile)
		rows = [row for row in infoReader]
		siteInfo = rows[0]
	return siteInfo


siteInfo=getSiteInfo()

############################################################################
# AA 
############################################################################

timeStr = generatNowStr()
# Ref Asset ID
newAssetID  = timeStr[3:10]
print newAssetID

# Ref PM Schedule Name 
newPMName = "NPM" + timeStr[-3:]
# Part Number
newPartID = "NPA" + timeStr[-3:] 

#############################################################################
# Admin 
#############################################################################
# Asset Type Name
newAssetType = "NAT"  + timeStr[-4:]  
# Asset Attribute name
newAttribute = "NA"  + timeStr[-4:]  
# Asset Attribute Table Name
newAttributeTable ="NATA"  + timeStr[-4:]  
# Asset Attribute Template Name
newAttributeTemplate = "NATE"  + timeStr[-4:] 
# Asset CA  Name
newAssetCA = "NACA"  + timeStr[-4:] 
# Asset Rating Type Name
newRatingType = "NRT"  + timeStr[-4:] 

# Cost Group Name
newCostGroup = "NCG" +  timeStr[-4:] 
# Cost Item Name 
newCostItem = "NCI" +  timeStr[-4:] 

newTimeType = "NTT" + timeStr[-4:] 

newTimeGroup = "NTG" +timeStr[-4:] 
	
newPartLocation = "NPL" + timeStr[-3:] 	
		
newWOTemplate = "NWOT" + timeStr[-3:] 