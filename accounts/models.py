from django.db import models

class Accounts(models.Model):
  user_id = models.CharField(max_length = 20)
  user_name = models.CharField(max_length = 20)
  password = models.CharField(max_length = 20)
  
  def __str__(self):
    return self.user_name
