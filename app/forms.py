from django import forms

def check(value):
    if value[0]=='s':
        raise forms.ValidationError('it should not start with s')

class StudentForms(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField(max_length=100,validators=[check])
    sage=forms.IntegerField()
