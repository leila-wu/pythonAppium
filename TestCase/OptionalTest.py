import os
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys
from PageObject.BasePage import BasePage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OptionalTest(ParametrizedTestCase):
    # 进入自选页面
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

    # 首次点击查询按钮，检查查询列表空
    def testBAddOptionalFirstself(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/AddOptionalFirst.yaml")
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
