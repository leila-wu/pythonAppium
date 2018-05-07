#coding=utf-8

from appium import webdriver
import os
import re
import time

# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())
# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径
desired_caps={}
#使用的移动平台
desired_caps['platformName']='Android'
#指定平台的版本
desired_caps['platformVersion']=deviceVersion
#设备名称
desired_caps['deviceName']=deviceId
#待测试的app的Java package  from appium import webdriver
desired_caps['appPackage']= 'com.thinkive.future.dev.standard'
#待测试的app的Activity名字 '.NotesActivity'
desired_caps['appActivity']= 'com.thinkive.futureshl.activity.LauncherActivity'
# desired_caps['noReset'] = True
# desired_caps['autoAcceptAlerts'] = Ture
# desired_caps['app'] = apk_path + '\\app\\test.apk'
#automationName 使用哪种自动化引擎。appium（默认）还是Selendroid。

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(10)

driver.find_element_by_xpath("//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]").click()
time.sleep(3)
driver.find_element_by_id("com.thinkive.future.dev.standard:id/iv_quotation_futures_search").click()
a = driver.find_element_by_xpath("//*[contains(@class,'android.support.v7.app.ActionBar$Tab')][1]/android.widget.TextView").get_attribute('text')
print(a)

# driver.find_element_by_id("com.thinkive.future.dev.standard:id/search_edittext").send_keys("")

time.sleep(2)


time.sleep(10)
driver.quit()