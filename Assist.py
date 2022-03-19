#!/usr/local/bin/python
# -*-coding:UTF-8-*-
# -*-coding:cp936-*-
import tkinter as tk
import json
import time
import tkinter.messagebox
from pymouse import PyMouse
import sys
import datetime
import logging

mouse = PyMouse()
import requests
import psutil
import os
import re
import subprocess
from subprocess import *

logger = logging.getLogger(__name__)


def Record_logger(filename="/Users/gdlocal/Documents/Assist_log.txt", level=logging.INFO, console_swtich=True):
    # logger = logging.getLogger(__name__)
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s[line:%(lineno)d][%(funcName)s] - %(levelname)s - %(message)s")
    file_handler = logging.FileHandler(filename)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    if console_swtich:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter
        logger.addHandler(console_handler)
        # 指定日志的最低输出级别，默认为warn级别
        logger.setLevel(level)
        return logger


def check_running():
    ########only one open######
    count = 0
    pid_list = psutil.pids()
    for pid in pid_list:
        p = psutil.Process(pid)
        if p.name() == "Assist":
            count += 1
        if count >= 3:
            tk.messagebox.showerror(title='Error', message='Do not repeat open the program! Thank you very much！')
            sys.exit()


def check_starttime():
    start_systime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    start_time.set("Last Mini restart time：" + start_systime)


def open_atlas():
    openApp = '''
    tell application "Hyperion"
        activate
        tell application "System Events"
            tell process "Hyperion"
                #tell window1
                entire contents
            end tell
        end tell
    end tell
    # delay=0.1
    # do shell script "killall System\\ Events"
    '''
    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(openApp)
    # print(p.returncode, stdout, stderr)
    status = p.returncode
    # print(status)
    return status


def click_L():
    script_click_L = '''
    tell application "Hyperion" to activate
    tell application "System Events"
        tell process "Hyperion"
            tell window 1
                entire contents
                ignoring application responses
                click button "L" of window 1 of application process "Hyperion" of application "System Events"
                end ignoring
                delay(0.1)
            end tell
        end tell
    end tell
    # do shell script "killall System\\ Events"
    delay 0.1
    '''
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script_click_L)
    # print(p.returncode, stdout, stderr)
    status = p.returncode
    return status


def click_R():
    script_click_R = '''
    tell application "Hyperion" to activate
    tell application "System Events"
        tell process "Hyperion"
            tell window 1
                entire contents
                ignoring application responses
                click button "R" of window 1 of application process "Hyperion" of application "System Events"
                end ignoring
                delay(0.1)
            end tell
        end tell
    end tell
    # do shell script "killall System\\ Events"
    delay 0.1
    '''
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script_click_R)
    # print(p.returncode, stdout, stderr)
    status = p.returncode
    # print(status)
    return status


def click_R_panelID():
    script_click_R_PanelID = '''
    tell application "Hyperion" to activate
    tell application "System Events"
        tell process "Hyperion"
            tell window 1
                entire contents
                ignoring application responses
                click text field 2 of group 5 of group 1 of pop over 1 of window 1 of application process "Hyperion" of application "System Events"
                end ignoring
                delay(0.1)
            end tell
        end tell
    end tell
    # do shell script "killall System\\ Events"
    # delay 0.1
    '''
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script_click_R_PanelID)
    # print(p.returncode, stdout, stderr)
    status = p.returncode
    # print(status)
    return status


def click_L_panelID():
    script_click_L_PanelID = '''
    tell application "Hyperion" to activate
    tell application "System Events"
        tell process "Hyperion"
            tell window 1
                entire contents
                # ignoring application responses
                click text field 2 of group 5 of group 1 of pop over 1 of window 1 of application process "Hyperion" of application "System Events"
                # end ignoring
                delay(0.1)
            end tell
        end tell
    end tell
    # do shell script "killall System\\ Events"
    # delay 0.1
    '''
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script_click_L_PanelID)
    # print(p.returncode, stdout, stderr)
    status = p.returncode
    # print(status)
    return status


def scan_status_R():
    script_scan = '''
    tell application "System Events"
        tell process "Hyperion"
            tell window 1
                tell scroll area 2
                    # ignoring application responses
                    click static text "Unit Scanning (Fixture 2)" of pop over 1 of window 1 of application process "Hyperion" of application "System Events"
                    # end ignoring
                end tell
            end tell
        end tell
    end tell
    # do shell script "killall System\\ Events"
    # delay 0.1
    '''
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script_scan)
    # status = len(stderr)
    # print(p.returncode, stdout, stderr)
    status = p.returncode
    # print(status)
    return status


