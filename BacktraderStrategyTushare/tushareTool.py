import tushare as ts
import os
import os.path
from pathlib import Path

class tushareTool:
    def __init__(self,dataDirectory = 'DataCsv'):
        ts.set_token('c343b849075c0ed86534b3e4fe8a40d90d57f6ee50e6b96f1d71d6f1')
        self.pro = ts.pro_api()
        self.dataDirectory = dataDirectory

    def downloadDataCsv(self,tsCode,startDate,endDate):
        print('downloadDataCsv.\n')
        # 检查如果存在就跳过
        filename = tsCode.replace('.','') + '.csv'
        path = self.dataDirectory + '/' + filename
        my_file = Path(path)
        if my_file.exists():
            print(filename + '.csv is alread existsed.\n')
            return

        self.df = self.pro.daily(ts_code=tsCode, start_date=startDate, end_date=endDate)
        # backtrader导入csv格式需要按时间升序
        self.df = self.df.sort_index(ascending=False)
        self.df.to_csv(path)
        print(filename+'.csv is alread download.\n')