from django import forms
from monsters.models import Monster, Monster_Attacks, Monster_Environment


class MonsterForm(forms.Form):
    model = Monster
    fields = '__all__'


class MonsterAttackForm(forms.Form):
    model = Monster_Attacks
    fields = '__all__'


class MonsterEnvironmentForm(forms.Form):
    model = Monster_Environment
    fields = '__all__'
