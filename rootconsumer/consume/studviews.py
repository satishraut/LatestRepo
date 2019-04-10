from django.shortcuts import render
from .consumeapi import ConsumeStudentInfo
from .models.StudentInfo import Student

studOp=ConsumeStudentInfo()


def studLandingPage(request):
    return render ( request, 'student.html', {"listOfStud": studOp.getAllInfo(), "studOb": returnDummyObj()})


def returnDummyObj():
      s1=Student(fname="",lname="",gender="",email="",address="",contact="",age="",subjs="",photo="",website="",dept="")
      s1.id=0
      return s1


def saveStud(request):
    print(request.POST)
    stud=Student(fname=request.POST['fname'],lname=request.POST['lname'],
                 gender=request.POST['gender'],email=request.POST['email'],
                 address= request.POST['address'],contact=request.POST['contact'],
                 age=request.POST['age'],website=request.POST['website'],
                 dept=request.POST['dept'],subjs=request.POST['subj'],photo=request.POST['photo'])
    if int(request.POST['id'])>0:
        stud.id=request.POST['id']
        studOp.modifyData(stud)
    else:
        studOp.insertData(stud)

    return render(request, 'student.html',{"listOfDepts":studOp.getAllInfo(),"studOb":returnDummyObj()})

def sttudEdit(request, id):
    obj=studOp.getInfoById(id)
    print(obj)
    return render(request,'student.html',{"listOfStud":studOp.getAllInfo(), "studOb":obj})

def studDelete(request, id):
    print('Delete the stud id', id)
    studOp.deleteData(id)
    print(studOp)
    return render(request,'student.html',{"listOfStud":studOp.getAllInfo(),"studOb":returnDummyObj()})










