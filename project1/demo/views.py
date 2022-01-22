from django.shortcuts import render
from demo.models import Blog
# Create your views here.
def Display(request):
    b=Blog.objects.all()
    return render(request,'demo/demo.html',{'b':b})