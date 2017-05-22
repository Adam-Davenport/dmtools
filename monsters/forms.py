from django import forms
from monsters.models import Monster


class CreateMonsterForm(forms.Form):
    model = Monster
    fields = __all__
