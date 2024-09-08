"""car_rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from clinet_site import c_views
from admin_site import views
import clinet_site
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.client_view),
    path('client/',include('clinet_site.c_urls')),
    path('admin_index/',views.home),
    path('user_tabel/',views.user_tabel),
    path('verify_accept/<int:id>/',views.verify_accept),
    path('verify_reject/<int:id>/',views.verify_reject),

    path('company/',views.company_tabel),
    path('car/',views.car_tabel),
    path('booking/',views.booking_ta),
    path('order_details/<int:bid>/',views.order_details),

    path('login/',views.ad_login),
    path('logout/',views.logout),
    path('forgot/',views.forgg),
    path('sendmail/',views.send_OTP),
    path('reset_pass/',views.set_pass),

    path('user_profile/',views.user_profile),
    path('edit_profile/',views.edit_profile),

    path('location/',views.loc_tabel),
    path('co_ins/',views.company_insert),
    path('car_i/',views.car_insert),
    path('location_i/',views.location_insert),
    path('det_c/<int:id>',views.det_company),
    path('det_l/<int:id>',views.det_location),
    path('det_car/<int:id>',views.det_car),
    path('edit_company/<int:id>',views.edit_company),
    path('update_company/<int:id>',views.update_company),
    path('edit_location/<int:id>',views.edit_location),
    path('update_location/<int:id>',views.update_location),
    path('edit_car/<int:id>',views.edit_car),
    path('update_car/<int:id>',views.update_car),
    
]
