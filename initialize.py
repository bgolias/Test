# -*- coding: utf-8 -*-
"""
Spyder Editor

This creates a text file from an Excel Spreadsheet that the powershell initialization script then reads from 
"""
import glob
import pandas as pd
import math


def setvalue(device_dataframe,columnName,default_dict,set_type,side="Left"):
    if device_dataframe['Unit Name'].str.contains("LS-654", na=False).bool() and columnName=="UID":
       uid_list=device_dataframe[columnName].str.split(" ").item()
       if type(uid_list)==list:
           if(side=="Left"):
               return int(uid_list[0].strip("L"))
           else:
               return int(uid_list[1].strip("R"))
       else:
           return default_dict["Left and Right UID"]
    try:
        read_value=device_dataframe[columnName].item()
    except:
        print("No column with the name "+columnName+" exists")
        read_value=default_dict[columnName]
    if type(read_value)!=str:
        if (math.isnan(read_value)):
            read_value=default_dict[columnName]
            return read_value
    if set_type=="str":
        return str(read_value)
    else:
        return int(read_value)

defaults={"Unit Name": "",
          "Equipment Type": "",
          "Station": 1,
          "Default Group": 23,
          "Co-Loc": 0,
          "IC-Offset": 0,
          "Override Frequency": 0,
          "Circuit Number": 1,
          "Ring Line": 1,
          "Instructor Flag": "N",
          "IP Address": "10.10.17.21",
          "Subnet Mask":"255.255.255.0",
          "Gateway": "NONE",
          "Multicast IP": "225.0.2.",
          "GMDSS Net Port": 5020,
          "UID": 13,
          "Recording": "N",
          "PC NAME": "DESKTOP-F61EA5",
          "VHF MMSI": "",
          "BCG Serial": "",
          "Mic Type": "Hand",
          "Firmware": 4.1,
          "IVCS\LS-654 Loc": 2,
          "Open Lines": 1,
          "Circuits": 1,
          "Left and Right UID": 1}

f = glob.glob(r'C:\Utils\*.csv')[-1]
df=pd.read_csv(f)

val_device= input("Enter a device: ")
val_sn = input("Enter a SN: ")

contain_values = df[df['Unit Name'].str.contains(val_device, na=False)]
TempShare =list(df.loc[df["Unit Name"] == "TempShare"].values[0])[1]
device_info=contain_values[contain_values['BCG Serial']==int(val_sn)]
seriesindex=0
deviceindex=0
caid=0
location=2
openlines=1
circuits=1
leftuid=1
rightuid=1
if device_info.empty ==False:
    station=setvalue(device_info,"Station",defaults,"int")
    group=setvalue(device_info,"Default Group",defaults,"int")
    
    Colocation=setvalue(device_info,"Co-Loc",defaults,"int")
    
    ICOffset=setvalue(device_info,"IC-Offset",defaults,"int")
    Overridefrequency=setvalue(device_info,"Override Frequency",defaults,"int")
    ComputerName=setvalue(device_info,"PC NAME",defaults,"str")
    CommsIP=setvalue(device_info,"IP Address",defaults,"str")
    CommsMask=setvalue(device_info,"Subnet Mask",defaults,"str")
    Commsgateway=setvalue(device_info,"Gateway",defaults,"str")
    Commsmulticast=setvalue(device_info,"Multicast IP",defaults,"str")
    Commsport=setvalue(device_info,"GMDSS Net Port",defaults,"str")
    Recording=setvalue(device_info,"Recording",defaults,"str")
    uid=setvalue(device_info,"UID",defaults,"int")
    i=0

    spp_circuit=1
    spp_ring=1
    info_list=[]
    if val_device=='SPP':
        seriesindex=1
        caid=""
        spp_circuit=setvalue(device_info,"Circuit Number",defaults,"int")
        spp_ring=setvalue(device_info,"Ring Line",defaults,"int")
        if device_info['Mic Type'].str.contains('Hand', na= False).bool()==True:
            deviceindex=1
        else:
            deviceindex=2
    if val_device=='Red':
        seriesindex=2
        deviceindex=1
    if val_device=='UHF':
        seriesindex=2
        deviceindex=2
    if val_device=='NET15':
        seriesindex=3
        deviceindex=1
    if val_device=='TT-NET':
        seriesindex=3
        deviceindex=2
    if val_device=="1MC":
        seriesindex=4
        deviceindex=1
    if val_device=="IVCS":
        seriesindex=5
        deviceindex=1
        location=setvalue(device_info,"IVCS\LS-654 Loc",defaults,"int")
    if val_device=="LS-654":
        seriesindex=5
        deviceindex=2
        location=setvalue(device_info,"IVCS\LS-654 Loc",defaults,"int")
        openlines=setvalue(device_info,"Open Lines",defaults,"int")
        circuits=setvalue(device_info,"Circuits",defaults,"int")
        leftuid=setvalue(device_info,"UID",defaults,"int","Left")
        rightuid=setvalue(device_info,"UID",defaults,"int","Right")
    if val_device=='SPP-PM':
        seriesindex=7
        deviceindex=1
        spp_circuit=setvalue(device_info,"Circuit Number",defaults,"int")
        spp_ring=setvalue(device_info,"Ring Line",defaults,"int")
    info_list=[seriesindex, deviceindex, caid, int(val_sn), ComputerName, CommsIP, CommsMask, Commsgateway, Commsmulticast, Commsport, group, station, Colocation, ICOffset, Overridefrequency, Recording, uid, spp_circuit, spp_ring, location, openlines, circuits, leftuid, rightuid, TempShare]
    print(info_list)
    with open(r'C:/Utils/initial.txt', 'w') as fp:
        for item in info_list:
            fp.write("%s\n" % item)    
    

    