# from django.test import TestCase

# Create your tests here.



list1=[10,20,30,40,50,60]
list2=[40,70,80,90,10]

empyt=[]
for item in list1:
    for it in list2:
       if item==it:
           empyt.append(item)
print(empyt)