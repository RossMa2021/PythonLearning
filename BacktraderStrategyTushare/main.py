from tushareTool import  tushareTool
from backtraderTool import backtraderTool

if __name__ == '__main__':
    ts = tushareTool()
    ts.downloadDataCsv('002594.SZ','20000101','20201231')
    bt = backtraderTool()
    bt.tryBacktrader()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
