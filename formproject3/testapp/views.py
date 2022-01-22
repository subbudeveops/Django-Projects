from django.shortcuts import render
from .forms import FeedBackForm,SingUpForm
# Create your views here.
def feedback_view(request):
  form=FeedBackForm()
  if request.method=='POST':
    form=FeedBackForm(request.POST)
    if form.is_valid():
      print('Basic Validation Completed and Printing Data') 
      print('Name:',form.cleaned_data['name']) 
      print('RollNo:',form.cleaned_data['rollno']) 
      print('Email:',form.cleaned_data['email']) 
      print('Feedback:',form.cleaned_data['feedback'])
  return render(request,'testapp/feedback.html',{'form':form})

def singup_view(request):
  form=SingUpForm()
  if request.method=='POST':
    form=SingUpForm(request.POST)
    if form.is_valid():
      print('Basic validation completed')
      print('Name:',form.cleaned_data['name']) 
      print('Password:',form.cleaned_data['password']) 
      print('Email:',form.cleaned_data['email']) 
  return render(request,'testapp/singup.html',{'form':form})
