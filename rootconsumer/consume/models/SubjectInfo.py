'''
"sname": "Tech",
  "scode": "C102",
  "sremarks": "Well"
'''

class Subject:
    def __init__(self,sname,scode,sremarks):
        self.sname=sname
        self.scode=scode
        self.sremarks=sremarks

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)