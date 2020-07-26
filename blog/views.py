from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from accounts.models import Accounts
from file.models import File

def cse(request):
	file_list = File.objects.all()
	return render(request, 'cse.html', {'file_list':file_list})
	
def home(request):
  blogs = Blog.objects
  user_list = Accounts.objects.all()
  return render(request, 'home.html', {'blogs':blogs,'user_list':user_list})

"""
def detail(request, blog_id):
	blog_detail = get_object_or_404(Blog, pk = blog_id)
	#pk = 몇 번째의 객체인지를 구분해주는 변수
	#get_object_or_404(target_object, index)
	return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
	return render(request, 'new.html')

def create(request):
	blog = Blog()
	blog.title = request.GET['title']
	blog.body = request.GET['body']
	blog.pub_date = timezone.datetime.now()
	blog.save()
	
	return redirect('/blog/' + str(blog.id))
"""
#redirect = 프로젝트 밖의 외부 url 입력 가능
#render = html에 파이썬에서 다룬 변수를 넘겨줄 수 있음
