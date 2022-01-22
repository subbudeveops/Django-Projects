from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import *
from django import forms
class PostForm(ModelForm):
  class Meta:
    model=Post
    fields='__all__'

  def clean(self):
    super(PostForm.self).clean()
    username=self.cleaned_data.get('name')
    text=self.cleaned_data.get('text')

    if len(username)<5:
      self._errors['username']=self.error_class(['Minimun 5 character is required'])
    
    if len(text)<10:
      self._errors['text']=self.error_class(['Minimun 10 character is required'])

    return self.cleaned_data


