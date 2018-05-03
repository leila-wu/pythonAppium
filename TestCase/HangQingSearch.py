import os
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys

from PageObject.BasePage import BasePage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HangQingSearch(ParametrizedTestCase):
    # 查看主页行情
    def testHangQingList(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/futures_quotes/zhuliangqing.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 查看夜盘行情
    def testYePan(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/futures_quotes/yepanhangqing.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(HangQingList, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HangQingList, cls).tearDownClass()
