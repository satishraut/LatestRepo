from django.shortcuts import render
from .consumeapi import ConsumeSubjectInfo
from .models.SubjectInfo import Subject
from .forms.SubjFrom import SubjForm

# this is for the individual componant
# from rootconsumer.consume.consumeapi import ConsumeSubjectInfo
# from rootconsumer.consume.models.SubjectInfo import Subject


subjOperation = ConsumeSubjectInfo ()


def landingPageOne(request):
    return render ( request, 'subject.html', {"listOfSubj": subjOperation.getAllInfo (), "subjob": returnDummyObj ()} )


def returnDummyObj():
    d = Subject ( sname="", scode="", sremarks="" )
    d.id = 0
    return d


def saveSubjInfo(request):
    print ( request.POST )
    sub = Subject ( sname=request.POST['sname'], scode=request.POST['scode'], sremarks=request.POST['sremarks'] )
    if int ( request.POST['id'] ) > 0:
        sub.id = request.POST['id']
        subjOperation.modifyData ( sub )
    else:
        subjOperation.insertData ( sub )

    return render ( request, 'subject.html', {"listOfSubj": subjOperation.getAllInfo (), "subjob": returnDummyObj ()} )


def editSubj(request, id):
    obj = subjOperation.getInfoById ( id )
    print ( obj )
    return render ( request, 'subject.html', {"listOfSubj": subjOperation.getAllInfo (), "subjob": obj} )


def deleteSubj(request, id):
    print ( 'Delete Dept Id', id )
    subjOperation.deleteData ( id )
    return render ( request, 'subject.html', {"listOfSubj": subjOperation.getAllInfo (), "subjob": returnDummyObj ()} )


''' Logic end for the Department....... Starting for the subject........'''
