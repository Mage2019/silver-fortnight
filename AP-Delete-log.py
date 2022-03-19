#!/usr/local/bin/python
# -*-coding:UTF-8-*-
# -*-coding:cp936-*-
import os
import time
import datetime
# import logging
import psutil
import glob
import json
from tkinter import *
# import subprocess
from tkinter import ttk
import tkinter.messagebox
class DeleteFile(object):
    def __init__(self, path):
        self.path = path

    def delete(self):
        file_list = [self.path]  # file list
        # get time
        today = datetime.datetime.now()
        # effect time
        offset = datetime.timedelta(hours=-24)
        # get need delete time
        re_date = (today + offset)
        # switch effect time to The time stamp
        re_date_unix = time.mktime(re_date.timetuple())

        try:
            while file_list:  # check wether the list is empty.
                path = file_list.pop()  # Delete the last element of the list and return it to path
                for item in os.listdir(path):  # Walk through the list,path
                    path2 = os.path.join(path, item)  # Combine absolute path path2
                    if os.path.isfile(path2):  # Check whether the absolute path is a file
                        # Comparing the timestamp, the file modification time is less than or equal to effect time days ago
                        if os.path.getmtime(path2) <= re_date_unix:
                            os.remove(path2)
                    else:
                        if not os.listdir(path2):  # Check whether the directory is empty
                            # If the directory is empty, delete it and recurse to the directory above, if it is also empty, delete it, and so on.
                            os.removedirs(path2)
                        else:
                            file_list.append(path2)

            return True
        except Exception as e:
            print(e)
            return False


def check_running():
    count = 0
    pid_list = psutil.pids()
    for pid in pid_list:
        p = psutil.Process(pid)
        if p.name() == "AP-Delete-log":
            count += 1
        if count >= 3:
            tkinter.messagebox.showerror(title='Error', message='Do not open the program again! Thank you very much!')
            sys.exit()


def read_json():
    with open("/vault/data_collection/test_station_config/gh_station_info.json", encoding="utf-8", ) as f:  # open json file
        # with open("./gh_station_info.json", 'r') as f:  # open json file
        jdata = json.loads(f.read())  # load json
        # print(jdata)
        jstationName = jdata["ghinfo"]["STATION_TYPE"]  # get StationName
        # print(jstationName)
        return jstationName


