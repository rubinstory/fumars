from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Accounts


def signup(request):
  user_list = Accounts.objects.all()
  if request.method == "POST":
   for user in user_list:
    if user.user_id == request.POST["user_id"]:
      messages.error(request, '이미 존재하는 아이디입니다')
      return render(request, 'signup.html')
   if request.POST["password_1"] != request.POST["password_2"]:
    messages.error(request, '비밀번호가 일치하지 않습니다')
    return render(request, 'signup.html')
   elif len(request.POST["password_1"]) < 8:
    messages.error(request, '비밀번호는 8자리 이상이어야 합니다')
    return render(request, 'signup.html')
   elif len(request.POST["year"]) != 4:
    messages.error(request, '입학년도는 4자리여야 합니다')
    return render(request, 'signup.html')
   elif request.POST["major"] != "전기" and request.POST["major"] != "컴퓨터":
    messages.error(request, '전공명을 정학히 입력하세요. [전기] 또는 [컴퓨터]로 입력하셔야 합니다.')
    return render(request, 'signup.html')
   else:
    user = Accounts()
    user.user_id = request.POST["user_id"]
    user.user_name = request.POST["user_name"]
    user.password = request.POST["password_1"]
    user.year = request.POST["year"]
    if request.POST["major"] == "전기":
      user.major = "ece"
    else:
      user.major = "cse"
    user.save()
    return render(request, 'signup_success.html')
  else:
    return render(request, 'signup.html') #POST 방식으로 접속한게 아닐 때
  

def login(request):
  id_check = False

  if request.session.get('user') == True:
    return redirect('home')
  if request.method == "POST":
    user_list = Accounts.objects.all()
    for user in user_list:
     if user.user_id == request.POST["user_id"]:
       id_check = True
       if user.password == request.POST["password"]:
         request.session['user'] = request.POST["user_id"]
         request.session['user_name'] = user.user_name
         request.session['user_type'] = user.access_type
         #print(request.session.get('user_id'))
         next_url = request.POST["next_url"]
         return redirect(next_url)
  else:
    next_url = request.GET['next_url']
    return render(request, 'login.html', {'next_url':next_url}) #POST 방식으로 접속한게 아닐 때
	
  if not id_check:
    messages.error(request, '아이디가 존재하지 않습니다')
  else:
    messages.error(request, '비밀번호가 틀렸습니다')
  next_url = request.POST["next_url"]
  return render(request, 'login.html', {'next_url':next_url})


def logout(request):
    if request.session.get('user') is False:
      return redirect('home')
    request.session.pop('user_type')
    request.session.pop('user')
    request.session.pop('user_name')
    return redirect('home')

def home(request):
  return render(request, 'home.html')
