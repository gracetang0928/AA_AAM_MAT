# -*- coding: utf-8 -*-
import os
caselist = os.listdir("C:\\Users\\grace.tang\\Desktop\\ps\\AAversionPage\\cases")
for case in caselist :
	s=case.split('.')[1]
	if s=='py':
		os.system("C:\\Users\\grace.tang\\Desktop\\ps\\AAversionPage\\cases\\%s 1>>log.txt 2>&1"%case)