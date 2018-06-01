import os
from time import sleep

import unittest
import re
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    @classmethod
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '2ea1c8b8'
        desired_caps['appPackage'] = 'com.thinkive.future.dev.standard'
        desired_caps['appActivity'] = 'com.thinkive.futureshl.activity.LauncherActivity'
        desired_caps['noReset'] = 'True'
        print('this is setUp')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    @classmethod
    def tearDown(self):
        # end the session
        print('this is tearDown')
        self.driver.quit()

    def test_demo1(self):
        el = self.driver.find_element_by_xpath('//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]')
        el.click()
        e2 = self.driver.find_elements_by_id('com.thinkive.future.dev.standard:id/item_alllistactivity_nameTv')
        e2[0].click()
        sleep(2)
        e2 = self.driver.find_element_by_id('com.thinkive.future.dev.standard:id/quntation_future_detial_wrap_more')
        e2.click()
        sleep(2)
        e2 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='设置']")
        e2.click()
        sleep(2)
        e2 = self.driver.find_element_by_id('com.thinkive.future.dev.standard:id/system_setting_parameter')
        e2.click()
        sleep(2)
        e2 = self.driver.find_element_by_xpath("//android.widget.TextView[@text='BOLL']")
        e2.click()
        sleep(2)
        e2 = self.driver.find_element_by_id('com.thinkive.future.dev.standard:id/et_paramater_three_value')
        e2.click()

        self.driver.tap([(600,1860)]);
        sleep(2)

        cmd = "adb -s  shell input tap " + x + " " + y
        os.system(cmd)
        self.driver.tap([(600,1460)]);
        sleep(2)
        sleep(10)
        self.assertIsNotNone(el)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
