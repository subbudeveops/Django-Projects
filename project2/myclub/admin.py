
from django.contrib import admin
from django.db.models import fields
from .models import Event
from .models import MyClubUser
from .models import Venue

 
# Register your models here.

admin.site.register(MyClubUser)

class VenueAdmin(admin.ModelAdmin):
  list_display=('name','address','phone')
  ordering=('name',)
  search_fields=('name','phone',)
  
admin.site.register(Venue,VenueAdmin)


class EventAdmin(admin.ModelAdmin):
  fields=('name', 'venue','event_date','manager','description','attends',)
  list_display=('name','venue','event_date','manager')
  list_filter=('event_date','venue')
  ordering=('-event_date',)
admin.site.register(Event,EventAdmin)


