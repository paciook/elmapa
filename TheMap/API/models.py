from django.db import models

# Create your models here.

class Casilla(models.Model):
	y = models.CharField(max_length = 2)
	x = models.CharField(max_length = 2)
	color = models.CharField(max_length = 20)