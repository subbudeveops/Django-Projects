from django.contrib import admin
from django.urls import path
from myclub import views

#from project2.myclub.views import template_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Month_Year_view, name='home'),
    path('<int:year>/<str:month>/', views.Month_Year_view, name='home'),
    path('event', views.Event_list, name='event_list'),
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venue', views.venue_list, name='list-venue'),
    path('show_venue/<venue_id>/', views.show_venue, name='show-venue'),
    path('search_venue', views.search_venue, name='search-venue'),
    path('update_venue/<venue_id>/', views.update_venue, name='update-venue'),
    path('update_event/<event_id>/', views.update_event, name='update-event'),
    path('delete_event/<event_id>/', views.delete_event, name='delete-event'),
    path('delete_venue/<venue_id>/', views.delete_venue, name='delete-venue'),
    path('add_event', views.add_event, name='add-event'),
    path('venue_text', views.venue_text, name='venue-text'),
    path('venue_csv', views.venue_csv, name='venue-csv'),
    path('venue_pdf', views.venue_pdf, name='venue-pdf'),

]
