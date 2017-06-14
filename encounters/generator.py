from monsters.models import Monster_Environment, Monster
import random


class Random_Encounter():

    def __init__(self, environment):
        self.environment = environment
    
    def get_monsters(self):
        monsters = Monster.objects.filter(environment=self.environment)
