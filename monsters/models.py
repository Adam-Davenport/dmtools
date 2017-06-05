from django.db import models
from math import floor


class Monster(models.Model):
    name = models.CharField(max_length=255)
    levels = models.IntegerField(default=1)
    hit_die = models.IntegerField(default=1)
    # Monster size
    size_choices = (
        ('T', 'Tiny'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('H', 'Huge'),
        ('G', 'Gargantuan')
    )
    size = models.CharField(choices=size_choices, default='M', max_length=1)
    challenge_rating = models.IntegerField(default=1)
    # Ability Scores
    strength = models.IntegerField(default=10, blank=True)
    dexterity = models.IntegerField(default=10, blank=True)
    constitution = models.IntegerField(default=10, blank=True)
    intelligence = models.IntegerField(default=10, blank=True)
    wisdom = models.IntegerField(default=10, blank=True)
    charisma = models.IntegerField(default=10, blank=True)

    def get_attacks(self):
        self.attacks = Monster_Attacks.objects.filter(monster=self.pk)
        for attack in self.attacks:
            attack = self.calculate_attack(attack)

    def calculate_attack(self, attack):
        attack_ability = self.get_ability(attack.ability_modifier)
        attack.bonus = floor((attack_ability-10)/2)
        return attack

    def get_ability(self, ability):
        abilities = {
            'str': self.strength,
            'dex': self.dexterity,
            'con': self.constitution,
            'int': self.intelligence,
            'wis': self.wisdom,
            'cha': self.charisma
        }
        return abilities[ability]

    # Get the modifier of a given ability score
    def get_modifier(self, ability):
        mod = floor((ability-10)/2)
        return mod

    # Get the modifier of all ability scores in a list
    def modifiers(self):
        modifiers = [
            self.get_modifier(self.strength),
            self.get_modifier(self.dexterity),
            self.get_modifier(self.constitution),
            self.get_modifier(self.intelligence),
            self.get_modifier(self.wisdom),
            self.get_modifier(self.charisma)
        ]
        return modifiers

    def __str__(self):
        return self.name


class Monster_Attacks(models.Model):
    monster = models.ForeignKey(Monster)
    # Ability score choices
    ability_choices = (
        ('str', 'Strength'),
        ('dex', 'Dexterity'),
        ('con', 'Constitution'),
        ('int', 'Intelligence'),
        ('wis', 'Wisdom'),
        ('cha', 'Charisma')
    )
    ability_modifier = models.CharField(
        choices=ability_choices,
        default='str',
        max_length=3)
    ability_damage = models.BooleanField()
    attack_bonus = models.IntegerField()
    damage_bonus = models.IntegerField()


class Monster_Environment(models.Model):
    monster = models.ForeignKey(Monster)
    # Setting up choices for environments
    Aquatic = 'Aquatic'
    Desert = 'Desert'
    Forest = 'Forest'
    Hill = 'Hill'
    Marsh = 'Marsh'
    Plain = 'Plain'
    Underground = 'Underground'
    terrain_choices = (
        (Aquatic, 'Aquatic'),
        (Desert, 'Desert'),
        (Forest, 'Forest'),
        (Hill, 'Hill'),
        (Marsh, 'Marsh'),
        (Plain, 'Plain'),
        (Underground, 'Underground')
    )
    terrain = models.CharField(
        max_length=128,
        choices=terrain_choices,
        default=Aquatic
    )

    def __str__(self):
        return self.monster + ': ' + self.terrain
