from django.shortcuts import render
from monster.models import Monster
from monsters.forms import CreateMonsterForm
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
)


class Monsters(ListView):
    model = Monster
    template_name = 'monsters/index.html'

    def get_queryset(self):
        return Monster.objects.all().order_by('name')


class Monster_Create(CreateView):
    model = Monster
    template_name = 'monsters/form.html'
    form_class = CreateMonsterForm


class Monster_Update(UpdateView):
    model = Monster
    template_name = 'monsters/form.html'
    form_class = CreateMonsterForm
