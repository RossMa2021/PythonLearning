import webbrowser
# my tool for
import transferTool as trans
import geoTool as geoTool
import mapTool as mapTool
import tableTool as tableTool

def generateData():
    # 生成转换后数据
    geoTool.prepareData_china()
    geoTool.prepareData_zhejiang()

def generateBackgroundMap():
    # 生成全国地图备用
    mapTool.generateMap_china()
    # 生成浙江省地图备用
    mapTool.generateMap_zhejiang()
    # 生成统计结果表
    tableTool.generateTable()

def generateDistibution():
    # 生成全国分布
    geoTool.generateDistribution_china()
    # 生成浙江省分布
    geoTool.generateDistribution_zhejiang()

    # url = "HTML\\FriendDistribution.html"
    # webbrowser.open(url, new=2)

if __name__ == '__main__':
    while 1:
        menuTool = input("请选择操作：0.生成底图 1.生成数据 2.绘制分布")
        if menuTool == "0" :
            generateBackgroundMap()
            print("底图生成完成!")
        elif menuTool == "1" :
            generateData()
            print("数据生成完成!")
        elif menuTool == "2":
            generateDistibution()
            print("分布绘制完成!")



