from pyecharts.charts import Geo
from pyecharts import options
from pyecharts.globals import GeoType

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
import pandas as pd
import json

import urllib
import webbrowser

def test1():
    g = Geo().add_schema(maptype="福州")
    g.add_coordinate("福州大学", 119.195050, 26.057266)
    data_pair = [("福州大学",1)]
    g.add('',data_pair, type_=GeoType.EFFECT_SCATTER, symbol_size=20)
    g.set_series_opts(label_opts=options.LabelOpts(is_show=False))
    g.set_global_opts(title_opts=options.TitleOpts(title="地图标点测试"))

    g.render_notebook()


def add_adress_one() -> Geo:
    c = (
        Geo()
            .add_schema(maptype="china")  # 加入自定义的点，格式为
            .add_coordinate("测试点", 119.195050, 26.057266)  # 加入的地址名称，和经度、纬度
            # 为自定义的点添加属性，名称要一致，例如均为 '测试点'
            .add("", data_pair=[("测试点", 100)], symbol_size=30, large_threshold=1000, symbol="pin")

            #        .add(                                   #可用于在同一个图上绘制多个图形
            #            "",
            #            data_pair =[("测试点", 100)],
            #            type_=ChartType.EFFECT_SCATTER,
            #            symbol_size=10, point_size = 3,
            #            color="yellow",
            #        )

            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=500),
                             title_opts=opts.TitleOpts(title="加入一个名为测试点的坐标"))
    )
    return c


if __name__ == '__main__':
    add_one = add_adress_one()
    add_one.render(path="test_add_one.html")

    # page = urllib.urlopen('test_add_one.html').read()
    # print(page)

    url = "test_add_one.html"
    webbrowser.open(url, new=2)