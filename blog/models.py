from django.db import models
# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 200)
	pub_date = models.DateField('date published')
	body = models.TextField()
	#file = models.FileField(upload_to='./file')

	#게시물의 제목이 게시판에 노출되게 하는 코드
	def __str__(self):
		return self.title

	#게시판에서 글을 보여줄 때 글자수를 제한하는 코드 
	def summary(self):
		return self.body[:100]

