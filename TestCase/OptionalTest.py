import os
from Base.BaseRunner import ParametrizedTestCase
import sys
from PageObject.BasePage import BasePage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OptionalTest(ParametrizedTestCase):
    # 进入自选页面
    def testAFirstOpenOptional(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/AFirstOpenOptional.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 点击+号添加自选
    def testBAddOptionalFirst(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/BAddOptionalFirst.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 通过搜索一次添加多个产品合同到自选
    def testCAddOptionalForSearch(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/CAddOptionalForSearch.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 通过搜索一次添加多个产品合同到自选
    def testDAddOptionalForSearch1(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/DAddOptionalForSearch1.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 通过产品详情加入自选
    def testEAddOptionalForDetial(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/EAddOptionalForDetial.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 自选列表超过十条记录，可向上滑动
    def testFAddOptionalForSwipe(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/FAddOptionalForSwipe.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 自选列表向左滑动
    def testGOptionalForLeftSwipe(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/GOptionalForLeftSwipe.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 编辑自选列表置顶操作
    def testHOptionalListTop(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/HOptionalListTop.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 从产品详情取消自选
    def testIDelOptionalForDetial(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/IDelOptionalForDetial.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 通过查询结果取消自选
    def testJDelOptionalForSearch(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/JDelOptionalForSearch.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 未选择记录删除
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

    # 通过编辑删除一条自选记录
    def testLDelOptionalForListOne(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/LDelOptionalForListOne.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BasePage(app)
        page.operate()
        page.checkPoint()

    # 通过编辑删除所有自选记录
    def testNDelOptionalForListAll(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/optional/NDelOptionalForListAll.yaml")
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
