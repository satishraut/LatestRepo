
from django.contrib import admin
from django.urls import path

# 1 Department
from .views import landingPage,saveDeptInfo,editDept,deleteDept

#2 Subject
from .subjectview import landingPageOne,saveSubjInfo,editSubj,deleteSubj

#3 Student
from .studviews import studLandingPage,sttudEdit,studDelete

urlpatterns = [

    # Thhis is for the Department
    path('index/',landingPage),
    path('save/',saveDeptInfo),
    path('edit/<int:id>',editDept),
    path('delete/<int:id>',deleteDept),

    # starting for the Subject
    path('indexone/',landingPageOne),
    path('subjsave/',saveSubjInfo),
    path('editsubj/<int:id>',editSubj),
    path('deletesubj/<int:id>', deleteSubj),

    # starting for the Student
    path('studindex/',studLandingPage),
    path('studEdit/',sttudEdit),
    path('studdelete/<int:id>',studDelete)

]