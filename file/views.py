from django.shortcuts import render
from .models import File
from blog.views import get_notice_alert, get_notice_full

def cse(request): #컴퓨터공학부
	temp_list = File.objects.all()
	file_list = []
	if request.method == "POST":
		keyword = request.POST['search']
		for file in temp_list:
			if keyword in file.subject or keyword in file.note or keyword in file.semester or keyword in file.owner:
			   if file.major == 'cse':
			   	  file_list.append(file)
	else:
		for file in temp_list:
			if file.major == 'cse':
				file_list.append(file)
	notice_list = get_notice_alert()
	return render(request, 'cse.html', {'file_list':file_list, 'notice_list':notice_list})

def ece(request): #전기공학부
	temp_list = File.objects.all()
	file_list = []
	if request.method == "POST":
		keyword = request.POST['search']
		for file in temp_list:
			if keyword in file.subject or keyword in file.note or keyword in file.semester or keyword in file.owner:
			   if file.major == 'ece':
			   	  file_list.append(file)
	else:
		for file in temp_list:
			if file.major == 'ece':
				file_list.append(file)
	notice_list = get_notice_alert()
	return render(request, 'ece.html', {'file_list':file_list, 'notice_list':notice_list})

def eec(request): #전자공학부
	temp_list = File.objects.all()
	file_list = []
	if request.method == "POST":
		keyword = request.POST['search']
		for file in temp_list:
			if keyword in file.subject or keyword in file.note or keyword in file.semester or keyword in file.owner:
			   if file.major == 'eec':
			   	  file_list.append(file)
	else:
		for file in temp_list:
			if file.major == 'eec':
				file_list.append(file)
	notice_list = get_notice_alert()
	return render(request, 'eec.html', {'file_list':file_list, 'notice_list':notice_list})