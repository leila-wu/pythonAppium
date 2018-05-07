# -*- coding: utf-8 -*-
from TestCase.HangQingSearch import HangQingSearch
from TestCase.HangQingList import HangQingList
import sys
import platform
from Base.BaseAndroidPhone import *
from Base.BaseAdb import *
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from Base.BaseInit import mk_file, init
from Base.BaseStatistics import countDate, writeExcel
from Base.BasePickle import *
from datetime import datetime

from TestCase.HomeTest import HomeTest

sys.path.append("..")
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def kill_adb():
    """停止adb服务并重启
     windows通过编写执行bat文件停止adb进程，使用的是taskkill
     其他操作系统（linux mac）使用killall命令停止进程
     adb start-server 启动adb服务，windows与Linux,mac处理一致"
    :return:
    """
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system(PATH("../app/kill.bat"))
    else:
        os.popen("killall adb")
    os.system("adb start-server")




def runnerPool(getDevices):
    """通过设备Id获取设备其他信息，启动多进程。有多少个设备启动多少个进程
    :param getDevices:  设备列表  判断有多少个设备，每个设备分别加载app信息
    :return:
    """
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        print("----runnerPool------")
        print(getDevices[i])
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        # _initApp["platformVersion"] = "6.0"
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        _initApp["appPackage"] = "com.thinkive.future.dev.standard"
        _initApp["appActivity"] = "com.thinkive.futureshl.activity.LauncherActivity"
        # _initApp["automationName"] = "uiautomator2"
        _initApp["automationName"] ="Appium"
        _initApp["systemPort"] = getDevices[i]["systemPort"]
        # _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        # _initApp["appActivity"] = apkInfo.getApkActivity()
        # _initApp["app"] = getDevices[i]["app"]
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    # suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(HangQingList, param=devices))
    suite.addTest(ParametrizedTestCase.parametrize(HangQingSearch, param=devices))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")


if __name__ == '__main__':

    kill_adb()

    # 获取设备列表
    devicess = AndroidDebugBridge().attached_devices()
    if len(devicess) > 0:
        mk_file()
        l_devices = []
        for dev in devicess:
            app = {}
            app["devices"] = dev
            # init(dev)
            app["port"] = str(random.randint(4700, 4900))
            app["bport"] = str(random.randint(4700, 4900))
            app["systemPort"] = str(random.randint(4700, 4900))
            l_devices.append(app)

        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runnerPool(l_devices)
        print('runnerPool(l_devices)')
        writeExcel()
        print('writeExcel()')
        appium_server.stop_server(l_devices)
    else:
        print("没有可用的安卓设备")
