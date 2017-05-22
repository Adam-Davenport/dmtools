from django.shortcuts import render
from django.views.generic import(
    ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
)

# Create your views here.
def new(request):
    return(render('monsters/new.html'))
def monsters(request):
    return(render('monsters/show.html'))
