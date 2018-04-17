# coding=utf-8
import unittest, os, re, time

from appium import webdriver


class Test(unittest.TestCase):

    def setUp(self):
        # 读取设备 id
        readDeviceId = list(os.popen('adb devices').readlines())
        # 正则表达式匹配出 id 信息
        deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
        # 读取设备系统版本号
        deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
        deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
        apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径

        desired_caps = {}
        # 使用的移动平台
        desired_caps['platformName'] = 'Android'
        # 指定平台的版本
        desired_caps['platformVersion'] = deviceVersion
        # 设备名称
        desired_caps['deviceName'] = deviceId
        desired_caps['app'] = apk_path + '\\app\\test.apk'
        desired_caps['noReset'] = True
        desired_caps['appPackage'] = 'com.zxjt.jjt'
        # 待测试的app的Activity名字
        desired_caps['appActivity'] = 'com.thinkive.android.invest_app.ui.activities.LauncherActivity'

        # desired_caps['autoAcceptAlerts'] = Ture
        # automationName 使用哪种自动化引擎。appium（默认）还是Selendroid。

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # def setUpClass(self):


    def tearDown(self):
        self.driver.quit()

    # def tearDownClass(self):



    def testSwrit(self):
        widht = self.driver.manage().window().getSize().width;
        height = self.driver.manage().window().getSize().height;
        for i in range(1,4):
            self.driver.swipe(widht * 6 / 7, height / 2, widht / 7, height / 2, 1000);
        # self.driver.swipe(800, 800, 200, 800, 1000)

if __name__=="__mian__":
    suite = unittest.TestSuite()
    suite.addTest("testSwrit")
    unittest.TextTestRunner.run(suit)