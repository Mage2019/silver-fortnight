#!/usr/local/bin/python
# -*-coding:UTF-8-*-
# -*-coding:cp936-*-
import tkinter as tk
import sys
from tkinter import *
from tkinter import ttk
import logging
import re
import requests
import json
import tkinter.messagebox

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


class SFC_Query():
    def __init__(self):
        self.url = '{}?test_head_id=&p=unit_process_check&c=QUERY_RECORD&sw_version=&tsid={}&sn={}&fixture_id=&'

    def get_url(self, SN):
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

    # def run(self, MLB_SN):
    #     SN = MLB_SN
    #     url = self.get_url(SN)
    #     self.get_data(url)
    # respon=self.get_data(url)
    # print("2#:",respon)


def Uop_check(MLB_SN):
    SN = MLB_SN
    sfc_query = SFC_Query()
    # sfc_query.run(SN)
    url = sfc_query.get_url(SN)
    res = sfc_query.get_data(url)
    # print("3#",res)
    result = ""
    try:
        if re.findall(r"unit_process_check=OK", res, re.I):
            result = str(SN + ":\r\n" + "DFU流程正常,请继续测试")
            print(result)
            logger.info(f"{SN} check Uop info:{result}")
            uop_info.set(result)
            MLBSN.set("")
            # top.config(bg='green')
        else:
            err_info = re.search(r"UNIT OUT OF PROCESS(.*)", res)
            print("错误信息：", err_info)
            err_code = err_info.groups()[0] if err_info else ""
            print("错误代码：", err_code)
            result = (SN + ":\r\n""流程异常，请停止测试！\r\n 错误信息：" + err_code)
            # print(result)
            uop_info.set(result)
            tk.messagebox.showerror(title='Error', message=result)
            logger.info(f"{SN} check Uop info:{result}")
            # top.config(bg='orange')
            MLBSN.set("")
    except:
        result = res.replace('\n', ' ')
        print(result)
    logger.info(f"{SN} check Uop info:{result}")
    uop_info.set(result)
    MLBSN.set("")


def main(event):
    sn = input_barcode.get()
    Uop_check(sn)


if __name__ == '__main__':
    top = tk.Tk()
    top.title("SFCS query-tool_1.3")
    top.geometry("600x130+500+50")
    top.resizable(0, 0)
    top.config(bg='#F0FFFF')
    # top.attributes('-topmost', True)
    uop_info = tk.StringVar()
    MLBSN = tk.StringVar()
    L_id = tk.Label(top, text="PanelID", bg='#F0FFFF')
    L_id.pack()
    # R_id = tk.Label(top, text = "R-PanelID").place(x = 30, y = 90)
    # Label_tip = tk.Label(top,text = "",).place(x = 30, y = 130)
    input_barcode = tk.Entry(top, textvariable=MLBSN, fg='blue', bg='#FFFF00', width=18)
    input_barcode.pack()
    # P_L_ID = tk.Entry(top,textvariable=MLBSN).place(x = 100, y = 50)
    # P_R_ID = tk.Entry(top,textvariable=MLBSN).place(x = 100, y = 90)
    Tips = tk.Label(top, textvariable=uop_info, bg='#F0FFFF', fg='blue')
    Tips.pack()
    # P_L_ID.bind("<Return>", main)
    # P_R_ID.bind("<Return>", main)
    input_barcode.bind("<Return>", main)
    top.mainloop()
