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
# width = driver.manage().window().getSize().width;
# height = driver.manage().window().getSize().height;

driver.find_element_by_xpath("//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]").click()
# driver.find_element_by_xpath("//android.widget.TextView[@text='大商所']").click()
time.sleep(2)
element = driver.find_element_by_xpath("//android.widget.TextView[@text='大商所']")
start = element.location
x = start['x']
y = start['y']

size1 = element.size

startx=size1["height"]
endx = size1["width"] + x
print("element的坐标x轴:"+str(x))
print("element的坐标x轴:"+str(y))
print("element尺寸的高:"+str(size1["width"]))
print("endx:"+str(endx)+",y:"+str(y)+" ,startx:"+str(startx)+" ,y:"+str(y))
driver.swipe(endx, y , startx, y)

time.sleep(10)


# el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ImageView")
# el1.click()
# driver.find_element_by_id("com.smartisanos.notes:id/new_note_button").click()
# time.sleep(5)
# driver.find_element_by_id("com.smartisanos.notes:id/list_rtf_view").send_keys('test')
# driver.find_element_by_id("com.smartisanos.notes:id/edit_done_button").click()

driver.quit()