
from django.forms import forms
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
import datetime
import calendar
from calendar import Calendar, HTMLCalendar, month, monthcalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm, EventFormAdmin
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.models import User
# import pdf attributes
import csv
import reportlab
from django.http import FileResponse
import io
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# import for create pagigations f
from django.core.paginator import Paginator


# Create your views here.

# Generate odf file venuelist9


def venue_pdf(request):
    buff = io.BytesIO()
    c = canvas.Canvas(buff, pagesize=letter, bottomup=0)
    p = c.beginText()
    p.setTextOrigin(inch, inch)
    p.setFont("Helvetica", 14)
    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append(
            " == == == == == == == == == == == == == == == == == == == == == == == == == == ==")

    for line in lines:
        p.textLine(line)
    c.drawText(p)
    c.showPage()
    c.save()
    buff.seek(0)
    return FileResponse(buff, as_attachment=True, filename='venue.pdf')


def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venue.csv'
    # create csv writer
    writer = csv.writer(response)
    venues = Venue.objects.all()
    # Add Colum heading to the csv filename
    writer.writerow(['Venue Name', 'Address', 'ZIP_CODE',
                    'PhoneNo', 'Website', 'EmailId'])
    for venue in venues:
        writer.writerow(
            [venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])
    return response


def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = venue.txt'
    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(
            f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n')
    # lines = ["This line one\n", "This is line 2\n"]
    response.writelines(lines)
    return response


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venue')


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.manager:
        event.delete()
        messages.success(request, ("Event Deleted!!!!"))
        return redirect('event-list')
    else:
        messages.success(
            request, ("Your are not authoeized to Delete this Event"))
        return redirect('event-list')


def add_event(request):
    submitted = False

    if request.method == "POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('./add_event?submitted=True')
        else:

            form = EventFormAdmin(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.manage = request.user
                event.save()
    else:
        if request.user.is_superuser:
            form = EventFormAdmin
        else:
            form = EventForm()

        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'myclub/addevent.html', {'form': form, 'submitted': submitted})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form .save()
        return redirect('list-venue')
    return render(request, 'myclub/updatevenue.html', {'venue': venue, 'form': form})


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'myclub/update_event.html', {'form': form, 'event': event})


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('event_list')


def search_venue(request):
    if request.method == "POST":
        searchvenue = request.POST['searchvenue']
        venues = Venue.objects.filter(name__contains=searchvenue)
        return render(request, 'myclub/searchvenue.html', {'searchvenue': searchvenue, 'venues': venues})
    else:
        return render(request, 'myclub/searchvenue.html', {})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    # this logic is VenuEe Owner name and email getting details
    venue_owner = User.objects.get(pk=venue.owner)sh
    return render(request, 'myclub/showvenue.html', {'venue': venue, 'venue_owner': venue_owner})


def venue_list(request):
    #venue_list = Venue.objects.all().order_by('name')
    venue_list = Venue.objects.all()
    # setup pagenation for venue
    p = Paginator(Venue.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    return render(request, 'myclub/venuelist.html', {'venue_list': venue_list, 'venues': venues})


def add_venue(request):
    form = VenueForm()
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            # form.save()
        return Month_Year_view(request)
    return render(request, 'myclub/add_venue.html', {'form': form})


def Event_list(request):
    all_list = Event.objects.all().order_by('name')
    return render(request, 'myclub/event_list.html', {'all_list': all_list})


def Month_Year_view(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'subbareddy'
    month = month.capitalize()
    # convert month from month name to number
    month_number = list(calendar.month_name).index(month)
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year
    time = now.strftime("%I:%M:%S %p")
    return render(request, 'myclub/home.html', {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'now': now,
        'current_year': current_year,
        'time': time
    })
