from django.urls import path
from turfapp import views

urlpatterns = [

# Home Pages
path('',views.index),
path('gallery/',views.gallery),
path('event/',views.event),
path('contact/',views.contact),
path('about/',views.about),

# User Pages
path('login/',views.login),
path('turf/',views.turf),
path('turf_details/',views.turf_details),

# Admin Pages
path('adminlogin/',views.adminlogin),
path('addturf/',views.addturf),
path('userlist/',views.userlist),
path('adminindex/',views.adminindex),
path('adminviewbooking/',views.adminviewbooking),

# Backend Actions
path('register/',views.register),
path('logout/',views.logout),
path('booking/',views.booking),
path('check_booking/',views.check_booking),
path('adminlogout/',views.adminlogout),
path('approved_booking/',views.approved_booking),

# Test Pages
path('test/',views.test),
]