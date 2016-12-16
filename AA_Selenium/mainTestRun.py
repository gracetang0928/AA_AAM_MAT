# -*- coding: utf-8 -*-
import os
caselist = os.listdir("C:\\Users\\grace.tang\\Desktop\\ps\\AA_Selenium\\cases")
print caselist
for case in caselist :
	if case.startswith('T'):
		s=case.split('.')[1]
		if s=='py':
			os.system("C:\\Users\\grace.tang\\Desktop\\ps\\AA_Selenium\\cases\\%s 1>>log.txt 2>&1"%case)