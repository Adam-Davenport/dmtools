from django.shortcuts import render
from monsters.models import Monster
from monsters.forms import MonsterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
)


class Monsters(ListView):
    model = Monster
    template_name = 'monsters/index.html'

    def get_queryset(self):
        return Monster.objects.all().order_by('name')


class MonsterCreate(LoginRequiredMixin, CreateView):
    model = Monster
    template_name = 'monsters/form.html'
    form_class = MonsterForm


class MonsterDetails(DetailView):
    model = Monster
    template_name = 'monsters/details.html'

    def get_object(self, queryset=None):
        monster = super(MonsterDetails, self).get_object(queryset=queryset)
        monster.health = '{}d{}+{} ({})'.format(
            monster.level,
            monster.hit_die,
            str(monster.modifiers()[2]*monster.level),
            str(monster.level*((int(monster.hit_die/2))+1))
        )
        monster.get_attacks()
        return monster


class MonsterUpdate(LoginRequiredMixin, UpdateView):
    model = Monster
    template_name = 'monsters/form.html'
    form_class = MonsterForm


class MonsterDelete(LoginRequiredMixin, DeleteView):
    model = Monster
    template_name = 'monster/delete.html'
    success_url = '/monsters'
