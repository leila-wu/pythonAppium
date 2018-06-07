import os

from Base.BaseRunner import ParametrizedTestCase
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
        app["path"] = PATH("../yaml/home/AHomeSwipeDown.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # # 未选择记录删除
    # def testKDelOptionalForListNone(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/optional/KDelOptionalForListNone.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = BasePage(app)
    #     page.operate()
    #     page.checkPoint()

    # 通过编辑删除所有自选记录
    # def testRDetaillMoreSettingZTCSXGFirst(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/detail/RDetaillMoreSettingZTCSXGFirst.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = BasePage(app)
    #     page.operate()
    #     page.checkPoint()

        # 修改默认设置
    # def testOFDetaillMoreSettingYP(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/detail/OFDetaillMoreSettingYP.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = BasePage(app)
    #     page.operate()
    #     page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()
