from cProfile import label
from datetime import datetime
from msilib.schema import Control
from django import forms
from django.forms import widgets
import datetime
from .models import Venue,Event

#create Forms
class VenueForm(forms.ModelForm):
  class Meta:
    model=Venue
    #fields=('name','address','zip_code','phone','web','email_address')
    fields="__all__"
    labels={
      'name':'',
      'address':'',
      'zip_code':'',
      'phone':'',
      'web':'',
      'email_address':'',

    }
    widgets={
      'name':forms.TextInput(attrs={'class':"form-control",'placeholder':"Venue Name"}),
      'address':forms.TextInput(attrs={'class':"form-control",'placeholder':"Venue Address"}),
      'zip_code':forms.TextInput(attrs={'class':"form-control",'placeholder':"ZIP_CODE"}),
      'phone':forms.TextInput(attrs={'class':"form-control",'placeholder':"PHONE"}),
      'web':forms.TextInput(attrs={'class':"form-control",'placeholder':"WEB ADDRESS"}),
      'email_address':forms.TextInput(attrs={'class':"form-control",'placeholder':"EMAIL ID"}),
      }



class EventForm(forms.ModelForm):
  class Meta:
    model=Event
    fields="__all__"
    labels={
      'name':'',
      'event_date':'',
      'venue':'',
      'manager':'',
      'description':'',
      'attends':'',
    }
    widgets={
      'name':forms.TextInput(attrs={'class':"form-control",'placeholder':"Event Name"}),
      'event_date':forms.SelectDateWidget(attrs={'class':"form-control",'placeholder':"Event Date"}),
      'venue':forms.Select(attrs={'class':"form-select",'placeholder':"Venue"}),
      'manager':forms.Select(attrs={'class':"form-select",'placeholder':"Manager"}),
      'description':forms.Textarea(attrs={'class':"form-control",'placeholder':"Description"}),
      'attends':forms.SelectMultiple(attrs={'class':"form-control",'placeholder':"Attend"}),
      }

    