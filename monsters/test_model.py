from monsters.models import Monster, Monster_Attacks, Monster_Environment
from django.test import TestCase


class Test_Monster_Model(TestCase):

    def setUp(self):
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

    def test_basic(self):
        monster = Monster.objects.get(name='Test Goblin')
        self.assertEqual(str(monster), 'Test Goblin')
        self.assertEqual(monster.levels, 1)
        self.assertEqual(monster.size, 'S')
        self.assertEqual(monster.modifiers(), [1, 2, -1, -2, 0, -1])

    def test_attacks(self):
        monster = Monster.objects.get(name='Test Goblin')
        monster_attack = Monster_Attacks.objects.create(
            monster=monster,
            ability_modifier='str',
            ability_damage=True,
            attack_bonus=1,
            damage_bonus=0
        )
        monster.get_attacks()
        attack = monster.attacks[0]
        monster.calculate_attack(attack)
        self.assertEqual(attack.bonus, 2)
        self.assertEqual(attack.ability_modifier, 'str')
        self.assertEqual(attack.damage_bonus, 0)
