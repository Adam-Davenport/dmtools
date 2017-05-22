from django.shortcuts import render
from monster.models import Monster
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
)


class Monsters(ListView):
    model = Monster
    template_name = 'monsters/index.html'

    def get_queryset(self):
        return Monster.objects.all().order_by('name')


class Create_Monster(CreateView):
    model = Monster
    template_name = 'monsters/new.html'
