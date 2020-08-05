from django.db import models

class Accounts(models.Model):
  user_id = models.CharField(max_length = 20)
  user_name = models.CharField(max_length = 20)
  password = models.CharField(max_length = 20)
  year = models.IntegerField(default=2020,
  						  help_text = "입학년도를 4자리로 입력")
  major = models.CharField(max_length = 20, 
                         choices = ( ('eec', '전자'), ('ece', '전기'), ('cse', '컴퓨터') ),
                         default="")
  access_type = models.CharField(max_length = 20, 
  	 					  choices = ( ('temp', '승인 대기중'), ('user', '사용자'), ('admin', '관리자') ),
  	 					  default = 'temp')
  
  def __str__(self):
    return (self.user_name + ' / ' + str(self.year) + ' / ' + self.user_id)
