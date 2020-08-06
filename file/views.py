from django.shortcuts import render, get_object_or_404, redirect
from .models import File
from blog.views import get_notice_alert, get_notice_full
import os

def file_setting(request):
	file_list = File.objects.all()
	notice_list = get_notice_alert()
	return render(request, 'file_setting.html', {'file_list':file_list, 'notice_list':notice_list})

def delete_file(request, file_id):
	target = File.objects.get(pk=file_id).data.name
	File.objects.get(pk=file_id).delete()
	if os.path.isfile("uploads/" + target):
		os.remove("uploads/" + target)
	return redirect('file_setting')

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