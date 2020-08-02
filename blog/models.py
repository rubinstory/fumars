from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 500)
	pub_date = models.DateTimeField(default=timezone.now)
	body = models.TextField()
	author = models.CharField(max_length = 20, default="")
	type_of_article = models.CharField(max_length = 20, 
								choices = ( ('notice', '공지사항'),
											('blog', '게시글') ),
								default="")
	#file = models.FileField(null = True, upload_to = './file')

	#게시물의 제목이 게시판에 노출되게 하는 코드
	def __str__(self):
		if self.type_of_article == 'notice':
			return (self.title + ' / 공지사항' )
		return (self.title + ' / 게시글' )

	#게시판에서 글을 보여줄 때 글자수를 제한하는 코드 
	def summary(self):
		return self.body[:100]
