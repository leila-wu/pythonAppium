import os
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys
from PageObject.BasePage import BasePage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OptionalTest(ParametrizedTestCase):
    # # 进入自选页面
    # def testAFirstOpenOptional(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/optional/FirstOpenOptional.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = BasePage(app)
    #     page.operate()
    #     page.checkPoint()
    #
    # # # 点击+号添加自选
    # def testBAddOptionalFirst(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/optional/AddOptionalFirst.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = BasePage(app)
    #     page.operate()
    #     page.checkPoint()
    #
    # # 通过查询添加多个产品到自选
    # def testBAddOptionalForSearch(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/optional/AddOptionalForSearch.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = BasePage(app)
    #     page.operate()
    #     page.checkPoint()
    #
    # # # 通过查询添加多个产品到自选
    # def testBAddOptionalForSearch2(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/optional/AddOptionalForSearch2.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = BasePage(app)
    #     page.operate()
    #     page.checkPoint()
    #
    # # 通过产品详情加入自选
    # def testBAddOptionalForDetial(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/optional/AddOptionalForDetial.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = BasePage(app)
    #     page.operate()
    #     page.checkPoint()

    # 自选列表滑动
    def testBAddOptionalForSwipe(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/AddOptionalForSwipe.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(OptionalTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(OptionalTest, cls).tearDownClass()
