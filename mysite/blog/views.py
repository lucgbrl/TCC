from django.shortcuts import render
#from . import views
# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})