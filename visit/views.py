from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.



def main(request):
    return render(request, 'Index.html')

def about_me(request):
    return render(request, 'aboutme.html')