# def clear_trash():
#     DeleteFile('~/.Trash').delete()
def clear_log():
    time.sleep(5)
    if read_json() == "DFU":
        time.sleep(0.5)
        msg.set("Station type is  DFU")
        pd["value"] = 10
        root.update()
        time.sleep(0.5)
        msg.set("The system starts to delete the Atlas directory")
        pd["value"] = 15
        root.update()
        DeleteFile('/vault/Atlas').delete()  # delete atlas
        msg.set("he Atlas directory has been deleted")
        pd["value"] = 30
        root.update()
        time.sleep(0.5)
        msg.set("Start deleting the AtlasSummary directory")
        DeleteFile('/Users/gdlocal/Documents/AtlasSummary').delete()  # delete atlassummary
        time.sleep(0.5)
        msg.set("The Atlassummary directory has been deleted")
        pd["value"] = 50
        root.update()
        time.sleep(0.5)
        msg.set("reDFU station log deleted is about to exit the program")
        pd["value"] = 60
        time.sleep(0.5)
        msg.set("The system starts to re-delete the Atlas directory")
        pd["value"] = 70
        root.update()
        DeleteFile('/vault/Atlas').delete()  # delete atlas
        msg.set("he Atlas directory has been deleted")
        pd["value"] = 80
        root.update()
        time.sleep(0.5)
        msg.set("Start re-deleting the AtlasSummary directory")
        DeleteFile('/Users/gdlocal/Documents/AtlasSummary').delete()  # delete atlassummary
        time.sleep(0.5)
        msg.set("The Atlassummary directory has been deleted")
        pd["value"] = 90
        root.update()
        time.sleep(0.5)
        msg.set("PreDFU station log deleted is about to exit the program")
        pd["value"] = 100
        root.update()
        time.sleep(1)
        root.destroy()
    elif read_json() == "DFU-NAND-INIT":
        time.sleep(0.5)
        msg.set("Station type is  DFU-NAND-INT")
        pd["value"] = 10
        root.update()
        time.sleep(0.5)
        path_dump_log = os.path.exists('/Users/gdlocal/Desktop/DFU_coredump_log')
        # print("DFU_coredump_log:", path_dump_log)
        msg.set("Deleting the Log path：/Users/gdlocal/Desktop/DFU_coredump_log" + str(path_dump_log))
        DeleteFile('/Users/gdlocal/Desktop/DFU_coredump_log').delete()  # delete dfu coredump log
        msg.set("Delete complete：/Users/gdlocal/Desktop/DFU_coredump_log" + str(path_dump_log))
        pd["value"] = 15
        root.update()
        time.sleep(0.5)
        path_log = os.path.exists("/Users/gdlocal/Documents/LOG")
        # print("Documents/LOG:", path_log)
        msg.set("Deleting the Log path：/Users/gdlocal/Documents/LOG" + str(path_log))
        DeleteFile('/Users/gdlocal/Documents/LOG').delete()  # delete Log
        msg.set("Delete complete：/Users/gdlocal/Documents/LOG" + str(path_log))
        pd["value"] = 35
        root.update()
        time.sleep(0.5)
        path_Archive = os.path.exists("/vault/DCSD/RestoreLogsArchive")
        # print("RestoreLogsArchive:", path_Archive)
        msg.set("Deleting the Log path：/vault/DCSD/RestoreLogsArchive" + str(path_Archive))
        DeleteFile('/vault/DCSD/RestoreLogsArchive').delete()  # delete restorelogarchive
        msg.set("Delete complete：/vault/DCSD/RestoreLogsArchive'" + str(path_Archive))
        pd["value"] = 50
        root.update()
        time.sleep(0.5)
        path_blobfile = os.path.exists('/Users/gdlocal/Documents/TRANTEST_POSTDFU/BlobFiles')
        # print("BlobFiles:", path_blobfile)
        msg.set("Deleting the Log path：Users/gdlocal/Documents/TRANTEST_POSTDFU/BlobFiles" + str(path_blobfile))
        DeleteFile('/Users/gdlocal/Documents/TRANTEST_POSTDFU/BlobFiles').delete()  # delete blobfiles
        msg.set("Delete complete：Users/gdlocal/Documents/TRANTEST_POSTDFU/BlobFiles" + str(path_blobfile))
        pd["value"] = 70
        root.update()
        time.sleep(0.5)
        pdca_list = glob.glob(r"/Users/gdlocal/Documents/TRANTEST_POSTDFU/*/PDCA")
        msg.set("Deleting the Log path：/Users/gdlocal/Documents/TRANTEST_POSTDFU/*/PDCA" + str(pdca_list))
        # print(pdca_list)
        for i in range(len(pdca_list)):
            pdca_l = str(pdca_list[i])
            DeleteFile(str(pdca_l)).delete()
            i += 1
        msg.set("Delete complete：/Users/gdlocal/Documents/TRANTEST_POSTDFU/*/PDCA" + str(pdca_list))
        pd["value"] = 80
        root.update()
        time.sleep(0.5)
        Sequence_list = glob.glob(r"/Users/gdlocal/Documents/TRANTEST_POSTDFU/*/Sequence")
        msg.set("Deleting the Log path：/Users/gdlocal/Documents/TRANTEST_POSTDFU/*/Sequence" + str(Sequence_list))
        # print(Sequence_list)
        for i in range(len(Sequence_list)):
            Sequence_l = str(Sequence_list[i])
            DeleteFile(str(Sequence_l)).delete()
            i += 1
        msg.set("Delete complete：/Users/gdlocal/Documents/TRANTEST_POSTDFU/*/Sequence" + str(Sequence_list))
        pd["value"] = 90
        root.update()
        time.sleep(0.5)
        TestTime_list = glob.glob(r"/Users/gdlocal/Documents/TRANTEST_POSTDFU/*/TestTime")
        # print(TestTime_list)
        msg.set("Deleting the Log path：/Users/gdlocal/Documents/TRANTEST_POSTDFU/*/TestTime" + str(TestTime_list))
        for i in range(len(TestTime_list)):
            TestTime_l = str(TestTime_list[i])
            DeleteFile(str(TestTime_l)).delete()
            i += 1
        msg.set("Delete complete：/Users/gdlocal/Documents/TRANTEST_POSTDFU/*/TestTime" + str(TestTime_list))
        pd["value"] = 100
        root.update()
        time.sleep(0.5)
        msg.set("The PostDFU log is deleted and is about to exit the program.")
        time.sleep(1)
        root.destroy()
    elif read_json() == "FCT":
        time.sleep(0.5)
        msg.set("Station type name:FCT")
        pd["value"] = 10
        root.update()
        time.sleep(0.5)
        path_blobfile = os.path.exists('/Users/gdlocal/Documents/TRANTEST_FCT/BlobFiles')
        # print("BlobFiles:", path_blobfile)
        msg.set("Deleting：/Users/gdlocal/Documents/TRANTEST_FCT/BlobFiles" + str(path_blobfile))
        DeleteFile('/Users/gdlocal/Documents/TRANTEST_FCT/BlobFiles').delete()  # delete blobfiles
        msg.set("Delete complete：/Users/gdlocal/Documents/TRANTEST_FCT/BlobFiles" + str(path_blobfile))
        pd["value"] = 30
        root.update()
        time.sleep(0.5)
        Clean_list = glob.glob(r"/Users/gdlocal/Documents/LOG/*/CLEAN")
        msg.set("Deleting：/Users/gdlocal/Documents/LOG/*/CLEAN" + str(Clean_list))
        for i in range(len(Clean_list)):
            clean_l = str(Clean_list[i])
            DeleteFile(str(clean_l)).delete()
            i += 1
        msg.set("Delete complete：/Users/gdlocal/Documents/LOG/*/CLEAN" + str(Clean_list))
        pd["value"] = 40
        root.update()
        time.sleep(0.5)
        MLB_list = glob.glob(r"/Users/gdlocal/Documents/LOG/*/MLB")
        msg.set("Deleting：/Users/gdlocal/Documents/LOG/*/MLB" + str(MLB_list))
        for i in range(len(MLB_list)):
            mlb_l = str(MLB_list[i])
            DeleteFile(str(mlb_l)).delete()
            i += 1
        msg.set("Delete complete：/Users/gdlocal/Documents/LOG/*/MLB" + str(MLB_list))
        pd["value"] = 50
        root.update()
        time.sleep(0.5)
        UART_list = glob.glob(r"/Users/gdlocal/Documents/LOG/*/UART")
        msg.set("Deleting：/Users/gdlocal/Documents/LOG/*/UART" + str(UART_list))
        for i in range(len(UART_list)):
            uart_l = str(UART_list[i])
            DeleteFile(str(uart_l)).delete()
            i += 1
        msg.set("Delete complete：/Users/gdlocal/Documents/LOG/*/UART" + str(UART_list))
        pd["value"] = 60
        root.update()
        time.sleep(0.5)
        pdca_list = glob.glob(r"/Users/gdlocal/Documents/TRANTEST_FCT/*/PDCA")
        msg.set("Deleting：/Users/gdlocal/Documents/TRANTEST_FCT/*/PDCA" + str(pdca_list))
        for i in range(len(pdca_list)):
            pdca_l = str(pdca_list[i])
            DeleteFile(str(pdca_l)).delete()
            i += 1
        msg.set("Delete complete：/Users/gdlocal/Documents/TRANTEST_FCT/*/PDCA" + str(pdca_list))
        pd["value"] = 70
        root.update()
        time.sleep(0.5)
        Sequence_list = glob.glob(r"/Users/gdlocal/Documents/TRANTEST_FCT/*/Sequence")
        msg.set("Deleting：/Users/gdlocal/Documents/TRANTEST_FCT/*/Sequence" + str(Sequence_list))
        # print(Sequence_list)
        for i in range(len(Sequence_list)):
            Sequence_l = str(Sequence_list[i])
            DeleteFile(str(Sequence_l)).delete()
            i += 1
        msg.set("Delete complete：/Users/gdlocal/Documents/TRANTEST_FCT/*/Sequence" + str(Sequence_list))
        pd["value"] = 80
        root.update()
        time.sleep(0.5)
        TestTime_list = glob.glob(r"/Users/gdlocal/Documents/TRANTEST_FCT/*/TestTime")
        # print(TestTime_list)
        msg.set("Deleting：/Users/gdlocal/Documents/TRANTEST_FCT/*/TestTime" + str(TestTime_list))
        for i in range(len(TestTime_list)):
            TestTime_l = str(TestTime_list[i])
            DeleteFile(str(TestTime_l)).delete()
            i += 1
        msg.set("Delete complete：/Users/gdlocal/Documents/TRANTEST_FCT/*/TestTime" + str(TestTime_list))
        pd["value"] = 90
        root.update()
        time.sleep(0.5)
        msg.set("Complete FCT station log deletion about to exit program")
        time.sleep(0.5)
        pd["value"] = 100
        root.update()
        time.sleep(1)
        root.destroy()
    else:
        tkinter.messagebox.showerror('Error', "This program only works with PreDFU/DFU/FCT, thank you!")
        time.sleep(1)
        root.destroy()


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("300x140+600+300")
    root.resizable(0,0)
    root.title("One key clear log tool(v.2.0)")
    pd = ttk.Progressbar(root, length=200, mode="determinate", orient=HORIZONTAL)
    pd.pack(padx=10,pady=5)
    pd["maximum"] = 100
    pd["value"] = 0
    btn = ttk.Button(root, text='清理Log', command=clear_log)
    # btn.config(foreground='blue')
    btn.pack(padx=10,pady=7)
    msg = StringVar(value='仅保留24小时内Log,点击清理log开始自动清理log!')
    tips = ttk.Label(root, textvariable=msg,anchor=CENTER,foreground='blue')
    tips.pack(padx=10,pady=9)
    # tips.config(fg="blue")
    time.sleep(1)
    check_running()
    # clear_log()
    root.mainloop()

#######change list###########
##2021/12/09 1.2  add auto choose station and delete PostDFU/FCT log function
####2022/01/18  add UI and add only one open function
