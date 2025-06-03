from django.shortcuts import render, redirect
from .forms import NewsPostForm
from datetime import datetime

# Create your views here.

def add_article(request):
    error = ''
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.publication_date = datetime.now()
            new_post.author = request.user
            new_post.save()
            return redirect('dj03_news:index')
        else:
            error = 'Данные заполнены некорректно'
    form = NewsPostForm()
    return render(
        request,
        'dj04_forms_news/add_article.html',
        {'form': form, 'error': error}
    )
