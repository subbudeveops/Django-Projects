from django.shortcuts import render
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index_view(request):
  return render(request,'testapp/index.html')


def add_movie_view(request):
  form=MovieForm()
  if request.method=='POST':
    form=MovieForm(request.POST)
    if form.is_valid():
      form.save()
      return index_view(request)

  return render(request,'testapp/addmovie.html',{'form':form})

def movie_list_view(request):
  movie_list=Movie.objects.all().order_by('-rating')
  return render(request,'testapp/movielist.html',{'movie_list':movie_list})