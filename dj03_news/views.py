from django.shortcuts import render, get_object_or_404

from .models import NewsPost


def index(request):
    news = NewsPost.objects.all()
    return render(
        request,
        'dj03_news/index.html',
        {'news': news}
    )

def news_detail(request, pk):
    article = get_object_or_404(NewsPost, pk=pk)
    try:
        next_news = article.get_previous_by_publication_date()
    except NewsPost.DoesNotExist:
        next_news = None

    try:
        prev_news = article.get_next_by_publication_date()
    except NewsPost.DoesNotExist:
        prev_news = None
    return render(
        request,
        'dj03_news/news_detail.html',
        {'article': article,
                'prev_news': prev_news,
                'next_news': next_news,
                }
    )
