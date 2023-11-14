from django.shortcuts import redirect, render
from article.models import Article

def index(request):
    articles = Article.objects.all()  # Corrected variable name
    context = {'articles': articles}  # Corrected variable name
    print(context)
    return render(request, 'article/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}  # Corrected variable name
    return render(request, 'article/detail.html', context)

def new(request):
    return render(request, 'article/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article(title=title, content=content)
    article.save()
    
    return redirect('article:index')

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article' : article}
    return render(request, 'article/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('article:detail', article.pk)