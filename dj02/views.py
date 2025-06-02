from django.shortcuts import render

def index(request):
    return render(request, 'dj02/index.html')

def day1(request):
    return render(request, 'dj02/day1.html')

def day2(request):
    return render(request, 'dj02/day2.html')

def day3(request):
    return render(request, 'dj02/day3.html')
