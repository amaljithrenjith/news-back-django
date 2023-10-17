from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key='4a0e6c03fcb548eb9558ea1ae2ce9c0b')
    headlines = newsapi.get_top_headlines(sources='bbc-news')
    articles = headlines['articles']
    desc = []
    news = []
    img = []


    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])

    mylist = zip(news,desc,img)

    return render(request,"main/index.html",context={"mylist":mylist})