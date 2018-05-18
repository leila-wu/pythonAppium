import os

from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys

from PageObject.BasePage import BasePage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeTest(ParametrizedTestCase):
    # 进入首页打开APP成功
    def testAHomeSwipeDown(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/HomeSwipeDown.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = BasePage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()
