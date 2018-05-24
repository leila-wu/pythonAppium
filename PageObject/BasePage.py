from PageObject import Pages
from Base.BaseYaml import getYam


class BasePage:

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYam(kwargs["path"]), "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    def operate(self):
        self.page.operate()

    def checkPoint(self):
        self.page.checkPoint()