def scan_status_L():
    script_scan = '''
    tell application "System Events"
        tell process "Hyperion"
            tell window 1
                tell scroll area 2
                    # ignoring application responses
                    click static text "Unit Scanning (Fixture 1)" of pop over 1 of window 1 of application process "Hyperion" of application "System Events"
                    # end ignoring
                end tell
            end tell
        end tell
    end tell
    # do shell script "killall System\\ Events"
    # delay 0.1
    '''
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script_scan)
    # status = len(stderr)
    # print(p.returncode, stdout, stderr)
    status = p.returncode
    # print(status)
    return status


def click_assist():
    script_click_assist = '''
    tell application "Assist" to activate
    tell application "System Events"
	    tell process "Assist"
		    #tell window 1
		    entire contents
		    delay (0.1)
	    end tell
    end tell
    # do shell script "killall System\\ Events"
    delay 0.1
        '''
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    stdout, stderr = p.communicate(script_click_assist)
    # print(p.returncode, stdout, stderr)
    status = p.returncode
    # print(status)
    return status


####获取窗口位置并点击#######
def get():
    x = root.winfo_x()
    y = root.winfo_y()
    mouse.click(x, y)


def got_l_status():
    t_endl = time.time() + 8
    while time.time() < t_endl:
        status = scan_status_L()
        if status == 0:
            # input_barcode.config(stage='readonly')
            # click_L_panelID()
            time.sleep(1)
        else:
            # input_barcode.config(stage='normal')
            inputcode.set("")
            time.sleep(0.1)
            get()
            time.sleep(0.1)
            get()
            time.sleep(0.1)
            get()
            break
    else:
        click_L()
        # input_barcode.config(stage='normal')
        # time.sleep(0.2)
        # get()
        time.sleep(0.1)
        inputcode.set("")
        # time.sleep(0.1)
        get()


def got_r_status():
    t_endr = time.time() + 8
    while time.time() < t_endr:
        status = scan_status_R()
        if status == 0:
            # click_R_panelID()
            # input_barcode.config(stage='readonly')
            time.sleep(1)
        else:
            # input_barcode.config(stage='normal')
            inputcode.set("")
            time.sleep(0.1)
            get()
            time.sleep(0.1)
            get()
            time.sleep(0.1)
            get()
            break
    else:
        click_R()
        # input_barcode.config(stage='normal')
        # time.sleep(0.2)
        # get()
        time.sleep(0.1)
        inputcode.set("")
        # time.sleep(0.1)
        get()


####从json档抓stationID#####
def read_json():
    with open("/vault/data_collection/test_station_config/gh_station_info.json", encoding="utf-8", ) as f:  # 打开json档
        # with open("./gh_station_info.json", 'r') as f:  # open json
        jdata = json.loads(f.read())  # load json
        # print(jdata)
        jstationID = jdata["ghinfo"]["STATION_NUMBER"]  # get stationID
        if len(jstationID) == 1:
            jstationID = "0" + jstationID
            # print(jstationID)
        # print(jstationID)
        logger.info(f"json file station ID is :{jstationID}")
        return jstationID


#####GET station A/B from scaned barcode
def sanvalue():
    # input_barcode.set("")
    scancode = input_barcode.get()
    codelen = len(scancode)
    # print(codelen)
    StationID = str(scancode[0:2])
    # print("stationid is " + StationID)
    Fixturesite = str(scancode[2])
    # print("属于治具" + Fixturesite)
    logger.info(f"Scanded  station ID is :{StationID}")
    logger.info(f"Scanded  Fixture site  is :{Fixturesite}")
    logger.info(f"Scanded  code len  is :{codelen}")
    return StationID, Fixturesite, codelen


#####SFCS UOP check######
class SFC_Query():
    def __init__(self):
        self.url = '{}?test_head_id=&p=unit_process_check&c=QUERY_RECORD&sw_version=&tsid={}&sn={}&fixture_id=&'

    def get_url(self,SN):
        dict = {}
        with open("/vault/data_collection/test_station_config/gh_station_info.json", 'r') as f:
        # with open("/Users/mage/Desktop/gh_station_info.json", 'r') as f:
            content = f.read()
            dict = json.loads(content)
        SFC_URL = dict["ghinfo"]["SFC_URL"]
        Site = dict["ghinfo"]["SITE"]
        Line_id = dict["ghinfo"]["LINE_ID"]
        Station_name = dict["ghinfo"]["STATION_TYPE"]
        Station_Number = dict["ghinfo"]["STATION_NUMBER"]
        TSID = Site + "_" + Line_id + "_" + Station_Number + "_" + Station_name
        sn = SN
        print("MLBSN:", sn)
        new_url = self.url.format(SFC_URL, TSID, sn)
        # print(new_url)
        return new_url

    def get_data(self, url):
        response = requests.get(url)
        response_data = response.content.decode()
        # print("1#response_data：",response_data)
        return response_data


