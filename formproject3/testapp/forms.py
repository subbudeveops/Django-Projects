from django import forms
from django.core import validators
from django.forms.widgets import PasswordInput


class FeedBackForm(forms.Form):
  name=forms.CharField()
  rollno=forms.IntegerField()
  email=forms.EmailField()
  feedback=forms.CharField()

  def clean(self):
    print('Total Form Validation')
    total_cleaned_data=super().clean()
    inputname=total_cleaned_data['name']
    if inputname[0].lower()!='s':
      raise forms.ValidationError['Start Should with of name s|S']
    inputrollno=total_cleaned_data['rollno']
    if inputrollno <=0:
      raise forms.ValidationError('Rollno shouled >0')


class SingUpForm(forms.Form):
  name=forms.CharField()
  password=forms.CharField(widget=forms.PasswordInput)
  repassword=forms.CharField(label='Reenter Password',widget=forms.PasswordInput)
  email=forms.EmailField()

  def clean(self):
    total_cleaned_data=super().clean()
    pwd=total_cleaned_data['password']
    rpwd=total_cleaned_data['repassword']
    if pwd!=rpwd:
      raise forms.ValidationError('Both password must be same')
