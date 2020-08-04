from django.db import models
# Create your models here.

class File(models.Model):
	major_list = ( ('eec', '전자'),
				   ('ece', '전기'), 
			       ('cse', '컴퓨터'))

	subject = models.CharField(max_length = 200, 
							   help_text="줄임말이 아닌 수업명 입력", 
							   default="")

	major = models.CharField(max_length=20, 
		                     choices=major_list, 
		                     default="")

	note = models.CharField(max_length = 200, 
							help_text="설명 입력 ex) 텀프 파일, 수업자료...", 
							default="")

	semester = models.CharField(max_length = 200, 
								help_text="0학년 0학기와 같이 입력", 
								default="")

	data = models.FileField(null = True)

	owner = models.CharField(max_length = 200, 
							 help_text="파일 주인 이름 입력", 
							 default="")

	#게시물의 제목이 게시판에 노출되게 하는 코드
	def __str__(self):
		return (self.subject + ' / ' + self.note)
"""
class Post(models.Model):
    title = models.CharField(max_length=100, help_text='최대 100자 내로 입력가능합니다.'
    choices = (
              ('제목1', '제목 1 레이블'),
              ('제목2', '제목 2 레이블'),
              ('제목3', '제목 3 레이블'),
    ))
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators = [lnglat_validator], # 함수를 넘겨서 유효성 검사 실행
        help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
"""