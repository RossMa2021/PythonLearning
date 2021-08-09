import json as json
from pyecharts import options as opts
from pyecharts.charts import Geo
import transferTool as trans
import random as random

def prepareData_china():
    test_data_ = trans.generateData("INPUTDATA\\studentData-china.txt")
    json_data = {}
    for ss in range(len(test_data_)):
        json_data[test_data_[ss][0]] = [test_data_[ss][1], test_data_[ss][2]]

    json_str = json.dumps(json_data, ensure_ascii=False, indent=4)
    with open('OUTPUTDATA\\distributionData_china.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)

def prepareData_zhejiang():
    test_data_ = trans.generateData("INPUTDATA\\studentData-zhejiang.txt")
    json_data = {}
    for ss in range(len(test_data_)):
        json_data[test_data_[ss][0]] = [test_data_[ss][1], test_data_[ss][2]]

    json_str = json.dumps(json_data, ensure_ascii=False, indent=4)
    with open('OUTPUTDATA\\distributionData_zhejiang.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)

def generateDistribution_china() -> Geo:
    # distributionData: ('李十四', '113.349906', '23.155411')
    distributionData = trans.generateData("INPUTDATA\\studentData-china.txt")
    # init
    name = []
    color = []
    for ss in range(len(distributionData)):
        name.append(distributionData[ss][0])
        color.append(100) # 控制颜色

    # paint
    c = (
        # 背景色
        Geo(init_opts=opts.InitOpts(width="1920px", height="1080px", page_title='毕业生分布',bg_color="#FFFFFF"))
            .add_schema(maptype="china",
                        # 地图背景色 和 边框色
                        itemstyle_opts=opts.ItemStyleOpts(color="#FFFFFF", border_color="#D3D3D3"))
            # 加入自定义的点 通过点的实际位置
            .add_coordinate_json(json_file='OUTPUTDATA\\distributionData_china.json')
            # 为自定义的点添加属性: 名字和颜色
            .add("", data_pair=[list(z) for z in zip(name, color)], symbol_size=20, large_threshold=2000, symbol="pin",point_size=50,
                 blur_size=50,
                 color="#000000",
                 #label_opts=opts.LabelOpts(is_show=True,formatter='{b}',font_size=16,color="#0000FF"))
                 label_opts=opts.LabelOpts(is_show=True, formatter='{b}', font_size=15, color = "#B22222"))
            # 地图的显示格式
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=False,max_=100,range_color=["#FFFFFF","#B22222"]),
                             title_opts=opts.TitleOpts(title="毕业生分布"))
    ).render("HTML\\FriendDistribution-china.html")

def generateDistribution_zhejiang() -> Geo:
    # distributionData: ('李十四', '113.349906', '23.155411')
    distributionData = trans.generateData("INPUTDATA\\studentData-zhejiang.txt")
    # init
    name = []
    color = []
    for ss in range(len(distributionData)):
        name.append(distributionData[ss][0])
        color.append(100)  # 控制颜色

    # paint
    c = (
        # 背景色
        Geo(init_opts=opts.InitOpts(width="1920px", height="1080px", page_title='毕业生分布', bg_color="#FFFFFF"))
            .add_schema(maptype="浙江",
                        # 地图背景色 和 边框色
                        itemstyle_opts=opts.ItemStyleOpts(color="#FFFFFF", border_color="#D3D3D3"))
            # 加入自定义的点 通过点的实际位置
            .add_coordinate_json(json_file='OUTPUTDATA\\distributionData_zhejiang.json')
            # 为自定义的点添加属性: 名字和颜色
            .add("", data_pair=[list(z) for z in zip(name, color)], symbol_size=20, large_threshold=2000, symbol="pin",
                 point_size=50,
                 blur_size=50,
                 color="#000000",
                 # label_opts=opts.LabelOpts(is_show=True,formatter='{b}',font_size=16,color="#0000FF"))
                 label_opts=opts.LabelOpts(is_show=True, formatter='{b}', font_size=15, color="#B22222"))
            # 地图的显示格式
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(is_show=False, max_=100, range_color=["#FFFFFF", "#B22222"]),
            title_opts=opts.TitleOpts(title="毕业生分布"))
    ).render("HTML\\FriendDistribution-zhejiang.html")
