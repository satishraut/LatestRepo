from django import forms

class DeptForm(forms.Form):
    id = forms.CharField(max_length=100)
    name= forms.CharField(max_length=100)
    code= forms.CharField(max_length=100)
    prof = forms.CharField(max_length=100)
