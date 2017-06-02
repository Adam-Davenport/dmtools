from monsters.models import Monster, Monster_Attacks, Monster_Environment
from django.test import TestCase


class Test_Monster_Model(TestCase):

    def test_name(self):
        monster = Monster.objects.create(
            name = 'Test Goblin',
        )
        self.assertEqual(str(monster), 'Test Goblin')
