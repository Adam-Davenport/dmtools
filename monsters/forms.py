from django.forms import ModelForm
from monsters.models import Monster, Monster_Attacks, Monster_Environment


class MonsterForm(ModelForm):
    class Meta:
        model = Monster
        fields = '__all__'


class MonsterAttackForm(ModelForm):
    class Meta:
        model = Monster_Attacks
        fields = '__all__'


class MonsterEnvironmentForm(ModelForm):
    class Meta:
        model = Monster_Environment
        fields = '__all__'
