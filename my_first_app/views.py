from django.shortcuts import render, HttpResponse

def home_page(request):
    print('I am responding to a url request using django')
    return render(request, "home.html")

def python_page(request):
    print('I have my request from ython page')
    return render(request, "python.html")