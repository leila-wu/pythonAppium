import os
from Base.BaseRunner import ParametrizedTestCase
# from Base.BaseTestBase import *
import sys

from PageObject.BasePage import BasePage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class FutureList(ParametrizedTestCase):
    # 查看主页行情
    def testAFirstOpenFutureList(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/futures_quotes/FirstOpenFutureList.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 查看夜盘行情
    def testBYePan(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/futures_quotes/YepanFuture.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()
    # FutureListFilter

    # 过滤操作
    def testCFutureListFilter(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/futures_quotes/FutureListFilter.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 取消过滤操作
    def testDFutureListFilterAll(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/futures_quotes/FutureListFilterAll.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 验证+号通过导航栏切换
    def testEFutureListNavigaterBar(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/futures_quotes/EFutureListNavigaterBar.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(FutureList, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(FutureList, cls).tearDownClass()