def Uop_check(MLB_SN):
    SN=MLB_SN
    sfc_query = SFC_Query()
    # sfc_query.run(SN)
    url = sfc_query.get_url(SN)
    res = sfc_query.get_data(url)
    # print("3#",res)
    result = ""
    try:
        if re.findall(r"unit_process_check=OK", res, re.I):
            result = str(SN+":"+"当站流程正常,请继续测试")
            # print(result)
            logger.info(f"{SN} check Uop info:{result}")
            uop_info.set(result)
            # MLBSN.set("")
            # top.config(bg='green')
        else:
            err_info = re.search(r"UNIT OUT OF PROCESS(.*)", res)
            # print("错误信息：", err_info)
            err_code = err_info.groups()[0] if err_info else ""
            # print("错误代码：", err_code)
            result = (SN+":"+"当站流程错误，请确认流程！\r\n" + err_code)
            # print(result)
            uop_info.set(result)
            tk.messagebox.showerror(title='Error', message=result)
            logger.info(f"{SN} check Uop info:{result}")
            # top.config(bg='orange')
            # MLBSN.set("")
    except:
        result = res.replace('\n', ' ')
        # print(result)
    logger.info(f"{SN} check Uop info:{result}")
    uop_info.set(result)
    # MLBSN.set("")


#####get panel ID from atlas log#######
def show_panelid():
    # atlas_log = open("/vault/Atlas/atlas.log", "rb")
    logname = "/vault/Atlas/atlas.log"
    data = os.popen("tail -b 2048 %s" % logname).read()  ###这里是个巨坑，试了N种方法，终于一次抓1M log 才把R的panelid data 包进来。
    # data = atlas_log.read()
    # print("First data:", "@" * 50, data)
    lastscan = data.rfind("updated contents of _barcodeInfo [{")  ###find last [{ string in data
    # print("last scan", "@" * 50, lastscan)
    data = data[lastscan:]  ###cut last scan code output
    # print("second-data", "*" * 50, data)
    # atlas_log.close()
    #### find the panelID from last output
    SN_L_Str = re.search(r"0 =     \{\n.*PanelID = (.+);", data)
    SN_R_Str = re.search(r"1 =     \{\n.*PanelID = (.+);", data)
    # print("SN_L_Str:", "&" * 50, SN_L_Str)
    # print("SN_R_Str:", "&" * 50, SN_R_Str)
    ####find the string and set the value,
    SN_L = SN_L_Str.groups()[0] if SN_L_Str else ""
    SN_R = SN_R_Str.groups()[0] if SN_R_Str else ""
    logger.info(f"Scanded left PanelID  is :{SN_L}")
    logger.info(f"Scanded right panelID  is :{SN_R}")
    # print(SN_L, SN_R)
    if SN_L != SN_R:
        L_ID_status = SN_L.startswith("H")
        R_ID_status = SN_R.startswith("H")
        # print(L_ID_status, R_ID_status)
        if L_ID_status == True:
            ID_A_lable.config(fg='blue')
            Panel_ID_A.set("L: " + SN_L)
            Uop_check(SN_L)
        else:
            msg.set("左边未扫板边码或板边码错误，请重新刷入")
            logger.info(f"L_ID_Status: Left site panelID not been input  or barcode error")
            tips.config(fg="red")
            ID_A_lable.config(fg="red")
            Panel_ID_A.set("L: " + SN_L)

        if R_ID_status == True:
            ID_B_lable.config(fg="blue")
            Panel_ID_B.set("R: " + SN_R)
            Uop_check(SN_R)
        else:
            msg.set("右边未扫板边码或板边码错误，请重新刷入！")
            logger.info(f"R_ID_status: Right site panelID not been input or panelID code error")
            tips.config(fg="red")
            ID_B_lable.config(fg="red")
            Panel_ID_B.set("R: " + SN_R)
    else:
        # tips.config("blue")
        msg.set("L和R PanelID重复，请确认后重新输入")
        tips.config(fg="red")
        ID_A_lable.config(fg="red")
        ID_B_lable.config(fg="red")
        Panel_ID_A.set("L: " + SN_L)
        Panel_ID_B.set("R: " + SN_R)
        logger.info(f"left panel ID{SN_L} == right panel ID{SN_R}，Code L is same as R,please check again！")
    return SN_L, SN_R


