from django.db import models

class Bike(models.Model):
	name = models.CharField(max_length=200, default="Bici")
	characts = models.CharField(max_length=600, default="Color: Negro \n")
	price = models.FloatField(default=149.99)
	img = models.CharField(max_length=200, default="thunderbolt.jpg")

class Book(models.Model):
	title = models.CharField(max_length=50, default="El Codigo Da Vinci")
	author = models.CharField(max_length=70, default="Dan Brown")
	style = models.CharField(max_length=400, default="Aventuras")
	price = models.FloatField(default=15)
	img = models.CharField(max_length=200, default="danbrown.jpg")

class CD(models.Model):
	title = models.CharField(max_length=50, default="Jazz")
	author = models.CharField(max_length=70, default="Queen")
	style = models.CharField(max_length=30, default="Rock")
	price = models.FloatField(default=15)
	img = models.CharField(max_length=200, default="queen.jpg")
