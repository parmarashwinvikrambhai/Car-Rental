import os
import sys
from car_rental.settings import BASE_DIR

from django.conf import settings
from django.contrib import messages
import random

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from admin_site.forms import *
from admin_site.functions import handle_uploaded_file
from admin_site.models import *
from django.views.decorators.cache import cache_control
# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def home(request):
    no_user=users.objects.all().count()
    no_car=car.objects.all().count()
    no_booking=booking.objects.all().count()
    no_company=company.objects.all().count()
    user=users.objects.all()
    if header(request):
       return render(request,"admin_index.html",{"user":user,"no_company":no_company,"no_user":no_user,"no_car":no_car,"no_booking":no_booking})
    else:
        return redirect("/login/")

def header(request):
    if request.session.has_key('admin_id'):
        return True
    else:
        return False

def user_tabel(request):
    user=users.objects.all()
    if header(request):
        return render(request,"user_table.html",{"user":user})
    else:
        return redirect("/login/")

def car_in(request):
    return render(request,"car_ins.html")
    

def forgg(request):
    return render(request,"forgot_password.html")
        


def company_tabel(request):
    cs=company.objects.all()
    if header(request):
        return render(request,"company.html",{"company":cs})
    else:
        return redirect("/login/")


def car_tabel(request):
    ca=car.objects.all()
    if header(request):
        return render(request,"car.html",{"car":ca})
    else:
        return redirect("/login/")


def new_car_email(toemail):
    car_D=car.objects.last()
    car_data={
        "carmodel":car_D.model_name,
        "modelyear":car_D.model_year,
        "mileage":car_D.mileage,
        "fuelstype":car_D.fuels_type,
        "noseats":car_D.no_seats,
        "cost":car_D.cost,
        "transmission":car_D.transmission,
    }

    
    subject = "Your Booking Details"
    html_body = render_to_string("caremail_template.html",car_data)

    email = EmailMultiAlternatives(
        subject = subject,
        from_email= settings.EMAIL_HOST_USER,
        to=[toemail],
    )
    os.path.join(BASE_DIR, '/client_site/static/')

    img_path=str(BASE_DIR)+"/admin_site/static/image/"+car_D.img_car
    # +carE.img_car
    
    print(str(BASE_DIR)+"/admin_site/static/image/"+car_D.img_car)
    print("ImageUrl: ",BASE_DIR,"------>", img_path)
    email.attach_alternative(html_body, "text/html")
    email.attach_file(img_path)
    email.send()



def booking_ta(request):
    # ba= booking.objects.all().order_by("-booking_id")
    ba=booking.objects.all().order_by("-booking_id")
    if header(request):
        return render(request,"booking.html",{"booking":ba})
    else:
        return redirect("/login/")

def loc_tabel(request):
    la=location.objects.all()
    if header(request):
        return render(request,"location.html",{"location":la})
    else:
        return redirect("/login/")




def order_details(request,bid):
    order_detail=booking.objects.get(booking_id=bid)
    cid=order_detail.car_id.car_id
    uid=order_detail.users_id.users_id
    print("0000000>",uid) 
    
    cal_details=None
    if(order_detail.payment_status)==2:
        cal_details=cancel_payment.objects.get(booking_id=bid)
    
    
    pay_tranfer_id=""
    if(order_detail.payment_status) >=1:
        pay_details=payments.objects.get(booking_id=bid) 
        pay_tranfer_id =pay_details.transfer_id 

    car_detial=car.objects.get(car_id=cid)
    user_detial=users.objects.get (users_id=uid)
    print(user_detial)

    return render(request,"order_details.html",
    {"order_detail":order_detail,
     "cal_details":cal_details,
     "pay_details":pay_tranfer_id,
     "car_detail":car_detial,
     "use_details":user_detial,
    })

def loc_lns(request):
    return render(request,"location_ins.html")



def company_insert(request):
    if request.method=="POST":
        form = CompanyForms(request.POST)
        print("-----------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/company")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form =CompanyForms()

    return render(request,"company_ins.html",{"form":form})

def car_insert(request):
    # c=company.objects.all()
    # print("+++++++++++++++",c)
    if request.method == "POST":
        form = CarForms(request.POST,request.FILES)
        print("-----------", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['img_car'])
                form.save()
                # sending the email form new car added.
                userEmail=users.objects.all()
                for ue in userEmail:

                    print("------>",ue.users_email)
                    
                    sendemail=ue.users_email
                    new_car_email(sendemail)

                return redirect("/car")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form = CarForms()
    c=company.objects.all()
    print(c)
    return render(request,"car_ins.html",{"form":form,"ca":c})


def location_insert(request):
    if request.method=="POST":
        form = LocationForms(request.POST)
        print("-----------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/location")
            except:
                print("-----------",sys.exc_info())
        else:
            pass
    else:
        form =LocationForms()

    return render(request,"location_ins.html",{"form":form})


