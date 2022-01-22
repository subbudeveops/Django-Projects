from django import forms
from django.core import validators
def start_with_d(value):
  if value[0].lower()!='s':
    raise forms.ValidationError('Name should be start with s|S')


class FeedBacKForm(forms.Form):
  name=forms.CharField(validators=[start_with_d])
  rollno=forms.IntegerField(label='ENTER ROLLNO')
  email=forms.EmailField(required=False)
  feedback=forms.CharField()
 
 