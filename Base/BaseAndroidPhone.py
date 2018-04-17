
# -*- coding: utf-8 -*-
__author__ = 'shikun'
import os
import re
import math
from math import ceil
import subprocess

def getPhoneInfo(devices):
    """得到手机信息

    :param devices:
    :return:
    """
    # adb -s 指定手机，执行shell命令
    cmd = "adb -s " + devices +" shell cat /system/build.prop "
    print(cmd)
    # phone_info = os.popen(cmd).readlines()
    phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    result = {"release": "5.0", "model": "model2", "brand": "brand1", "device": "device1"}
    # 版本
    release = "ro.build.version.release="
    # 型号
    model = "ro.product.model="
    # 品牌
    brand = "ro.product.brand="
    # 设备名
    device = "ro.product.device="
    for line in phone_info:
         # 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
         for i in line.split():
            #  格式转码，将str转换成unicode
            temp = i.decode()
            if temp.find(release) >= 0:
                # 字符串切片的应用
                result["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                result["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                result["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                result["device"] = temp[len(device) :]
                break
    print(result)
    return result

# 得到最大运行内存
def get_men_total(devices):
    cmd = "adb -s "+devices+ " shell cat /proc/meminfo"
    get_cmd = os.popen(cmd).readlines()
    men_total = 0
    men_total_str = "MemTotal"
    for line in get_cmd:
        if line.find(men_total_str) >= 0:
            men_total = line[len(men_total_str) +1:].replace("kB", "").strip()
            break
    return int(men_total)
# 得到几核cpu
def get_cpu_kel(devices):
    cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
    get_cmd = os.popen(cmd).readlines()
    find_str = "processor"
    int_cpu = 0
    for line in get_cmd:
        if line.find(find_str) >= 0:
            int_cpu += 1
    return str(int_cpu) + "核"

# 得到手机分辨率
def get_app_pix(devices):
    result = os.popen("adb -s " + devices+ " shell wm size", "r")
    return result.readline().split("Physical size:")[1]

if __name__=="__main__":
    getPhoneInfo("DU2TAN15AJ049163")
