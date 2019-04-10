from django import forms

class SubjForm(forms.Form):
    id = forms.CharField(max_length=100)
    sname= forms.CharField(max_length=100)
    scode= forms.CharField(max_length=100)
    sremarks = forms.CharField(max_length=100)
