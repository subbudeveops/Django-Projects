from django.shortcuts import render
from .models import Post
from .forms import PostForm

from django.http import HttpResponse
# Create your views here.
def home(request):
  form=PostForm()

  if request=='Post':
    details=PostForm(request.POST)
    if details.is_valid():
      form=details.save(commit=True)
      form.save()    
  return render(request, "testapp/home.html", {'form':form})
