from rest_framework.serializers import ModelSerializer
from .models import Subject,Student,Department,Hobbies

class DeptSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    # dept=DeptSerializer(required=True)
    class Meta:
        model = Student
        exclude = ('created_at','updated_at')

class HobbiesSerializer(ModelSerializer):
    #stud = StudentSerializer ( required=True )
    class Meta:
        model = Hobbies
        fields = '__all__'