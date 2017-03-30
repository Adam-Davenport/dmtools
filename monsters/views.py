from django.shortcuts import render

# Create your views here.
def new(request):
    return(render('monsters/new.html'))
def monsters(request):
    return(render('monsters/show.html'))
