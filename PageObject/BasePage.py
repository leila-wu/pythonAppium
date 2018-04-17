from PageObject import Pages

class BasePage:

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"], "launch_app": 1,
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    def operate(self):
        self.page.operate()

    def checkPoint(self):
        self.page.checkPoint()