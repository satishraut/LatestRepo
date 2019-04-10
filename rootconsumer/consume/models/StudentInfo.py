
class Student:
    def __init__(self,fname,lname,gender,email,address,contact,age,website,dept,subjs,photo):
        self.subjs=[]
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.email=email
        self.address=address
        self.contact=contact
        self.age=age
        self.website=website
        self.dept=dept
        self.subjs.extend(subjs)
        self.photo=photo

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)