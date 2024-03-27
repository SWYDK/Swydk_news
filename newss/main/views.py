from django.shortcuts import render
from .models import News
from django.db.models import Q
from django.http import HttpResponseNotFound

def home(request):
    search_query = request.GET.get('search','')
    isNone = ''
    if search_query:
        news1 = News.objects.filter(Q(title__icontains=search_query) | Q(anons__icontains=search_query))[:15]
        getValue = str(news1)
        getValue = getValue.replace('<QuerySet [', '')
        getValue = getValue.replace(']>', '')
        if getValue == '':
            news1=News.objects.order_by('-date')[:15]
            isNone='Ничего не найдено'
    else:
        news1 = News.objects.order_by('-date')[:15]
    if isNone == '':
        return render(request, 'home.html', {'news1':news1})
    else:
        return render(request, 'home.html', {'news1':news1, 'isNone':isNone})
        
def articlepage(request, article_id):
    article = News.objects.filter(id=article_id).first()
    if article:
        return render(request, "article.html", {"article": article})

    return HttpResponseNotFound("Article not found")


def about(request):
    return render(request,'about.html')
    