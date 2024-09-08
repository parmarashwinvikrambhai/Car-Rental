from django.urls import path
from django.contrib import admin
from  clinet_site.c_views import *


urlpatterns = [

    path('home/',home),
    path('car_list/',car_list),
    path('search0/',autosuggest,name='search2'),
    path('car_list_search/',car_list_search),
    path('car_details/<int:cars_id>/',car_details),
    path('booked_car/',booked_car),
    path('booking_car/',booking_car),
    path('bookingdetail/<int:booked_id>/',booking_detail),
    path('user_aboutus/',user_aboutus),
    path('user_signin/',clinet_login),
    path('user_signup',user_register),
    path('user_forgot/',user_forgot),
    path('user_send/',send_otp),
    path('user_setpass/',set_password),
    path('client_header_menu/',load_menu),
    path('user_profile/',user_profile),
    path('user_update/',user_update),
    path('payment/<int:booking_id>/',payment),
    path('car_list_comp/<int:com_id>/',car_list_comp),
    path('user_logout/',user_logout),
    path('payment/<int:booking_id>/',payment),
    path('fliter/<str:str>/<str:str1>/',filter1),
    path('paymentMOdule/<int:booking_id>/', paymentMOdule),
    path('cancel/<int:id>/', cancelBooking),
]