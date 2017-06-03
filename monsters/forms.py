from django import forms
from monsters.models import Monster, Monster_Attacks, Monster_Environment


class MonsterForm(forms.ModelForm):
    class Meta:
        model = Monster
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'levels': forms.NumberInput(attrs={'class': 'form-control'}),
            'hit_die': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'challenge_rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'strength': forms.NumberInput(attrs={'class': 'form-control'}),
            'dexterity': forms.NumberInput(attrs={'class': 'form-control'}),
            'constitution': forms.NumberInput(attrs={'class': 'form-control'}),
            'intelligence': forms.NumberInput(attrs={'class': 'form-control'}),
            'wisdom': forms.NumberInput(attrs={'class': 'form-control'}),
            'charisma': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class MonsterAttackForm(forms.ModelForm):
    class Meta:
        model = Monster_Attacks
        fields = '__all__'


class MonsterEnvironmentForm(forms.ModelForm):
    class Meta:
        model = Monster_Environment
        fields = '__all__'
