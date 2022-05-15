import tushare as ts
from clickhouse_driver import Client
from datetime import datetime, timedelta, timezone
from dataIntegrator.TuShareService.TuShareService import TuShareService

class TuShareChinaStockIndexService(TuShareService):

    @classmethod
    def prepareDataFrame(self, ts_code, start_date, end_date):
        print("prepareData started")

        try:
            ts.set_token(self.token)
            pro = ts.pro_api()
            self.dataframe = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            print(self.dataframe.dtypes)

        except Exception as e:
            print('Exception', e)
            raise e

        print("prepareData ended")

        return self.dataframe

    @classmethod
    def convertDataFrame2JSON(self):
        print("prepareData started")

        try:
            dataFrame = self.dataframe
            self.jsonString = dataFrame.to_json(orient='table')
        except Exception as e:
            print('Exception', e)
            raise e

        print("prepareData ended")

        return self.jsonString

    @classmethod
    def saveDateFrameToDisk(self, fileName):
        print("saveDateToDisk started")

        try:
            self.dataframe.to_csv(
                fileName,
                sep='\u0001',
                mode="w",
                header="true")
        except Exception as e:
            print(e.message)
            raise e

        print("saveDateToDisk completed")

        return

    @classmethod
    def saveDateToClickHouse(self):
        print("saveDateToClickHouse started")

        try:
            client = Client(host='192.168.98.135', database='indexsysdb')

            insert_df_tushare_stock_daily = 'insert into indexsysdb.df_tushare_stock_daily (ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount) VALUES'

            dataValues = self.dataframe.to_dict('records')
            client.execute(insert_df_tushare_stock_daily, dataValues)
        except Exception as e:
            print(e.message)
            raise e

        print("saveDateToClickHouse ended")
