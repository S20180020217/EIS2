from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from jobs.models import Job
def home(request):
  return render(request,'a.html')
def form(request):
	return render(request,'formaction.html')
def signin(request):
	userid=request.GET['userid']
	password=request.GET['password']
	if userid=="S20180020217" and password=="123456":	
		return render(request, 'table.html', {"details":Job.objects.all()})
	else:
		return HttpResponse('invalid user')

@csrf_exempt
def submit(request):
	if request.method == "POST":
		j = Job()
		j.latitude = request.POST["latitude"]
		j.longitude = request.POST["longitude"]
		j.image1 = request.POST["image1"]
		j.image2 = request.POST["image2"]
		j.image3 = request.POST["image3"]
		j.save()
		return HttpResponse("Successfully Submitted")
	else:
		return HttpResponse("Failed")
	
