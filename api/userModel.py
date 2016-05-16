from django.db import models

# Create your models here.

class user(models.Model):
	username=models.CharField(max_length=200)
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	tel=models.CharField(max_length=200)
	def _unicode_(self):
		return self.name