from django.contrib import admin
from .models import Post
# Register your models here.
class Postadmin(admin.ModelAdmin):
  list_display=('name','text','gender')
admin.site.register(Post,Postadmin)