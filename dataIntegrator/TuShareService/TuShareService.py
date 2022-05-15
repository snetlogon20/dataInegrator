import pandas

class TuShareService:
    token = "00fcaf64c13f1a8e58011bb7b07d2016f9c632e7711162c0b95c2003"
    dataFrame = pandas.core.frame.DataFrame
    jsonString = ""

    def __init__(self):
        print("__init__ started")

        self.token = self.getToken()

        print("__init__ completed")

    @classmethod
    def getToken(self):
        print("getToken started")

        print("getToken ended")

        return self.token

    @classmethod
    def prepareDataFrame(self, ts_code, start_date, end_date):
        print("prepareData started")

        print("prepareData completed")

    @classmethod
    def convertDataFrame2JSON(self):
        print("prepareData started")

        print("prepareData completed")

    @classmethod
    def saveDateFrameToDisk(self, fileName):
        print("saveDateToDisk started")

        print("prepareData ended")

    @classmethod
    def saveDateToClickHouse(self):
        print("saveDateToClickHouse started")

        print("saveDateToClickHouse completed")
