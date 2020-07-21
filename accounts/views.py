from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	if request.method == "POST":
		if request.POST["password_1"] == request.POST["password_2"]:
			user = User.objects.create_user(
				username = request.POST["username"],
				password = request.POST["password_1"])
			auth.login(request, user)
			return redirect('home')
		return render(request, 'signup.html', {'error':'password incorrect'})
	return render(request, 'signup.html', {'error':'FATAL ERROR : SECURITY BREACH'})

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request, username = username, password = password)

		if user is not None:
			#auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'login.html', {'error':'아이디 혹은 비밀번호가 틀렸습니다.'})
	else:
		return render(request, 'login.html', {'error':'아이디 '})

	


	return render(request, 'login.html')

def logout(request):
	return render(request, 'login.html')
