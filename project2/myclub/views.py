from pickle import GET
from django.forms import forms
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
import datetime
import calendar
from  calendar import Calendar, HTMLCalendar, month, monthcalendar 
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm,EventForm
# Create your views here.
def add_event(request):
  submitted=False
  
  if request.method=="POST":
    form=EventForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('./add_event?submitted=True')
  else:
      form=EventForm
      if 'submitted' in request.GET:

        submitted=True
  return render(request,'myclub/addevent.html',{'form':form,'submitted':submitted})

def update_venue(request,venue_id):
  venue=Venue.objects.get(pk=venue_id)
  form=VenueForm(request.POST or None,instance=venue)
  if form.is_valid():
    form .save()
    return redirect('list-venue')

  return render(request,'myclub/updatevenue.html',{'venue':venue,'form':form})

def update_event(request,event_id):
  event=Event.objects.get(pk=event_id)
  form=EventForm(request.POST or None, instance=event)
  if form.is_valid():
    form.save()
    return redirect('event_list')
  return render(request,'myclub/update_event.html',{'form':form,'event':event})

def delete_event(request,event_id):
  event=Event.objects.get(pk=event_id)
  event.delete()
  return redirect('event_list')

def search_venue(request):
  if request.method=="POST":
    searchvenue=request.POST['searchvenue']
    venues=Venue.objects.filter(name__contains=searchvenue)
    return render(request,'myclub/searchvenue.html',{'searchvenue':searchvenue,'venues':venues})


  else:
    return render(request,'myclub/searchvenue.html',{})



def show_venue(request,venue_id):
  venue=Venue.objects.get(pk=venue_id)
  return render(request,'myclub/showvenue.html',{'venue':venue})

def venue_list(request):
  venue_list=Venue.objects.all()
  return render(request,'myclub/venuelist.html',{'venue_list':venue_list})

def add_venue(request):
  form=VenueForm()
  if request.method=="POST":
    form=VenueForm(request.POST)
    if form.is_valid():
      form.save()
    return Month_Year_view(request)
  return render(request,'myclub/add_venue.html',{'form':form})

def Event_list(request):
  all_list=Event.objects.all()
  return render(request,'myclub/event_list.html',{'all_list':all_list})

def Month_Year_view(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
  name='subbareddy' 
  month=month.capitalize()
  #convert month from month name to number
  month_number=list(calendar.month_name).index(month)
  cal=HTMLCalendar().formatmonth(year,month_number)
  now=datetime.now()
  current_year=now.year
  time=now.strftime("%I:%M:%S %p")
  return render(request,'myclub/home.html',{
                          'name':name,
                          'year':year,
                          'month':month,
                          'month_number':month_number,
                          'cal':cal,
                          'now':now,
                          'current_year':current_year,
                          'time':time
                          })