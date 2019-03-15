
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image
# Create your views here.
def photos_of_day(request):
    date = dt.date.today()
    photos = Image.objects.all()
    
   
    return render(request, 'all_photos/today_photos.html', {"date": date, "photos": photos})      
def search_results(request):

    if 'Category' in request.GET and request.GET['Category']:
        search_images = request.GET.get("Category")
        searched_images = Image.search_by_category(search_images)
        message = f"{search_images}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})
