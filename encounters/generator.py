from monsters.models import Monster_Environment
import random


def random_encounter(environment):
    # Assuming evnironment is already checked
    try:
        monsters = Monster_Environment.objects.all()
        for m in monsters:
            print(m.name)
    except:
        print('nope')
