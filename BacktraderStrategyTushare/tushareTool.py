import tushare as ts
import os
import os.path
from pathlib import Path

class tushareTool:
    def __init__(self):
        ts.set_token('c343b849075c0ed86534b3e4fe8a40d90d57f6ee50e6b96f1d71d6f1')
        self.pro = ts.pro_api()

    def downloadDataCsv(self,tsCode,startDate,endDate):
        # 检查如果存在就跳过
        filename = tsCode.replace('.','') + '.csv'
        path = 'DataCsv/'+ filename
        my_file = Path(path)
        if my_file.exists():
            print(filename + '.csv is alread existsed.\n')
            return

        self.df = self.pro.daily(ts_code=tsCode, start_date=startDate, end_date=endDate)
        self.df = self.df.sort_index(ascending=True)
        self.df.to_csv(path)
        print(filename+'.csv is alread download.\n')