from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts

def readData():
    info_data = []
    with open("INPUTDATA\\tableSumData.txt", "r") as f:
     while True:
        data = f.readline()
        if not data:
            break
        # print(data)

        # 分割字符串 name scholl city
        info_data.append([data.split(",")[0], data.split(",")[1]])

    return info_data

def generateTable():
    readData()

    table = Table()
    headers = ["城市", "人数"]
    rows = readData()
    table.add(headers, rows)
    table.set_global_opts(
        title_opts=ComponentTitleOpts()
    )
    table.render("HTML\\table_base.html")