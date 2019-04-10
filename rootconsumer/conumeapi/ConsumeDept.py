# import requests
#
# from ..consume.models.DeptInfo import Dept
#
# REST_API_URI = "http://localhost:8000/api/v1/"
#
# class ConsumeDeptInfo:
#     DEPT_URI="dept/"
#
# def getInfoById(self, id):
#     response = requests.get ( REST_API_URI + ConsumeDeptInfo.DEPT_URI + str ( id ) )
#     print ( 'Get info Dept invoked....', response.status_code )
#     try:
#         # print(response.json())
#         return response.json ()
#     except:
#         pass
#
# def getAllInfo(self):
#     response = requests.get ( REST_API_URI + ConsumeDeptInfo.DEPT_URI )
#     print ( 'Get All info Dept invoked....', response.status_code )
#     try:
#         # print(response.json())
#         return response.json ()
#     except:
#         pass
#
# def insertData(self, entity):
#     if entity and type ( entity ) == Dept:
#         print ( entity.__dict__ )
#         response = requests.post ( REST_API_URI + ConsumeDeptInfo.DEPT_URI, data=entity.__dict__ )
#         print ( 'Insert info Dept invoked....', response.status_code, )
#         try:
#             print ( response.json () )
#         except:
#             pass
#
# def deleteData(self, id):
#     response = requests.delete ( REST_API_URI + ConsumeDeptInfo.DEPT_URI + str ( id ) + "/" )
#     print ( 'Delete info Student invoked....', response.status_code, )
#     try:
#         print ( response.json () )
#     except:
#         pass
#
# def modifyData(self, entity):
#     if entity and type ( entity ) == Dept and entity.id:
#         print ( REST_API_URI + ConsumeDeptInfo.DEPT_URI + str ( entity.id ) )
#         response = requests.put ( REST_API_URI + ConsumeDeptInfo.DEPT_URI + str ( entity.id ) + "/",
#                                   data=entity.__dict__ )
#         print ( 'Get info Student invoked....', response.status_code, )
#         try:
#             return (response.json ())
#         except:
#             pass
#
#
