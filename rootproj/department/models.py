from django.db import models
from django.utils import timezone

class Department(models.Model):
    dname = models.CharField(max_length=30)
    dcode = models.CharField(max_length=30)
    dprof=models.CharField(max_length=30)

    class Meta:
        db_table = "dept_info"

#Department(dname="Information Tech",dcode="IT",dprof="AAA")

class Subject(models.Model):
    sname = models.CharField(max_length=100)
    scode = models.CharField(max_length=100)
    sremarks = models.CharField(max_length=100)

    class Meta:
        db_table = "subj_info"

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'student_{0}/{1}'.format(instance.id, filename)

'''
class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()
'''


class Student(models.Model):
    GENDER_CHOICES = (  #if you wanted to change 'M' to 'H' -- Foo.objects.filter(gender = 'M').update(gender = 'H')
        ('M', 'Male'),
        ('F', 'Female'),
    )

    fname= models.CharField(max_length=200)
    lname= models.TextField(max_length=200)
    gender= models.CharField(max_length=1, choices=GENDER_CHOICES)
    email= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    #contact= PhoneNumberField(blank=False, unique=True)
    contact = models.IntegerField()
    created_at = models.DateField(auto_now=True)  #auto_now  #add
    updated_at = models.DateField(auto_now_add=True)
    age = models.IntegerField()
    #photo= models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    #photo = models.FileField(upload_to='documents/%Y/%m/%d/')
    photo = models.FileField(upload_to=user_directory_path)
    dept = models.OneToOneField(Department, on_delete=models.CASCADE,related_name='stud')
    subjs = models.ManyToManyField(Subject,related_name="studs") #Subject.studs
    website = models.URLField(max_length=250)

    class Meta:
        db_table = "stud_info"


class Hobbies(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    stud = models.ForeignKey(Student, on_delete=models.CASCADE,related_name="hobbies")
    class Meta:
        db_table = "hobbies_info"