from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def student_view(request):
  sent=False
  if request.method=="POST":
    form=StudentForm(request.POST)
    if form.is_valid():
      print('FROM VALIDATION COMPLETE')
      print('Name:',form.cleaned_data['name'])
      print('Marks:',form.cleaned_data['marks'])
      sent=True
  form=StudentForm()
  return render(request,'testapp/input.html',{'form':form,'sent':sent})
