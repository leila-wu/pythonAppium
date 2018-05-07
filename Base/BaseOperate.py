import re

import os

import appium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

__author__ = 'shikun'
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
from Base.BaseElementEnmu import Element as be
import time
import os

'''
# 此脚本主要用于查找元素是否存在，操作页面元素
'''


class OperateElement:
    def __init__(self, driver=""):
        self.driver = driver

    def findElement(self, mOperate):
        '''
        查找元素.mOperate,dict|list
        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            if type(mOperate) == list:  # 多检查点
                for item in mOperate:
                    if item.get("is_webview", "0") == 1:  # 1表示切换到webview
                        self.switchToWebview()
                    elif item.get("is_webview", "0") == 2:
                        self.switchToNative()
                    # if item.get("element_info", "0") == "0":  # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                    #     return {"result": True}
                    t = item["check_time"] if item.get("check_time", "0") != "0" else be.WAIT_TIME
                    WebDriverWait(self.driver, t).until(lambda x: self.elements_by(item))
                return {"result": True}
            if type(mOperate) == dict:  # 单检查点
                if mOperate.get("is_webview", "0") == 1 and self.switchToWebview() is False:  # 1表示切换到webview
                    print("切换到webview失败，请确定是否在webview页面")
                    return {"result": False, "webview": False}
                elif mOperate.get("is_webview", "0") == 2:
                    self.switchToNative()
                if mOperate.get("element_info", "0") == "0":  # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                    return {"result": True}
                t = mOperate["check_time"] if mOperate.get("check_time",
                                                           "0") != "0" else be.WAIT_TIME  # 如果自定义检测时间为空，就用默认的检测等待时间
                WebDriverWait(self.driver, t).until(
                    lambda x: self.elements_by(mOperate))  # 操作元素是否存在 elements_by封装的查找元素方法
                return {"result": True}
        except selenium.common.exceptions.TimeoutException:
            # print("查找元素" + mOperate["element_info"] + "超时")
            return {"result": False}
        except selenium.common.exceptions.NoSuchElementException:
            # print("查找元素" + mOperate["element_info"] + "不存在")
            return {"result": False}
        except selenium.common.exceptions.WebDriverException:
            print("WebDriver出现问题了")
            return {"result": False, "text": "selenium.common.exceptions.WebDriverException异常"}

    '''
    查找元素.mOperate是字典
    operate_type：对应的操作
    element_info：元素详情
    find_type: find类型
    testInfo: 用例介绍
    logTest: 记录日志
    device: 设备名
    '''

    def operate(self, mOperate, testInfo, logTest, device):
        res = self.findElement(mOperate)
        if res["result"]:
            return self.operate_by(mOperate, testInfo, logTest, device)
        else:
            return res

    def operate_by(self, mOperate, testInfo, logTest, device):
        try:
            info = mOperate.get("element_info", " ") + "_" + mOperate.get("operate_type", " ") + str(mOperate.get(
                "code", " ")) + mOperate.get("msg", " ")
            logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + info)  # 记录日志

            if mOperate.get("operate_type", "0") == "0":  # 如果没有此字段，说明没有相应操作，一般是检查点，直接判定为成功
                return {"result": True}
            elements = {
                be.SWIPE_DOWN: lambda: self.swipeToDown(),
                be.SWIPE_UP: lambda: self.swipeToUp(),
                be.CLICK: lambda: self.click(mOperate),
                be.GET_VALUE: lambda: self.get_value(mOperate),
                be.SET_VALUE: lambda: self.set_value(mOperate),
                be.ADB_TAP: lambda: self.adb_tap(mOperate, device),
                be.GET_CONTENT_DESC: lambda: self.get_content_desc(mOperate),
                be.PRESS_KEY_CODE: lambda: self.press_keycode(mOperate),
                be.GET_ATTR: lambda: self.get_attr(mOperate),
                be.SWIPE_LEFT: lambda: self.swipeLeft(mOperate),
                be.GET_VALUE_CHECK: lambda: self.get_value_check(mOperate),
            }
            return elements[mOperate.get("operate_type")]()
        except IndexError:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + mOperate["element_info"] + "索引错误")  # 记录日志
            print(mOperate["element_info"] + "索引错误")
            return {"result": False}

        except selenium.common.exceptions.NoSuchElementException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + mOperate[
                    "element_info"] + "页面元素不存在或没加载完成")  # 记录日志
            print(mOperate["element_info"] + "页面元素不存在或没有加载完成")

            return {"result": False}
        except selenium.common.exceptions.StaleElementReferenceException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + mOperate[
                    "element_info"] + "页面元素已经变化")  # 记录日志
            print(mOperate["element_info"] + "页面元素已经变化")
            return {"result": False}
        except KeyError:
            # 如果key不存在，一般都是在自定义的page页面去处理了，这里直接返回为真
            return {"result": True}

    # 获取到元素到坐标点击，主要解决浮动层遮档无法触发driver.click的问题
    def adb_tap(self, mOperate, device):

        bounds = self.elements_by(mOperate).location
        x = str(bounds["x"])
        y = str(bounds["y"])

        cmd = "adb -s " + device + " shell input tap " + x + " " + y
        print(cmd)
        os.system(cmd)

        return {"result": True}

    def toast(self, xpath, logTest, testInfo):
        logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + "查找弹窗元素_" + xpath)  # 记录日志
        try:
            WebDriverWait(self.driver, 10, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
            return {"result": True}
        except selenium.common.exceptions.TimeoutException:
            return {"result": False}
        except selenium.common.exceptions.NoSuchElementException:
            return {"result": False}

    # 点击事件
    def click(self, mOperate):
        # print(self.driver.page_source)
        if mOperate["find_type"] == be.find_element_by_id or mOperate["find_type"] == be.find_element_by_xpath:
            self.elements_by(mOperate).click()
        elif mOperate.get("find_type") == be.find_elements_by_id:
            self.elements_by(mOperate)[mOperate["index"]].click()
        return {"result": True}

    # code 事件
    def press_keycode(self, mOperate):
        self.driver.press_keycode(mOperate.get("code", 0))
        return {"result": True}

    def get_content_desc(self, mOperate):
        result = self.elements_by(mOperate).get_attribute("contentDescription")
        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}

    '''
    切换native
    
    '''

    def switchToNative(self):
        self.driver.switch_to.context("NATIVE_APP")  # 切换到native

    '''
    切换webview
    '''

    def switchToWebview(self):
        try:
            n = 1
            while n < 10:
                time.sleep(3)
                n = n + 1
                print(self.driver.contexts)
                for cons in self.driver.contexts:
                    if cons.lower().startswith("webview"):
                        self.driver.switch_to.context(cons)
                        # print(self.driver.page_source)
                        self.driver.execute_script('document.querySelectorAll("html")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("head")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("title")[0].style.display="block"')
                        print("切换webview成功")
                        return {"result": True}
            return {"result": False}
        except appium.common.exceptions.NoSuchContextException:
            print("切换webview失败")
            return {"result": False, "text": "appium.common.exceptions.NoSuchContextException异常"}

    # 左滑动
    def swipeLeft(self, mOperate):
        t = mOperate["check_time"] if mOperate.get("check_time",
                                                   "0") != "0" else be.WAIT_TIME  # 如果自定义检测时间为空，就用默认的检测等待时间
        element = WebDriverWait(self.driver, t).until(lambda x: self.elements_by(mOperate))
        start = element.location
        size1 = element.size
        y = start['y']
        x1 = start['x'] + size1["width"]
        x2 = size1["height"]
        self.driver.swipe(x1, y, x2, y, 600)
        print("--swipeLeft--")
        return {"result": True}

    # swipe start_x: 200, start_y: 200, end_x: 200, end_y: 400, duration: 2000 从200滑动到400
    def swipeToDown(self):
        height = self.driver.get_window_size()["height"]
        x1 = int(self.driver.get_window_size()["width"] * 0.5)
        y1 = int(height * 0.25)
        y2 = int(height * 0.75)

        self.driver.swipe(x1, y1, x1, y2, 1000)
        # self.driver.swipe(0, 1327, 500, 900, 1000)
        print("--swipeToDown--")
        return {"result": True}

    def swipeToUp(self):
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4)
        print("执行上拉")
        return {"result": True}
        # for i in range(n):
        #     self.driver.swipe(540, 800, 540, 560, 0)
        #     time.sleep(2)

    def swipeToRight(self):
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        x1 = int(width * 0.05)
        y1 = int(height * 0.5)
        x2 = int(width * 0.75)
        self.driver.swipe(x1, y1, x1, x2, 1000)
        # self.driver.swipe(0, 1327, 500, 900, 1000)
        print("--swipeToUp--")

    def set_value(self, mOperate):
        """
        输入值，代替过时的send_keys
        :param mOperate:
        :return:
        """
        self.elements_by(mOperate).send_keys(mOperate["msg"])
        return {"result": True}

    def get_attr(self, mOperate):
        """
        读取element的值,获取元素属性，判断属性与预期是否一致
        :param mOperate:
        :return:
        """
        attr_key = mOperate["attr_key"]
        attr_value = mOperate["attr_value"]
        if mOperate.get("find_type") == be.find_elements_by_id:
            element_info = self.elements_by(mOperate)[mOperate["index"]]
        else:
            element_info = self.elements_by(mOperate)

        if mOperate.get("is_webview", "0") == 1:
            result = element_info.text
        else:
            result = element_info.get_attribute(attr_key)

        if result == "true":
            re_result = 1
        else:
            re_result = 0

        if re_result == attr_value:
            print("参数校验成功")
            return {"result": True, "text": "".join("参数校验成功")}
        else:
            print("参数校验失败")
            return {"result": False, "text": "".join("参数校验失败")}

    def get_value(self, mOperate):
        """
        读取element的值,支持webview下获取值
        :param mOperate:
        :return:
        """
        resutl = ""
        if mOperate.get("find_type") == be.find_elements_by_id:
            element_info = self.elements_by(mOperate)[mOperate["index"]]
        else:
            element_info = self.elements_by(mOperate)

        if mOperate.get("is_webview", "0") == 1:
            result = element_info.text
        else:
            result = element_info.get_attribute("text")

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)

        return {"result": True, "text": "".join(re_reulst)}

    def get_value_check(self, mOperate):
        """
        获取元素的值判断元素存在
        """
        resutl = ""
        value =  mOperate["value"]
        if mOperate.get("find_type") == be.find_elements_by_id:
            element_info = self.elements_by(mOperate)[mOperate["index"]]
        else:
            element_info = self.elements_by(mOperate)

        if mOperate.get("is_webview", "0") == 1:
            result = element_info.text
        else:
            result = element_info.get_attribute("text")

        if value == result:
            return {"result": True, "text": "".join(value)}
        else:
            return {"result": False,"text":"".join("取值校验失败")}

    # 封装常用的标签
    def elements_by(self, mOperate):

        elements = {
            be.find_element_by_id: lambda: self.driver.find_element_by_id(mOperate["element_info"]),
            be.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(mOperate["element_info"]),
            be.find_element_by_css_selector: lambda: self.driver.find_element_by_css_selector(mOperate['element_info']),
            be.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(mOperate['element_info']),
            be.find_elements_by_id: lambda: self.driver.find_elements_by_id(mOperate['element_info']),

        }
        return elements[mOperate["find_type"]]()
