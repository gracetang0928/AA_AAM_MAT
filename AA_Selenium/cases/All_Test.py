# -*- coding: utf-8 -*- 
import unittest

import MAT_Admin
import MAT_Assets
import MAT_AssetsCA
import MAT_Costing
import MAT_PartInventory
import MAT_PMSchedule
import MAT_TimeAccounting

testUnit = unittest.TestSuite()



suiteList = (MAT_Admin.AdminTest,MAT_Assets.AssetManageTest,MAT_AssetsCA.AssetCATest,MAT_Costing.CostingTest,MAT_PartInventory.PartTest,MAT_PMSchedule.PMScheduleTest,MAT_TimeAccounting.TimeAccountingTest)

testUnit.addTest(unittest.makeSuite(MAT_Assets.AssetManageTest))
testUnit.addTest(unittest.makeSuite(MAT_Costing.CostingTest))
testUnit.addTest(unittest.makeSuite(MAT_AssetsCA.AssetCATest))
testUnit.addTest(unittest.makeSuite(MAT_PartInventory.PartTest))
testUnit.addTest(unittest.makeSuite(MAT_PMSchedule.PMScheduleTest))
testUnit.addTest(unittest.makeSuite(MAT_TimeAccounting.TimeAccountingTest))

runner = unittest.TextTestRunner()
runner.run(testUnit)