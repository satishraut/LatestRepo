from rest_framework.viewsets import ModelViewSet
from .serializer import *
from .models import *

class DeptViewSet(ModelViewSet):
    serializer_class = DeptSerializer
    queryset = Department.objects.all()

class SubjectViewSet(ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class HobbiesViewSet(ModelViewSet):
    serializer_class = HobbiesSerializer
    queryset = Hobbies.objects.all()