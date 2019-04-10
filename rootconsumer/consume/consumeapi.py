import requests

# This is for the backend check
from .consumecontract import ConsumeService
from .models.DeptInfo import Dept
from .models.SubjectInfo import Subject
from rootconsumer.consume.models.StudentInfo import Student
# This is for the webcheck test

REST_API_URI = "http://localhost:8000/api/v1/"


class ConsumeStudentInfo ( ConsumeService ):
    ''' This is the consumer for student'''
    STUDENT_URI = "student/"

    def getInfoById(self, id):
        response = requests.get ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI + str ( id )+"/" )
        print ( 'Get info Student invoked....', response.status_code )
        try:
            return ( response.json () )
        except:
            pass

    def getAllInfo(self):
        response = requests.get ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI )
        print ( 'Get info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass

    def insertData(self, entity):
        files = {'photo': open ( entity.photo, 'rb' )}
        entity.__delattr__ ( 'photo' )
        response = requests.post ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI, files=files, data=entity.__dict__ )
        print ( 'INsert info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass

    def deleteData(self, id):
        response = requests.get ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI+"/" )
        print ( 'Get info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass

    def modifyData(self, entity):
        response = requests.get ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI )
        print ( 'Get info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass


class ConsumeSubjectInfo ( ConsumeService ):
    SUBJECT_URI = "subject/"

    def getInfoById(self, id):
        response = requests.get ( REST_API_URI + ConsumeSubjectInfo.SUBJECT_URI+str(id))
        print ( 'Get info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass

    def getAllInfo(self):
        response = requests.get ( REST_API_URI + ConsumeSubjectInfo.SUBJECT_URI )
        print ( 'Get All info Dept invoked....', response.status_code )
        try:
            # print(response.json())
            return response.json ()
        except:
            pass

    def insertData(self, entity):
        if entity and type ( entity ) == Subject:
            print ( entity.__dict__ )
            response = requests.post ( REST_API_URI + ConsumeSubjectInfo.SUBJECT_URI, data=entity.__dict__ )
            print ( 'Insert info Dept invoked....', response.status_code, )
            try:
                return ( response.json () )
            except:
                pass

    def deleteData(self, id):
        response = requests.delete ( REST_API_URI + ConsumeSubjectInfo.SUBJECT_URI + str ( id ) + "/" )
        print ( 'Delete info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass


    def modifyData(self, entity):
        if entity and type ( entity ) == Subject and entity.id:
            print ( REST_API_URI + ConsumeSubjectInfo.SUBJECT_URI + str ( entity.id ) )
            response = requests.put ( REST_API_URI + ConsumeSubjectInfo.SUBJECT_URI + str ( entity.id ) + "/",
                                      data=entity.__dict__ )
            print ( 'Get info Student invoked....', response.status_code, )
            try:
                return ( response.json () )
            except:
                pass

class ConsumeHobbiesInfo ( ConsumeService ):

    def getInfoById(self, id):
        response = requests.get ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI )
        print ( 'Get info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass

    def getAllInfo(self):
        response = requests.get ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI )
        print ( 'Get info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass

    def insertData(self, entity):
        response = requests.get ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI )
        print ( 'Get info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass

    def deleteData(self, entity):
        response = requests.get ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI )
        print ( 'Get info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass

    def modifyData(self, entity):
        response = requests.get ( REST_API_URI + ConsumeStudentInfo.STUDENT_URI )
        print ( 'Get info Student invoked....', response.status_code, )
        try:
            return ( response.json () )
        except:
            pass


class ConsumeDeptInfo ( ConsumeService ):
    DEPT_URI = "dept/"

    def getInfoById(self, id):
        response = requests.get ( REST_API_URI + ConsumeDeptInfo.DEPT_URI + str ( id ) )
        print ( 'Get info Dept invoked....', response.status_code )
        try:
            # print(response.json())
            return response.json ()
        except:
            pass

    def getAllInfo(self):
        response = requests.get ( REST_API_URI + ConsumeDeptInfo.DEPT_URI )
        print ( 'Get All info Dept invoked....', response.status_code )
        try:
            # print(response.json())
            return response.json ()
        except:
            pass

    def insertData(self, entity):
        if entity and type ( entity ) == Dept:
            print ( entity.__dict__ )
            response = requests.post ( REST_API_URI + ConsumeDeptInfo.DEPT_URI, data=entity.__dict__ )
            print ( 'Insert info Dept invoked....', response.status_code, )
            try:
                print ( response.json () )
            except:
                pass

    def deleteData(self, id):
        response = requests.delete ( REST_API_URI + ConsumeDeptInfo.DEPT_URI + str ( id ) + "/" )
        print ( 'Delete info Student invoked....', response.status_code, )
        try:
            print ( response.json () )
        except:
            pass

    def modifyData(self, entity):
        if entity and type ( entity ) == Dept and entity.id:
            print ( REST_API_URI + ConsumeDeptInfo.DEPT_URI + str ( entity.id ) )
            response = requests.put ( REST_API_URI + ConsumeDeptInfo.DEPT_URI + str ( entity.id ) + "/",
                                      data=entity.__dict__ )
            print ( 'Get info Student invoked....', response.status_code, )
            try:
                return ( response.json () )
            except:
                pass



if __name__ == '__main__':
    studImpl = ConsumeStudentInfo()
    studImpl.deleteData(1)
#
#     #deptConsume = ConsumeDeptInfo()
#     #deptConsume.getAllInfo()
#     #deptConsume.getInfoById(22)
#     #d = Dept(dnm="latest",dcode="ABAB",dprof="XYZ")
#     #d.id = 9
#     #deptConsume.insertData(d)
#     #deptConsume.modifyData(d)
#     #deptConsume.deleteData(9)



