from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from turfapp.models import *
import qrcode

# Create your views here.

def index(request):
	"""
	Home Page
	"""
	return render(request,'index.html')

def gallery(request):
	return render(request,'gallery.html')

def test(request):
	"""
	Test Function Request
	"""
	# result_render = render(request,'test.html')
	result_render = render(request,"test.html")
	return result_render

def event(request):
	return render(request,'event.html')

def contact(request):
	'''
		Sign Up Page
	'''
	if request.session.has_key('id'):
		# Redirect if Already Login
		return redirect("/")
	else:
		return render(request,'contact.html')

def about(request):
	return render(request,'about.html')

def adminlogin(request):
	"""
	Admin Login
	"""
	if request.session.has_key('id'):
		# Redirect if Already Login
		return redirect("/adminindex/")
	if request.method=='POST':
		# On Submitting Form
		email=request.POST['email']
		password=request.POST['password']
		check=admin_tb.objects.all().filter(email=email,password=password)
		if check:
			for x in check:
				request.session['id']=x.id
				return redirect('/adminindex')
		else:
			return render(request,'adminlogin.html')


	else:
		return render(request,'adminlogin.html')

def addturf(request):
	"""
	Create Turf Request
	"""
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
	"""
	User Login Page with Request Validation
	"""
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		check=user_tb.objects.all().filter(email=email,password=password)
		if check:
			for x in check:
				request.session['id']=x.id
				return redirect('/turf')
		else:
			return render(request,'login.html')


	else:
		return render(request,'login.html')


def logout(request):
	"""
	Route to logout user Delete Session keys
	"""
	if request.session.has_key('id'):
		del request.session['id']
	return render(request,'index.html')

def adminlogout(request):
	if request.session.has_key('id'):
		del request.session['id']
	return redirect("/adminlogin")


def register(request):
	"""
	Register New User
	"""
	if request.method=='POST':
		name=request.POST['name']
		address=request.POST['address']
		email=request.POST['email']
		phone=request.POST['phone']
		password=request.POST['password']
		query=user_tb(name=name,address=address,email=email,contact=phone,password=password)
		query.save()
		return redirect("/login")
	else:
		return render(request,'contact.html')

def userlist(request):
	ulist=user_tb.objects.all()
	return render(request,'tables.html',{'ulist':ulist})

def adminindex(request):
	if request.session.has_key('id'):
		return render(request,'adminindex.html')
	else:
		return redirect("/adminlogin")


def turf(request):
	"""
	Turf Details To book and booking Request Action
	"""
	if request.session.has_key('id'):
		uid=request.session['id']

		# Filter on Category
		if request.method == 'POST':
			cat = request.POST['Category']
			turfdetails=turf_tb.objects.all().filter(category__icontains = cat)
		else:
			turfdetails=turf_tb.objects.all()
			
		booking_details=booking_tb.objects.all().filter(userid=uid)
		return render(request,'turf.html',{'turfdetails':turfdetails,'booking_details':booking_details})
	else:
		# Filter on Category
		if request.method == 'POST':
			cat = request.POST['Category']
			turfdetails=turf_tb.objects.all().filter(category__icontains = cat)
		else:
			turfdetails=turf_tb.objects.all()
		return render(request,'turf.html',{'turfdetails':turfdetails})

def turf_details(request):
	tid=request.GET['tid']
	turfdetails=turf_tb.objects.all().filter(id=tid)
	category = turfdetails[0].category.split(',')
	qrcode.make(turfdetails[0].mobile + '@upi').save('static/images/payment_qr.png')
	return render(request,'bookingform.html',{'turfdetails':turfdetails, 'category':category})

def check_booking(request):
	"""
	Action Route to ckeck If already booked
	"""
	tid=int(request.GET['turfid'])
	date = request.GET.get('date')
	timefrom = request.GET.get('timefrom')
	timeto = request.GET.get('timeto')

	bookingFrom = booking_tb.objects.filter(
		turfid=tid,
		date=date,
		timefrom=timefrom,
	)

	bookingTo = booking_tb.objects.filter(
		turfid=tid,
		date=date,
		timeto=timeto,
	)

	BookingTimeFrame = booking_tb.objects.filter(
		Q(timefrom__lt=timeto) & Q(timeto__gt=timefrom),
		turfid=tid,
		date=date
	)
	text = 'Booking Is Available'

	if(BookingTimeFrame.exists()):
		text = "Booking not available From "+str(timefrom)+" To "+str(timeto)
		is_available = False
	elif(bookingFrom.exists()):
		is_available = False
		text = "Booking not available From "+str(timefrom)
	elif(bookingTo.exists()):
		is_available = False
		text = "Booking not available To "+str(timeto)
	else:
		is_available = True
		

	return JsonResponse({'available': is_available, 'text':text})

def booking(request):
	"""
	Turf Booking Request Action
	"""
	if request.session.has_key('id'):
		if request.method=='POST':
			timefrom=request.POST['timefrom']+":00"
			timeto=request.POST['timeto']+":00"
			date= request.POST['date']
			category= request.POST['category']
			ttime= request.POST['ttime']
			tprice= request.POST['tprice']
			payment_id=request.POST['payment-id']
			t=request.POST['turfid']
			u=request.session['id']
			tid=turf_tb.objects.get(id=t)
			uid=user_tb.objects.get(id=u)
			a=booking_tb(
				userid=uid,
				turfid=tid,
				timeto=timeto,
				timefrom=timefrom,
				date=date,
				status='pending',
				payment_id=payment_id,
				category=category,
				ttime=ttime,
				tprice=tprice)
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
		return redirect('/login')


def adminviewbooking(request):
	booking_details=booking_tb.objects.all()
	return render(request,'bookinglist.html',{'booking_details':booking_details})

def approved_booking(request):
	tid=request.GET['tid']
	booking_tb.objects.all().filter(id=tid).update(status='Approved')
	booking_details=booking_tb.objects.all()
	return render(request,'turf.html',{'booking_details':booking_details})


def turflist(request):
  tlist=turf_tb.objects.all()
  return render(request,'turflist.html',{'tlist':tlist})


def deleteturf(request):
	"""
	Delete Turf Action
	"""
	tid=request.GET['tid']
	turf_tb.objects.all().filter(id=tid).delete()
	return True