###主逻辑判断##########
def main(event):
    # check_starttime()
    # starttime = check_starttime()[0]
    Record_logger(level=logging.INFO)
    logger.info(f"Start used PreDFU Assist tool v2.8：")
    msg.set('欢迎使用立臻DFU扫码辅助工具！')
    tips.config(fg="blue")
    #####复制json档到Documents
    jstationID = read_json()
    # print("json档stationID:", jstationID)
    StationID = str(sanvalue()[0])
    # print("扫描stationID：", StationID)
    Fixturesite = str(sanvalue()[1])
    # print("左右治具：", Fixturesite)
    codelen = sanvalue()[2]
    # print("扫描码长度：", codelen)
    if codelen != 3:
        msg.set("条码长度不符，请重新输入！")
        logger.info(f"fixture barcode len is {codelen}，barcode len is out of order,please check again. ")
        tips.config(fg="red")
        inputcode.set("")
    elif StationID != jstationID:
        msg.set("扫描站别编号与系统不符，请确认后重新扫描！")
        logger.info(
            f"StationID:{StationID},json stationID:{jstationID}.Fmixture code stationID is different with System stationID, please check!")
        tips.config(fg="red")
        inputcode.set("")
        # click_assist()
    else:
        if Fixturesite == "L":
            logger.info(f"Fixturesite=={Fixturesite}")
            # print("L")
            click_L()
            # print("点击L完成")
            time.sleep(0.1)
            got_l_status()
            time.sleep(0.2)
            show_panelid()
            # l_panel = show_panelid()[0]
            # Panel_ID_A.set("L: " + l_panel)
            # ID_A_lable.config(fg="blue")

        elif Fixturesite == "R":
            # print("R")
            logger.info(f"Fixturesite=={Fixturesite}")
            click_R()
            time.sleep(0.1)
            got_r_status()
            time.sleep(0.2)
            show_panelid()
            # r_panel = show_panelid()[1]
            # Panel_ID_B.set("R: " + r_panel)
            # ID_B_lable.config(fg="blue")
        else:
            msg.set("治具L/R码不正确，请重新输入！")
            logger.info(f"Fixture L or R code is  not correct.please rescan please！")
            tips.config(fg="red")
            inputcode.set("")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("PreDFU Assist tool(v4.3)")
    root.geometry('400x200+500+20')
    root.resizable(0,0)  # 设置窗体大小固定
    root.configure(bg="#F5F5F5")
    msg = tk.StringVar()
    msgerr = tk.StringVar()
    inputcode = tk.StringVar()
    Panel_ID_A = tk.StringVar()
    Panel_ID_B = tk.StringVar()
    start_time = tk.StringVar()
    uop_info = tk.StringVar()
    # loglabel=tk.Label(root,text="LuxsanDFU扫码辅助工具",fg='Blue',bg="#F5F5F5").grid(row=1)
    Fixturecodelabel = tk.Label(root, text="请扫入治具载板上二维码", fg='blue', bg='#F5F5F5', width=20, height=2)
    Fixturecodelabel.grid(row=1, column=1)
    input_barcode = tk.Entry(root, textvariable=inputcode, fg='blue', bg='#FFFF00', width=18)
    input_barcode.grid(row=1, column=2)
    # loglabel=tk.Label(root,text="Luxsan",font=('Arial', 20),fg="green",bg="#F5F5F5",width=3)
    # loglabel.grid(row=2,column=1)
    ID_A_lable = tk.Label(root, textvariable=Panel_ID_A, bg="#F5F5F5", width=40)
    ID_A_lable.grid(row=2, column=1, columnspan=2)
    ID_B_lable = tk.Label(root, textvariable=Panel_ID_B, bg="#F5F5F5", width=40)
    ID_B_lable.grid(row=3, column=1, columnspan=2)
    tips = tk.Label(root, textvariable=msg, bg='#F5F5F5', width=40)
    tips.grid(row=4, column=1, columnspan=2)
    tips.config(fg="blue")
    msg.set('欢迎使用立臻DFU扫码辅助工具！')
    uop_tips = tk.Label(root, textvariable=uop_info, bg='#F5F5F5', width=40)
    uop_tips.grid(row=5, column=1, columnspan=2)
    uop_tips.config(fg='blue')
    starttime = tk.Label(root, textvariable=start_time, bg='#F5F5F5', width=40)
    starttime.grid(row=7, column=1, columnspan=2)
    starttime.config(fg='blue')
    root.attributes('-topmost', True)  ##窗口置顶
    check_running()  ###检测程式是否已打开
    check_starttime()  ###显示系统上次重启时间
    open_atlas()  ###开机打开atlas
    input_barcode.bind("<Return>", main)  # 刷完条码回车触发主逻辑函数
    root.mainloop()
########change list#######
# 2.4 添加了log记录功能和L和R panelID相同时提醒功能
# 2.5 修复了log记录功能无法生成问题
##2.6 修复PanelID左右相同时不能提示问题
##2.7 修复左右panel id相同时不能秀红色和显示问题
# 2.8 修复右通道不能显示问题
# 3.0 增加最后系统开机时间，增加不可多开功能，
# 4.3 增加完善了Panel ID SFCS 流程check 功能
