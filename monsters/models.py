from django.db import models


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
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    def display_abilities(self):
        attacks = Monster_Attacks.objects.filter(monster = self.pk)
        for attack in attacks:
            attack = calculate_attack(attack)

    def calculate_attack(self, attack):
        attack_ability = self.get_ability(attack.ability_modifier)
        attack.bonus = math.floor((attack_ability-10)/2)
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
    ability_modifier = models.CharField(choices=ability_choices, default='str', max_length=3)
    ability_damage = models.BooleanField()


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
        return self.name + ': ' + self.terrain
