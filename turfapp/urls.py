from django.urls import path
from turfapp import views

urlpatterns = [
path('',views.index),
path('gallery/',views.gallery),
path('event/',views.event),
path('contact/',views.contact),
path('about/',views.about),
path('register/',views.register),
path('login/',views.login),
path('adminlogin/',views.adminlogin),
path('addturf/',views.addturf),
path('userlist/',views.userlist),
path('adminindex/',views.adminindex),
path('turf/',views.turf),
path('turf_details/',views.turf_details),
path('logout/',views.logout),
path('booking/',views.booking),
path('adminviewbooking/',views.adminviewbooking),
path('approved_booking/',views.approved_booking)
]