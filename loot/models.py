from django.db import models
from math import floor


class Loot(models.Model):
    name = models.CharField(max_length=128)
    cost = models.IntegerField()

    def expanded_cost(self):
        gold = floor(self.cost)
        remainder = (self.cost % 1) * 10
        silver = floor(remainder)
        remainder = (remainder % 1) * 10
        copper = floor(remainder)
        return [gold, silver, copper]
