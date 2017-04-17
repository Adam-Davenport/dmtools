from django.db import models

class Monster(models.Model):
	name = models.CharField(max_length=255, primary_key=True)
	challenge_rating = models.IntegerField()
	def __str__(self):
		return self.name

class Monster_Environment(models.Model):
	name = models.ForeignKey(Monster)
	amount = models.CharField(max_length=6)
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
		max_length = 128,
		choices = terrain_choices,
		default = Aquatic
	)

