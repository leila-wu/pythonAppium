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
desired_caps['appPackage']= 'com.zxjt.jjt'
#待测试的app的Activity名字 '.NotesActivity'
desired_caps['appActivity']= 'com.thinkive.android.invest_app.ui.activities.LauncherActivity'
# desired_caps['noReset'] = True
# desired_caps['autoAcceptAlerts'] = Ture
desired_caps['app'] = apk_path + '\\app\\test.apk'
#automationName 使用哪种自动化引擎。appium（默认）还是Selendroid。

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(2)
# width = driver.manage().window().getSize().width;
# height = driver.manage().window().getSize().height;

widht = driver.get_window_size()['width']
height = driver.get_window_size()['height']
for i in range(1,4):
    time.sleep(2)
    driver.swipe(int(widht * 6 / 7), int(height / 2), int(widht / 7), int(height / 2), 1000);

time.sleep(2)
driver.find_element_by_id("com.zxjt.jjt:id/btn_start").click()

# el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ImageView")
# el1.click()
time.sleep(2)
# driver.find_element_by_id("com.smartisanos.notes:id/new_note_button").click()
# time.sleep(5)
# driver.find_element_by_id("com.smartisanos.notes:id/list_rtf_view").send_keys('test')
# driver.find_element_by_id("com.smartisanos.notes:id/edit_done_button").click()

driver.quit()