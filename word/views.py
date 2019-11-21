from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  return render(request,'a.html')
def form(request):
	return render(request,'formaction.html')
def count(request):
	email=request.GET['userid']
	passWord=requst.Get['password']
	return render(request,'count.html',{'email':email})
def about(request):
	return render(request,'about.html')