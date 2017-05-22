from django.db import models


class Monster(models.Model):
    name = models.CharField(max_length=255)
    levels = models.IntegerField()
    challenge_rating = models.IntegerField()
    # Ability Scores
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    special_abilities = models.TextField()

    def __str__(self):
        return self.name


class Monster_Environment(models.Model):
    name = models.ForeignKey(Monster)
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
