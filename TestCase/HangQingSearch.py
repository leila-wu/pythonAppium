import os
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys
from PageObject.quntation_future_detial.FuturesQuotesQueryPage import FuturesQuotesQueryPage

from PageObject.BasePage import BasePage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HangQingSearch(ParametrizedTestCase):
    # 首次点击查询按钮
    def testAFirstSearch(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/search/FQfirstquery.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 通过选择查询
    def testBSearchForChose(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/search/SearchForChose.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = FuturesQuotesQueryPage(app)
        page.operate()
        page.checkPoint()

    # 点击查询结果
    def testBSearchForChose(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/search/SearchForChose.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = FuturesQuotesQueryPage(app)
        page.operate()
        page.checkPoint()

    # 输入字母查询合同，并且查看合同详情
    def testBSearchForChose(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/search/SearchTODetial.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = FuturesQuotesQueryPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(HangQingSearch, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HangQingSearch, cls).tearDownClass()
