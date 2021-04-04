import datetime
import backtrader as bt

class backtraderTool:
    def __init__(self,dataDirectory = 'DataCsv',logDirectory = 'Log'):
        self.dataDirectory = dataDirectory
        self.logDirectory = logDirectory

    def execBacktraderStrategy(self,tsCode,startDate,endDate,strategyTool):
        # 创建Cerebro引擎
        cerebro = bt.Cerebro()
        # Cerebro引擎在后台创建broker(经纪人)，系统默认资金量为10000

        # 为Cerebro引擎添加策略
        strategyTool.setLogPath(self.logDirectory + '/' + tsCode.replace('.','')+'.txt')

        cerebro.addstrategy(strategyTool)

        # 通过网络读取数据
        # # 获取当前运行脚本所在目录
        # modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        # # 拼接加载路径
        # datapath = os.path.join(modpath, '../../datas/orcl-1995-2014.txt')
        #
        # # 创建交易数据集
        # data = bt.feeds.YahooFinanceCSVData(
        #     dataname=datapath,
        #     # 数据必须大于fromdate
        #     fromdate=datetime.datetime(2000, 1, 1),
        #     # 数据必须小于todate
        #     todate=datetime.datetime(2000, 12, 31),
        #     reverse=False)

        # 载入本地csv数据
        data = bt.feeds.GenericCSVData(
            dataname= self.dataDirectory + '/' + tsCode.replace('.','')+'.csv',
            fromdate= datetime.datetime.strptime(startDate, '%Y%m%d'),
            todate=datetime.datetime.strptime(endDate, '%Y%m%d'),
            nullvalue=0.0,
            dtformat=("%Y%m%d"),
            datetime=2,
            high=4,
            low=5,
            open=3,
            close=6,
            volume=10,
            openinterest=-1
        )

        # 加载交易数据
        cerebro.adddata(data)

        # 设置投资金额1000.0
        cerebro.broker.setcash(1000.0)

        # 每笔交易使用固定交易量
        cerebro.addsizer(bt.sizers.FixedSize, stake=10)
        # 设置佣金为0.0
        cerebro.broker.setcommission(commission=0.0)

        # 引擎运行前打印期出资金
        print('组合期初资金: %.2f' % cerebro.broker.getvalue())
        with open(self.logDirectory + '/' + tsCode.replace('.','')+'.txt', "w",encoding='utf-8') as f:
            f.write('组合期初资金: %.2f' % cerebro.broker.getvalue())
        cerebro.run()
        # 引擎运行后打期末资金
        print('组合期末资金: %.2f' % cerebro.broker.getvalue())
        with open(self.logDirectory + '/' + tsCode.replace('.','')+'.txt', "a",encoding='utf-8') as f:
            f.write('组合期末资金: %.2f' % cerebro.broker.getvalue())

        # 绘制图像
        # cerebro.plot()