def det_company(request,id):
   c= company.objects.get(company_id=id)
   try:
       c.delete()
       return redirect("/company")
   except:
       return redirect("/company-table")


def det_location(request,id):
   la= location.objects.get(location_id=id)
   try:
       la.delete()
       return redirect("/location")
   except:
       return redirect("/location-table")


def det_car(request,id):
   ca= car.objects.get(car_id=id)
   try:
       ca.delete()
       return redirect("/car")
   except:
       return redirect("/car-table")



def edit_company(request,id):
    pc = company.objects.get(company_id=id)
    return render(request,"edit_company.html",{"pc":pc})


def update_company(request,id):
    pc = company.objects.get(company_id=id)
    form = CompanyForms(request.POST,instance=pc)
    print("-----", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect('/company')
        except:
            print("-----", sys.exc_info())
    return render(request, "edit_company.html", {"pc": pc})



def edit_location(request,id):
    lc = location.objects.get(location_id=id)
    return render(request,"edit_location.html",{"lc":lc})


def update_location(request,id):
    lc = location.objects.get(location_id=id)
    form = LocationForms(request.POST,instance=lc)
    print("-----", form.errors)
    if form.is_valid():
        try:
            
            form.save()
            return redirect('/location')
        except:
            print("-----", sys.exc_info())
    return render(request, "edit_location.html", {"lc": lc})



def edit_car(request,id):
    p = company.objects.all()
    pd = car.objects.get(car_id=id)
    print("---------------------",pd.img_car)

    return render(request,"edit_car.html",{"pd":pd,"p":p})

def update_car(request,id):
    p = company.objects.all()
    pd = car.objects.get(car_id=id)
    print("---------------------",pd)
    form = CarForms(request.POST,request.FILES,instance=pd)
    print("-----", form.errors)
    if form.is_valid():
        try:
            handle_uploaded_file(request.FILES['img_car'])
            form.save()
            return redirect('/car')
        except:
            print("-----", sys.exc_info())
    return render(request, "edit_car.html", {"pd": pd,"p":p})


def verify_accept(request,id):
    vAusers=users.objects.get(users_id=id)
    vAusers.is_verify=1
    vAusers.save()
    return redirect("/user_tabel/")

def verify_reject(request,id):
    vRusers=users.objects.get(users_id=id)
    vRusers.is_verify=2
    vRusers.save()
    return redirect("/user_tabel/")


def ad_login(request):
    if request.method == "POST":
        e=request.POST["email"]
        p=request.POST["password"]

        val=users.objects.filter(users_email=e ,users_password=p , is_admin=1).count()

        if val == 1:

            data = users.objects.filter(users_email = e,users_password= p,is_admin = 1)

            for item in data:
                request.session['admin_id']=item.users_id
                request.session['admin_name'] = item.first_name
                request.session['admin_email'] = item.users_email

            return redirect("/admin_index/")
        else:
            messages.error(request, "Invalid username and password")
            return render(request,"login.html")
    else:
        return render(request, "login.html")


def logout(request):
    try:
        del request.session['admin_id']
        del request.session['admin_name']
        del request.session['admin_email']
    except:
        pass

    return redirect("/login/")


def send_OTP(request):
    otp1 = random.randint(10000, 99999)

    e = request.POST['email']
    print("---------------",e)
    request.session['users_email']=e
    obj = users.objects.filter(users_email=e,is_admin=1).count()

    if obj == 1:
        val = users.objects.filter(users_email=e).update(otp=otp1 , otp_used=0)
        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'reset_pass.html')

    else:
        messages.error(request,'Invalid username and password')
        return render(request,"login.html")




def set_pass(request):
    totp = request.POST['otp']
    tpassword = request.POST['npass']
    cpassword = request.POST['cpass']

    if tpassword == cpassword:
        e = request.session['users_email']
        val = users.objects.filter(users_email=e, otp=totp, otp_used=0, is_admin=1).count()

        if val == 1:
            val = users.objects.filter(users_email=e, is_admin=1).update(otp_used=1, users_password=tpassword)
            return redirect('/login/')
        else:
            messages.error(request, 'OTP does not match')
            return render(request, "reset_pass.html")
    else:
        messages.error(request, 'New Password & Confirm Password does not match')
        return render(request, "reset_pass.html")

    return render(request, "reset_pass.html")


def user_profile(request):
    if header(request):
        id = request.session["admin_id"]
        u = users.objects.get(users_id=id)
        return render(request, "user_profile.html",{"item":u})
    else:
        return redirect("/login/")

def edit_profile(request):
    id = request.session["admin_id"]
    u = users.objects.get(users_id=id)
    form = UsForms(request.POST, instance=u)
    print("----------", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/user_profile")
        except:
            print("++++++", sys.exc_info())

    return render(request, "edit_profile.html", {"form": form, "item": u})


def client_view(request):
    return redirect("/client/home/")
