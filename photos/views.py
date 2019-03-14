
from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
# Create your views here.
def photos_of_day(request):
    date = dt.date.today()
    # news = Article.todays_news()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
   
    return render(request, 'all_photos/today_photos.html', {"date": date})      
# def past_days_news(request, past_date):

#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(news_of_day)
#     news = Article.days_news(date)    

#     return render(request, 'all-news/past-news.html', {"date": date,"news":news})