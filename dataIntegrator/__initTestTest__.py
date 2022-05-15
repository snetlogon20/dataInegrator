import os
from dataIntegrator.TensorFlowService import TensorFlowService
# from dataIntegrator.KafkaService import KafkaService
# import cx_Oracle
# import matplotlib.pyplot as plt

def getEnv():
    print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
    print("PATH:", os.environ.get('PATH'))

# def callTensorFlowService():
#     print()
#
#     tensorFlowService = TensorFlowService.TensorFlowService()
#     # tensorFlowService.prepareData()
#     # tensorFlowService.trainModel()
#
#     tensorFlowService.readData()
#
# def callKafkaService():
#
# #    kafkaService = KafkaService.KafkaFlowService()
#
#     #kafkaService.prepareData()
#     #kafkaService.sendData()
#
#     kafkaService.sendDataSingleFuture("1111")
#
#
#
# def callCx_Oracle():
#     conn = cx_Oracle.connect('citi/"citi@citi"@192.168.98.129/orcl.localdomain')
#     curs = conn.cursor()
#     sql = 'select stuname, age from stuinfo '
#     curs.execute(sql)
#
#     stuname = []
#     stuage = []
#
#     for result in curs:
#         print(result[0], result[1])
#         stuname.append(result[0])
#         stuage.append(result[1])
#
#     curs.close()
#     conn.close()
#
#     plt.bar(range(len(stuage)), stuage, color='red', tick_label=stuname)
#     plt.xticks(rotation=-90)
#     plt.xlabel("student name")
#     plt.ylabel("student age")
#     plt.title("student chart")
#     for x, y in enumerate(stuage):
#         plt.text(x-0.3, y+0.5, y, fontsize=10, color='blue')
#     plt.show()
#
# def main():
#     print("hello python")
#     #callTensorFlowService()
#     #callCx_Oracle()
#     callKafkaService()
#
# if __name__ == '__main__':
#     main()
#
