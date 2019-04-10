from abc import ABC,abstractmethod

class ConsumeService(ABC):

    @abstractmethod
    def getInfoById(self,id):
        pass

    @abstractmethod
    def getAllInfo(self):
        pass

    @abstractmethod
    def insertData(self,entity):
        pass

    @abstractmethod
    def deleteData(self,entity):
        pass

    @abstractmethod
    def modifyData(self,entity):
        pass
