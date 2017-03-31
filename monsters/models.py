from django.db import models

class Monster(models.Model):
	name = models.CharField(max_length=255)
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
	# Applying terrain choices
	terrain = models.CharField(
		max_length = 128,
		choices = terrain_choices,
		default = Aquatic)

