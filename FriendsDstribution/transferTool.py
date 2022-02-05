import requests as requests
import json as json
import re

""" 请求url方法get方法 """
def requestGet(url):
    try:
        r = requests.get(url=url, timeout=30)
        if r.status_code == 200:
            # print(r.text)
            return r.text
        return None
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def parseJson(jsonCont):
    """  解析json函数 """
    result_json = json.loads(jsonCont)
    return result_json

def transferAddToPos(address, city, name):
    strUrl = 'https://restapi.amap.com/v3/geocode/geo?key=xxxxxxxxxxxxx&'
    strAdd = 'address='+address
    strCity = 'city='+city
    strUrl = strUrl + strAdd + strCity

    strResult = requestGet(strUrl)
    jsonObj = parseJson(strResult)

    strPos = jsonObj['geocodes'][0]['location']

    posX = jsonObj['geocodes'][0]['location'].split(",")[0]
    posY = jsonObj['geocodes'][0]['location'].split(",")[1]
    #
    # print(posX + ',' + posY)
    # print(strPos)
    #strData = [(address, posX, posY)]
    strData = name + ',' + posX + ',' + posY
    return strData

def readData(path):
    info_data = []
    with open(path, "r") as f:
     while True:
        data = f.readline()
        if not data:
            break
        # print(data)

        # 分割字符串 name scholl city
        info_data.append((data.split(",")[0], data.split(",")[1], data.split(",")[2]))

    return info_data
def generateData(path):
    info_data = readData(path)

    distributionData = []

    for info in info_data:
        temp = transferAddToPos(info[1], info[2], info[0])
        distributionData.append((temp.split(",")[0], temp.split(",")[1], temp.split(",")[2]))

    # print(distributionData)
    return distributionData
