from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request , 'main/about.html')
def services(request):
    return render(request , 'main/services.html')
def blog(request):
    return render(request , 'main/blog.html')

