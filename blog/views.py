from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from accounts.models import Accounts
from file.models import File

def get_notice_full():
	article_list = Blog.objects.all()
	notice_list = []
	for article in article_list:
		if article.type_of_article == 'notice':
			notice_list.append(article)
	notice_list.reverse()
	return notice_list

def get_notice_alert():
	temp_list = get_notice_full()
	notice_list = []
	curr_time = timezone.now()
	delta = timezone.timedelta(days=7)
	for notice in temp_list:
		if curr_time - notice.pub_date <= delta:
			notice_list.append(notice)
	if len(notice_list) > 4:
		return notice_list[:5]
	return notice_list



def cse(request):
	file_list = File.objects.all()
	notice_list = get_notice_alert()
	return render(request, 'cse.html', {'file_list':file_list, 'notice_list':notice_list})

def ece(request):
	file_list = File.objects.all()
	notice_list = get_notice_alert()
	return render(request, 'ece.html', {'file_list':file_list, 'notice_list':notice_list})

def eec(request):
	file_list = File.objects.all()
	notice_list = get_notice_alert()
	return render(request, 'eec.html', {'file_list':file_list, 'notice_list':notice_list})

def user_setting(request):
	user_list = Accounts.objects.all()
	notice_list = get_notice_alert()
	return render(request, 'user_setting.html', {'user_list':user_list, 'notice_list':notice_list})
	
def home(request):
  user_list = Accounts.objects.all()
  notice_list = get_notice_alert()
  return render(request, 'home.html', {'user_list':user_list, 'notice_list':notice_list})

def notice(request):
  notice_list = get_notice_alert()
  full_notice_list = get_notice_full()
  return render(request, 'notice.html', {'notice_list':notice_list, 'full_notice_list':full_notice_list})

def write(request):
  notice_list = get_notice_alert()
  return render(request, 'write.html', {'notice_list':notice_list})

def save_notice(request):
	blog = Blog()
	blog.title = request.POST['title']
	blog.body = request.POST['body']
	blog.pub_date = timezone.datetime.now()
	blog.type_of_article = "notice"
	blog.author = request.session.get('user_name')
	blog.save()
	return redirect('/blog/notice')

def show_notice(request, blog_id):
	notice_list = get_notice_alert()
	article = get_object_or_404(Blog, pk = blog_id)
	#pk = 몇 번째의 객체인지를 구분해주는 변수
	#get_object_or_404(target_object, index)
	return render(request, 'show_notice.html', {'article':article, 'notice_list':notice_list})

def delete_user(request, user_id):
	Accounts.objects.get(pk=user_id).delete()
	user_list = Accounts.objects.all()
	return redirect('user_setting')
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
