from django.db import models

# Create your models here.
class user_tb(models.Model):
	name=models.CharField(max_length=500,default='')
	address=models.CharField(max_length=500,default='')
	email=models.CharField(max_length=500,default='')
	contact=models.CharField(max_length=500,default='')
	password=models.CharField(max_length=500,default='')

class turf_tb(models.Model):
	tname=models.CharField(max_length=500,default='')
	category=models.CharField(max_length=500,default='')
	description=models.CharField(max_length=500,default='')
	location=models.CharField(max_length=500,default='')
	mobile=models.CharField(max_length=500,default='')
	email=models.CharField(max_length=500,default='')
	price=models.CharField(max_length=500,default='')
	image=models.ImageField(upload_to='files')
	facility=models.CharField(max_length=500,default='')
	specification=models.CharField(max_length=500,default='')


class booking_tb(models.Model):
	userid=models.ForeignKey(user_tb,on_delete=models.CASCADE)
	turfid=models.ForeignKey(turf_tb,on_delete=models.CASCADE)
	timeto=models.CharField(max_length=30,default='')
	timefrom=models.CharField(max_length=30,default='')
	date=models.CharField(max_length=30,default='')
	payment_id=models.CharField(max_length=50,default='')
	status=models.CharField(max_length=30,default='')

class admin_tb(models.Model):
	email=models.CharField(max_length=500,default='')
	password=models.CharField(max_length=500,default='')