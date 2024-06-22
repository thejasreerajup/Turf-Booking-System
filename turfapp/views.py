from django.shortcuts import render
from turfapp.models import *

# Create your views here.

def index(request):
	return render(request,'index.html')


def gallery(request):
	return render(request,'gallery.html')

def event(request):
	return render(request,'event.html')

def contact(request):
	return render(request,'contact.html')

def about(request):
	return render(request,'about.html')

def adminlogin(request):

	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		check=admin_tb.objects.all().filter(email=email,password=password)
		if check:
			for x in check:
				request.session['id']=x.id
				return render(request,'adminindex.html')
		else:
			return render(request,'adminlogin.html')


	else:
		return render(request,'adminlogin.html')

def addturf(request):
	if request.method=='POST':
		tname=request.POST['tname']
		category=request.POST['category']
		description=request.POST['des']
		location=request.POST['location']
		mobile=request.POST['mobile']
		email=request.POST['email']
		price=request.POST['price']
		image=request.FILES['image']
		facilities=request.POST['facilities']
		specification=request.POST['specification']
		query=turf_tb(tname=tname,category=category,description=description,location=location,mobile=mobile,email=email,price=price,image=image,facility=facilities,specification=specification)
		query.save()
		return render(request,'addturf.html')
	else:
		return render(request,'addturf.html')

def login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		check=user_tb.objects.all().filter(email=email,password=password)
		if check:
			for x in check:
				request.session['id']=x.id
				return render(request,'index.html')
		else:
			return render(request,'login.html')


	else:
		return render(request,'login.html')


def logout(request):
	if request.session.has_key('id'):
		del request.session['id']
	return render(request,'index.html')


def register(request):
	if request.method=='POST':
		name=request.POST['name']
		address=request.POST['address']
		email=request.POST['email']
		phone=request.POST['phone']
		password=request.POST['password']
		query=user_tb(name=name,address=address,email=email,contact=phone,password=password)
		query.save()
		return render(request,'contact.html')
	else:
		return render(request,'contact.html')

def userlist(request):
	ulist=user_tb.objects.all()
	return render(request,'tables.html',{'ulist':ulist})

def adminindex(request):
	return render(request,'adminindex.html')


def turf(request):
	if request.session.has_key('id'):
		uid=request.session['id']
		turfdetails=turf_tb.objects.all()
		booking_details=booking_tb.objects.all().filter(userid=uid)
		return render(request,'turf.html',{'turfdetails':turfdetails,'booking_details':booking_details})
	else:
		turfdetails=turf_tb.objects.all()
		return render(request,'turf.html',{'turfdetails':turfdetails})

def turf_details(request):
	tid=request.GET['tid']
	turfdetails=turf_tb.objects.all().filter(id=tid)
	return render(request,'bookingform.html',{'turfdetails':turfdetails})

def booking(request):
	if request.session.has_key('id'):
		if request.method=='POST':
			timefrom=request.POST['timefrom']
			timeto=request.POST['timeto']
			date=request.POST['date']
			t=request.POST['turfid']
			u=request.session['id']
			tid=turf_tb.objects.get(id=t)
			uid=user_tb.objects.get(id=u)
			a=booking_tb(userid=uid,turfid=tid,timeto=timeto,timefrom=timefrom,date=date,status='pending')
			a.save()
			uid=request.session['id']
			turfdetails=turf_tb.objects.all()
			booking_details=booking_tb.objects.all().filter(userid=uid)
			return render(request,'turf.html',{'turfdetails':turfdetails,'booking_details':booking_details})
		else:
			uid=request.session['id']
			turfdetails=turf_tb.objects.all()
			booking_details=booking_tb.objects.all().filter(userid=uid)
			return render(request,'turf.html',{'turfdetails':turfdetails,'booking_details':booking_details})
	else:
		return render(request,'login.html')


def adminviewbooking(request):
	booking_details=booking_tb.objects.all()
	return render(request,'bookinglist.html',{'booking_details':booking_details})

def approved_booking(request):
	tid=request.GET['tid']
	booking_tb.objects.all().filter(id=tid).update(status='Approved')
	booking_details=booking_tb.objects.all()
	return render(request,'turf.html',{'booking_details':booking_details})