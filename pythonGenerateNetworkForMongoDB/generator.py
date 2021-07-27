# -*- coding: utf-8 -*-
"""
Created on Sat May  2 04:55:36 2020

@author: Chenjun Li
"""

import csv
import random



def genSimulationUnit(longitude1, latitude1, longitude2, latitude2, deviceNumber, userNumber):
    if(longitude1 > 180):
        longitude1 = 180
    if(longitude1 < - 180):
        longitude1 = -180
    if(latitude1 > 90):
        latitude1 = 90
    if(latitude1 < -90):
        latitude1 = - 90
    if(longitude2 > 180):
        longitude2 = 180
    if(longitude2 < - 180):
        longitude2 = -180
    if(latitude1 > 90):
        latitude2 = 90
    if(latitude1 < -90):
        latitude2 = - 90
        
    midLong = (longitude1 + longitude2)/2
    midLati = (latitude1 + latitude2)/2
    
    genProject(midLong, midLati)
    
    with open('Radio.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["prefix", "device_id", "current_radio_name", "current_radio_index", "radio_name1", "radio_standard1", "radio_my1", "radio_channel1", "radio_network_id1", "radio_radius1", "radio_etx1", "radio_erx1", "radio_esleep1", "radio_elisten1", "radio_data_rate1", "conso_tx_model1", "conso_rx_model1"])
    with open('Devices.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["prefix", "device_type", "device_id", "device_longitude", "device_latitude", "device_elevation", "device_radius", "device_hide", "device_draw_battery", "device_sensor_unit_radius", "device_gps_file_name", "device_script_file_name", "natural_event_file_name"])
        
    currentID = genSensors(longitude1, latitude1, midLong, midLati, deviceNumber/4, 1)
    currentID = genRouters(longitude1, latitude1, midLong, midLati, deviceNumber/8, currentID)
    currentID = genBaseStations(longitude1, latitude1, midLong, midLati, deviceNumber/16, currentID)
    currentID = genNatureEvents(longitude1, latitude1, midLong, midLati, deviceNumber/4, currentID)
    
    currentID = genSensors(longitude1, latitude2, midLong, midLati, deviceNumber/4, currentID)
    currentID = genRouters(longitude1, latitude2, midLong, midLati, deviceNumber/8, currentID)
    currentID = genBaseStations(longitude1, latitude2, midLong, midLati, deviceNumber/16, currentID)
    currentID = genNatureEvents(longitude1, latitude2, midLong, midLati, deviceNumber/4, currentID)   
    
    currentID = genSensors(longitude2, latitude1, midLong, midLati, deviceNumber/4, currentID)
    currentID = genRouters(longitude2, latitude1, midLong, midLati, deviceNumber/8, currentID)
    currentID = genBaseStations(longitude2, latitude1, midLong, midLati, deviceNumber/16, currentID)
    currentID = genNatureEvents(longitude2, latitude1, midLong, midLati, deviceNumber/4, currentID)
    
    currentID = genSensors(longitude2, latitude2, midLong, midLati, deviceNumber/4, currentID)
    currentID = genRouters(longitude2, latitude2, midLong, midLati, deviceNumber/8, currentID)
    currentID = genBaseStations(longitude2, latitude2, midLong, midLati, deviceNumber/16, currentID)
    currentID = genNatureEvents(longitude2, latitude2, midLong, midLati, deviceNumber/4, currentID)
    
    with open('Users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["prefix", "selectedArea", "selectedLocation", "name", "latitude1", "latitude2", "longitude1", "longitude2", "locationLongitude", "locationLatitude", "temperatureSensing", "humiditySensing", "gasSensing", "lightSensing", "windLevelSensing", "waterLevelSensing", "dataEncrypted", "preferredLatency", "preferredThroughput", "preferredFrequency", "startTime", "endTime"])
    genUsers(longitude1, latitude1, longitude2, latitude2, userNumber)


def genSensors(longitude1, latitude1, longitude2, latitude2, num, currentID):
    temp = currentID
    with open('Devices.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        while(num > 0):
            pos = genRanPoint(longitude1, latitude1, longitude2, latitude2)
            writer.writerow(["device", 1, temp, pos[0], pos[1], 0, 0, 1, "false", 100, "", "SensorWithRouterFunction.csc", ""])
            genRadio(temp)
            temp = temp + 1
            num = num - 1
    return temp


def genRouters(longitude1, latitude1, longitude2, latitude2, num, currentID):
    temp = currentID
    with open('Devices.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        while(num > 0):
            pos = genRanPoint(longitude1, latitude1, longitude2, latitude2)
            writer.writerow(["device", 1, temp, pos[0], pos[1], 0, 0, 1, "false", 20, "", "Router.csc", ""])
            genRadio(temp)
            temp = temp + 1
            num = num - 1
    return temp


def genBaseStations(longitude1, latitude1, longitude2, latitude2, num, currentID):
    temp = currentID
    with open('Devices.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        while(num > 0):
            pos = genRanPoint(longitude1, latitude1, longitude2, latitude2)
            writer.writerow(["device", 4, temp, pos[0], pos[1], 0, 0, 1, "false", 20, "", "BaseStationWithRouterFunction.csc", ""])
            genRadio(temp)
            temp = temp + 1
            num = num - 1
    return temp


def genNatureEvents(longitude1, latitude1, longitude2, latitude2, num, currentID):
    temp = currentID
    eventType = 1
    tempType = -1
    typeFile = ""
    with open('Devices.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        while(num > 0):
            eventType = random.randint(1, 6)
            if(eventType == 1):
                tempType = 2
                typeFile = "gas.evt"
            if(eventType == 2):
                tempType = 13
                typeFile = "temperature.evt"
            if(eventType == 3):
                tempType = 14
                typeFile = "humidity.evt"
            if(eventType == 4):
                tempType = 15
                typeFile = "windLevel.evt"
            if(eventType == 5):
                tempType = 16
                typeFile = "waterLevel.evt"
            if(eventType == 6):
                tempType = 17
                typeFile = "lighting.evt"
            pos = genRanPoint(longitude1, latitude1, longitude2, latitude2)
            writer.writerow(["device", tempType, temp, pos[0], pos[1], 0, 10, 1, "false", 0, "", "", typeFile])
            temp = temp + 1
            num = num - 1
    return temp


def genRadio(myID):
    with open('Radio.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["radio_module", str(myID), "radio1", 1, "radio1", "ZIGBEE", 0, 0, 13108, 100, 0.0000592, 0.0000286, 1e-7, 0.000001, 250000, "Classical (Tx)", "Classical (Rx)"])


def genUsers(longitude1, latitude1, longitude2, latitude2, num):
    userID = 1
    Tem = "false"
    Hum = "false"
    Wat = "false"
    Lig = "false"
    Gas = "false"
    Win = "false"
    sensorType = 1
    with open('Users.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        while(num > 0):
            userName = "User " + str(userID)
            userPos = genRanPoint(longitude1, latitude1, longitude2, latitude2)
            area1 = genRanPoint(longitude1, latitude1, longitude2, latitude2)
            area2 = genRanPoint(longitude1, latitude1, longitude2, latitude2)
            sensorType = random.randint(1, 2)
            if(sensorType == 1):
                Tem = "true"
            else:
                Tem = "false"
            sensorType = random.randint(1, 2)
            if(sensorType == 1):
                Hum = "true"
            else:
                Hum = "false"
            sensorType = random.randint(1, 2)
            if(sensorType == 1):
                Wat = "true"
            else:
                Wat = "false"
            sensorType = random.randint(1, 2)
            if(sensorType == 1):
                Lig = "true"
            else:
                Lig = "false"
            sensorType = random.randint(1, 2)
            if(sensorType == 1):
                Gas = "true"
            else:
                Gas = "false"
            sensorType = random.randint(1, 2)
            if(sensorType == 1):
                Win = "true"
            else:
                Win = "false"
            
            freq = random.randint(2, 10)
            freq = freq * 1.0
            writer.writerow(["user", "true", "true", userName, area1[1], area2[1], area1[0], area2[0], userPos[0], userPos[1], Tem, Hum, Wat, Lig, Gas, Win, 0, 10.0, 0.0, freq, 0, 64000])
            userID = userID + 1
            num = num -1


def genProject(centerLong, centerLati):
    with open('Project.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["prefix", "CupCarbon", "name", "zoom", "centerposition_la", "centerposition_lo", "map", "display_details", "draw_radio_links", "draw_sensor_arrows", "radio_links_color", "draw_marker_arrows", "display_rl_distance", "propagation", "display_marker_distance", "display_radio_messages", "draw_script_file_name", "display_print_messages", "display_all_routes"])
        writer.writerow(["project", "U-One 4.2", "cs682", 4, centerLati, centerLong, 0, "false", "true", "true", 0, "false", "false", "false", "false", "false", "false", "true", "false"])


def genRanPoint(longitude1, latitude1, longitude2, latitude2):
    minLong = min(longitude1, longitude2)
    maxLong = max(longitude1, longitude2)
    minLati = min(latitude1, latitude2)
    maxLati = max(latitude1, latitude2)
    x = random.uniform(minLong, maxLong)
    y = random.uniform(minLati, maxLati)
    res = [x, y]
    return res


genSimulationUnit(-71.0446572303772, 42.319177010972695, -71.03641748428345, 42.31097379616, 100, 6)