from django.db import models

class User(models.Model):
  email = models.CharField(max_length=60)
  password = models.CharField(max_length=120)

  def __str__(self):
      return self.email
