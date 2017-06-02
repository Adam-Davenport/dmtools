from django import forms
from monsters.models import Monster, Monster_Attacks, Monster_Environment


class CreateMonsterForm(forms.Form):
    model = Monster
    fields = '__all__'


class MonsterAttackForm(forms.Form):
    model = Monster_Attacks
    fields = '__all__'


class MonsterEnvironmentForm(forms.form):
    model = Monster_Environment
    fields = '__all__'
