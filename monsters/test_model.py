from monsters.models import Monster, Monster_Attacks, Monster_Environment
from django.test import TestCase


class Test_Monster_Model(TestCase):

    def test_basic(self):
        monster = Monster.objects.create(
            name='Test Goblin',
            levels=1,
            hit_die=4,
            size='S',
            strength=12,
            dexterity=15,
            constitution=8,
            intelligence=7,
            wisdom=11,
            charisma=9
        )
        self.assertEqual(str(monster), 'Test Goblin')
        self.assertEqual(monster.levels, 1)
        self.assertEqual(monster.size, 'S')
        self.assertEqual(monster.modifiers(), [1, 2, -1, -2, 0, -1])
