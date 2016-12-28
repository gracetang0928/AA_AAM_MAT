# -*- coding: utf-8 -*- 
import unittest
import HTMLTestRunner
import os,datetime


casesDir = ".\\cases"

def createSuite():
	testUnit = unittest.TestSuite()
	discoverCase = unittest.defaultTestLoader.discover(casesDir,pattern='MAT_*.py',top_level_dir=None)

	for suite in discoverCase:
		for case in suite:
			testUnit.addTests(case)
			print testUnit
	return testUnit


MAT_case = createSuite()
now = datetime.datetime.now().strftime("%m-%d-%H-%M-%S")


reportName = '.\\report\\AAMTest'+now+'.html'

fp = file(reportName,'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp , title = "AAM MAT Test Results" , description = "Case Execute Results")

runner.run(testUnit)