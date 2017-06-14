from django.db import models
from math import floor


class Monster(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField(default=1)
    race = models.CharField(max_length=50)
    hit_die = models.IntegerField(default=1)
    challenge_rating = models.IntegerField(default=1)
    speed = models.IntegerField(default=30)
    armor_class = models.IntegerField(default=10)
    loot = models.CharField(max_length=500)
    skills = models.CharField(max_length=50)
    senses = models.CharField(max_length=50)
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
        attack.bonus = floor((attack_ability-10)/2) + attack.attack_bonus
        attack.damage = attack.damage_bonus
        if attack.ability_damage is True:
            ability = self.get_ability(attack.ability_modifier)
            mod = self.get_modifier(ability)
            attack.damage += mod
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

    # Xp chart for challenge ratings
    def xp(self):
        chart = {
            0: 10,
            0.125: 25,
            0.25: 50,
            0.5: 100,
            1: 200,
            2: 450,
            3: 700,
            4: 1100,
            5: 1800,
            6: 2300,
            7: 2900,
            8: 3900,
            9: 5000,
            10: 5900,
            11: 7200,
            12: 8400,
            13: 10000,
            14: 11500,
            15: 13000,
            16: 15000,
            17: 18000,
            18: 20000,
            19: 22000,
            20: 25000,
            21: 33000,
            22: 41000,
            23: 50000,
            24: 62000,
            25: 75000,
            26: 90000,
            27: 105000,
            28: 120000,
            29: 135000,
            30: 155000
        }
        return chart[self.challenge_rating]

    def proficiency_bonus(self):
        lvl = self.level
        if lvl < 5:
            return 2
        elif lvl < 9:
            return 3
        elif lvl < 13:
            return 4
        elif lvl < 17:
            return 5
        else:
            return 6

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


class Monster_Special(models.Model):
    monster = models.ForeignKey(Monster)
    special = models.CharField(max_length=255)
    text = models.CharField(max_length=999)
