from django.shortcuts import render
from .forms import DeptForm
from .models.DeptInfo import Dept

from .consumeapi import ConsumeDeptInfo


deptOperation = ConsumeDeptInfo()
def landingPage(request):
    return render(request, 'dept.html', {"listOfDepts" : deptOperation.getAllInfo(),"deptob":returnDummyObj()})

def returnDummyObj():
    d = Dept(dnm="",dcode="",dprof="")
    d.id=0
    return d

def saveDeptInfo(request):
    print(request.POST)
    dept=Dept(dnm=request.POST['dname'],dcode=request.POST['dcode'],dprof=request.POST['dprof'])
    if int(request.POST['id'])>0:
        dept.id=request.POST['id']
        deptOperation.modifyData(dept)
    else:
        deptOperation.insertData(dept)

    return render(request, 'dept.html',{"listOfDepts":deptOperation.getAllInfo(),"deptob":returnDummyObj()})

def editDept(request,id):
    print('Edit Dept Id', id)
    obj = deptOperation.getInfoById(id)
    print(obj)
    return render(request, 'dept.html', {"listOfDepts": deptOperation.getAllInfo(),'deptob':obj})

def deleteDept(request,id):
    print('Delete Dept Id', id)
    deptOperation.deleteData(id)
    return render(request, 'dept.html', {"listOfDepts": deptOperation.getAllInfo(),"deptob":returnDummyObj()})

''' Logic end for the Department....... Starting for the subject........'''

