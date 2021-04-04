from tushareTool import tushareTool
from backtraderTool import backtraderTool
from strategyNum1 import strategyNum1

# csv数据存储路径
dataDirectory = 'DataCsv'
# 日志存储路径
logDirectory = 'Log'

if __name__ == '__main__':
    # 初始化工具
    ts = tushareTool(dataDirectory)
    bt = backtraderTool(dataDirectory,logDirectory)
    # 加载数据
    ts.downloadDataCsv('002594.SZ','20000101','20201231')
    # 执行回测策略 strategyNum1
    bt.execBacktraderStrategy('002594.SZ','20000101','20201231', strategyNum1)

