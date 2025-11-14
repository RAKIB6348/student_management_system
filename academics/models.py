from django.db import models

# Create your models here.
class StudentClass(models.Model):
	name = models.CharField(max_length=20)
	code = models.CharField(max_length=2)

	def __str__(self):
		return self.name
