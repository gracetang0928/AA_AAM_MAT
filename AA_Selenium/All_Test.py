# -*- coding: utf-8 -*- 
import unittest
import HTMLTestRunner
import os,datetime,time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# creat MAT test suite

casesDir = ".\\cases"

def createSuite():
	testUnit = unittest.TestSuite()
	discoverCase = unittest.defaultTestLoader.discover(casesDir,pattern='MAT_*.py',top_level_dir=None)

	for suite in discoverCase:
		for case in suite:
			testUnit.addTests(case)
			print testUnit
	return testUnit



def sendReport(reportDir):
	sender ='lltang0928@163.com'
	receiver = 'lilantang0928@163.com'
	subject = 'python mail learn'
	smtpServer = 'smtp.163.com'
	username = 'lltang0928@163.com'
	password = 'tll657445'
	# Read report
	fr = open(reportDir,'rb') 
	content = fr.read()
	fr.close
	# identity email body
	msg = MIMEText(content,'html','utf-8')
	msg['Subject'] = Header(subject,'utf-8')
	msg['From'] = 'lltang0928@163.com'    
	msg['To'] = 'lilantang0928@163.com' 
	msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')

	smtp = smtplib.SMTP()
	smtp.connect(smtpServer)
	smtp.login(username, password)
	smtp.sendmail(sender,receiver,msg.as_string())
	smtp.quit()




now = datetime.datetime.now().strftime("%m-%d-%H-%M-%S")
reportName = '.\\report\\AAMTest'+now+'.html'




MAT_case = createSuite()

fp = file(reportName,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "AAM MAT Test Results" , description = "Case Execute Results")

runner.run(MAT_case)
sendReport(reportName)