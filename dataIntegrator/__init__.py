import os
from dataIntegrator.TensorFlowService import TensorFlowService
from dataIntegrator.TuShareService.TuShareServiceChinaStockIndex import TuShareChinaStockIndexService

def getEnv():
    print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
    print("PATH:", os.environ.get('PATH'))

def callTuShareService():
    print("callTuShareService started...")

    try:
        tuShareChinaStockIndexService = TuShareChinaStockIndexService()
        dataFrame = tuShareChinaStockIndexService.prepareDataFrame(ts_code='000001.SZ,600000.SH',
                                                  start_date='20000101',
                                                  end_date='20220430')
        jsonString = tuShareChinaStockIndexService.convertDataFrame2JSON()
        tuShareChinaStockIndexService.saveDateFrameToDisk("D:\workspace_python\practice\data\df_tushare_stock_daily20220507.csv")
        tuShareChinaStockIndexService.saveDateToClickHouse()

    except Exception as e:
        print('Exception', e)

    print("callTuShareService ended...")

def main():
    print("main started")
    callTuShareService()
    print("end ended")

if __name__ == '__main__':
    main()

