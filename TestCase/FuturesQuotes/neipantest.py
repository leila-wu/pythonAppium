import os
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys

from PageObject.BasePage import BasePage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class NeiPanTest(ParametrizedTestCase):
    # 首页下拉
    def testAHomeSwipeDown(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/futures_quotes/zhuliangqing.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = BasePage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(NeiPanTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(NeiPanTest, cls).tearDownClass()
