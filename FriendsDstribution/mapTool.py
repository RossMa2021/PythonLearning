from pyecharts.charts import Map
from pyecharts import options as opts

# 用于绘制 全国和浙江基础地图信息

provide1 = ['河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西',
         '山东', '河南', '湖北', '湖南', '广东', '海南', '四川', '贵州', '云南', '陕西',
         '甘肃', '青海', '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆', '北京', '天津',
         '上海', '重庆', '香港', '澳门']
#values1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
values1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
data_provide1 = [list(z) for z in zip(provide1, values1)]

provide = ['无']
values = [0]
data_provide = [list(z) for z in zip(provide, values)]

city1 = ['杭州市', '湖州市', '嘉兴市', '金华市', '丽水市', '宁波市', '衢州市', '绍兴市', '台州市', '温州市', '舟山市']
values2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]
data_city1 = [list(z) for z in zip(city1, values2)]

def generateMap_china():
    china = (
        Map(init_opts=opts.InitOpts(width="1920px", height="1080px", page_title='中国地图',bg_color="#FFFFFF"))
            .add('',
                 data_provide1,
                 maptype='china',
                 is_roam=True,
                 is_selected=False,
                 # 字体颜色
                 label_opts=opts.LabelOpts(is_show=True, formatter='{b}', font_size=15, color = "#BEBEBE"),
                 is_map_symbol_show=False
                 )
            .set_global_opts(title_opts=opts.TitleOpts(),  # 当前窗口打开
                             visualmap_opts=opts.VisualMapOpts(is_show=False,  # 视觉映射配置
                                                               max_=0,
                                                               range_color=["#1E90FF","#1E90FF"],
                                                               is_calculable=True,  # 是否显示拖拽用的手柄
                                                               is_piecewise=True,  # 是否为分段型
                                                               #range_text=["High", "Low"],
                                                               border_color="#FFFFFF")
                             )
        .render('HTML\\Map_china.html')
    )

def generateMap_zhejiang():
    zhejiang = (
        Map(init_opts=opts.InitOpts(width="1920px", height="1080px", page_title='中国地图', bg_color="#FFFFFF"))
            .add('',
                 data_city1,
                 maptype='浙江',
                 is_roam=True,
                 is_selected=False,
                 # 字体颜色
                 label_opts=opts.LabelOpts(is_show=True, formatter='{b}', font_size=15, color="#BEBEBE"),
                 is_map_symbol_show=False
                 )
            .set_global_opts(title_opts=opts.TitleOpts(),  # 当前窗口打开
                             visualmap_opts=opts.VisualMapOpts(is_show=False,  # 视觉映射配置
                                                               max_=0,
                                                               range_color=["#1E90FF", "#1E90FF"],
                                                               is_calculable=True,  # 是否显示拖拽用的手柄
                                                               is_piecewise=True,  # 是否为分段型
                                                               # range_text=["High", "Low"],
                                                               border_color="#FFFFFF")
                             )
        .render('HTML\\Map_province_zhejiang.html')
    )
