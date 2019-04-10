'''
   "name": "string",
  "category": "string",
  "remarks": "string",
  "stud": 0
'''

class Hobbies:
    def __init__(self,name,category,remarks,stud):
        self.name=name
        self.category=category
        self.remarks=remarks
        self.stud=stud

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)