from django.shortcuts import render
from .forms import FeedBacKForm

# Create your views here.
def feedbackview(request):
  form=FeedBacKForm(auto_id=False)
  if request.method=="POST":
    form=FeedBacKForm(request.POST)
    if form.is_valid():
      print('form validation sucessfull')
      print('Name:',form.cleaned_Data['name'])
      print('RollNo:',form.cleaned_Data['rollno'])
      print('Email:',form.cleaned_Data['email'])
      print('FeedBack:',form.cleaned_Data['feedback'])
  return render(request,'testapp/feedback.html',{'form':form})