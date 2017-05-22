from django.shortcuts import render
from monster.models import Monster
from monsters.forms import CreateMonsterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
)


class Monsters(ListView):
    model = Monster
    template_name = 'monsters/index.html'

    def get_queryset(self):
        return Monster.objects.all().order_by('name')


class Monster_Create(LoginRequiredMixin, CreateView):
    model = Monster
    template_name = 'monsters/form.html'
    form_class = CreateMonsterForm

    def get_success_url(self):
        return('/monsters/' + self.pk)


class Monster_Details(LoginRequiredMixin, DetailView):
    model = Monster
    template_name = 'monsters/details.html'


class Monster_Update(LoginRequiredMixin, UpdateView):
    model = Monster
    template_name = 'monsters/form.html'
    form_class = CreateMonsterForm


class Monster_Delete(LoginRequiredMixin, DeleteView):
    model = Monster
    template_name = 'monster/delete.html'
    success_url = '/monsters'
