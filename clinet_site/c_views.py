from datetime import datetime,timezone
import random
import string
import os
from urllib import response

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from admin_site.models import booking, cancel_payment, car, company, location, payments, users
from car_rental.settings import BASE_DIR
from clinet_site.c_forms import P_userForms, RegisterForms
from admin_site.functions import handle_uploaded_file

# Create your views here.
def home(request):
    cars=car.objects.all().filter(available_flag=1).order_by('?')[:9]
    cars_count = car.objects.all().count()
    return render(request,"index2.html",{"cars":cars})



def car_list(request):
    carslist=car.objects.filter(available_flag=1)
    distinct_transmission = car.objects.all().values('transmission').distinct()
    distinct_fuels_type = car.objects.all().values('fuels_type').distinct()
    distinct_car_type = car.objects.all().values('car_type').distinct()
    distinct_no_seats = car.objects.all().values('no_seats').distinct()
    paginator=Paginator(carslist,10)
    page_next=request.GET.get('page')
    page_obj=paginator.get_page(page_next)
    print("_"*10)
    pass_data={"carslist":page_obj,
    "distinct_no_seats":distinct_no_seats,
    "distinct_car_type":distinct_car_type,
    "distinct_fuels_type":distinct_fuels_type,
    "distinct_transmission":distinct_transmission}
    return render(request,"cars_list.html",pass_data)

def payment(request,booking_id):
    if request.session.has_key('client_id'):
        book=booking.objects.get(booking_id=booking_id)
        book.payment_status=1
        book.save()
        c_id=book.car_id
        print("=============== ",c_id)
        car_booked=car.objects.get(car_id=c_id)
        car_booked.available_flag=1
        car_booked.save()

        return redirect("/client/booked_car/")
    else:
        return redirect("/client/home/")





def autosuggest(request):
    if 'term' in request.GET:
        qs=car.objects.filter(model_name__instartswith=request.GET.get('term'))
        name=list()
        for x in qs:
            name.append(x.model_name)
        return JsonResponse(name,safe=False)
    return render(request,"index2.html")

def car_list_search(request):
    
    distinct_transmission = car.objects.all().values('transmission').distinct()
    distinct_fuels_type = car.objects.all().values('fuels_type').distinct()
    distinct_car_type = car.objects.all().values('car_type').distinct()
    distinct_no_seats = car.objects.all().values('no_seats').distinct()
    if request.method=="POST":
        name = request.POST["search1"]
        carslist=car.objects.filter(model_name=name)
    else:
        carslist=car.objects.filter(available_flag=1)
    paginator=Paginator(carslist,10)
    page_next=request.GET.get('page')
    page_obj=paginator.get_page(page_next)
    print("_"*10)
    pass_data={"carslist":page_obj,
    "distinct_no_seats":distinct_no_seats,
    "distinct_car_type":distinct_car_type,
    "distinct_fuels_type":distinct_fuels_type,
    "distinct_transmission":distinct_transmission}
    return render(request,"cars_list.html",pass_data)



def car_list_comp(request,com_id):
    carslist=car.objects.filter(company_id=com_id)
    distinct_transmission = car.objects.all().values('transmission').distinct()
    distinct_fuels_type = car.objects.all().values('fuels_type').distinct()
    distinct_car_type = car.objects.all().values('car_type').distinct()
    distinct_no_seats = car.objects.all().values('no_seats').distinct()
    paginator=Paginator(carslist,10)
    page_next=request.GET.get('page')
    page_obj=paginator.get_page(page_next)
    print("_"*10)
    pass_data={"carslist":page_obj,
    "distinct_no_seats":distinct_no_seats,
    "distinct_car_type":distinct_car_type,
    "distinct_fuels_type":distinct_fuels_type,
    "distinct_transmission":distinct_transmission}
    return render(request,"cars_list.html",pass_data)

def filter1(request,str,str1):
    if str == "transmission":
        carslist=car.objects.filter(transmission=str1,available_flag=1)
    elif str == "car_type":
        carslist=car.objects.filter(car_type=str1,available_flag=1)
    elif str == "no_seats":
        carslist=car.objects.filter(no_seats=str1,available_flag=1)
    elif str == "fuels_type":
        carslist=car.objects.filter(fuels_type=str1,available_flag=1)
    
    distinct_transmission = car.objects.all().values('transmission').distinct()
    distinct_fuels_type = car.objects.all().values('fuels_type').distinct()
    distinct_car_type = car.objects.all().values('car_type').distinct()
    distinct_no_seats = car.objects.all().values('no_seats').distinct()
    
    paginator=Paginator(carslist,10)
    page_next=request.GET.get('page')
    page_obj=paginator.get_page(page_next)
    print("_"*10)
    
    pass_data={"carslist":page_obj,
        "distinct_no_seats":distinct_no_seats,
        "distinct_car_type":distinct_car_type,
        "distinct_fuels_type":distinct_fuels_type,
        "distinct_transmission":distinct_transmission}
    
    return render(request,"cars_list.html",pass_data)
    

def load_menu(request):
    comp=company.objects.all()
    # sue=sub_categorys.objects.all()
    return render(request,"c_menu.html",{"comp":comp})

def car_details(request,cars_id):

    if request.method=="POST":
        
        p_datetime=request.POST["p_datetime"]
        d_datetime=request.POST["d_datetime"]
        p_location=request.POST["p_location"]
        d_location=request.POST["d_location"]

        print("3"*2,p_datetime,"--3"*2,p_location,"3"*2,d_datetime,"--3"*2,d_location)
        cars1=car.objects.get(car_id=cars_id)
        d1=datetime.strptime(p_datetime,"%Y-%m-%dT%H:%M")
        d2=datetime.strptime(d_datetime,"%Y-%m-%dT%H:%M")
        delta = d2 - d1
        tsecs = delta.total_seconds()
        thours=tsecs/(60*60)
        price_hours=cars1.cost/24
        prince_uers_req=int(thours*price_hours)
        # int_day=int(delta.days)*12
        print(f'Difference is {prince_uers_req} price ')
        print(f'Difference is {thours} hours ')
        print(f'Difference is {delta} days ')
        total=int(prince_uers_req+200+2400)
        comp_id=cars1.company_id.company_id
        carslist=car.objects.filter(company_id=comp_id).order_by('?')[:6]
        cost_car=car.cost
        locations=location.objects.all()
        today_date=datetime.now()
        x = str(today_date).split(" ")
        print("-------",x)
        y=x[1].split(".")
        print("yyyyyy",y)
        tod=x[0]+"T"+y[0]
        print(";;;;;;;",tod)
        
        if request.session.has_key('client_id'):
            Userid=request.session['client_id']
            uDetails=users.objects.get(users_id=Userid)
            if uDetails.is_verify == 0:
                verify=0
            elif uDetails.is_verify == 1:
                verify=1
            elif uDetails.is_verify == 2:
                verify=2
        else:
            verify=0

        tag_cal="true"
        datapass={"prince_uers_req":str("Rs."+str(prince_uers_req)),
                    "pick_date":d1,
                    "drop_date":d2,
                    "cost_cars":str("Rs."+str(cost_car)),
                    "no_days":delta,
                    "Delivery": str("Rs."+str(200)),
                    "deposit":str("Rs."+str(2400)),
                    "total":str("Rs."+str(total)),
                    "cars":cars1,
                    "locations":locations,
                    "carslist":carslist,
                    #pass date
                    "pass_p_location":p_location,
                    "pass_d_location":d_location,
                    "pass_total":int(total),
                    "pass_p_datetime":str(p_datetime),
                    "pass_d_datetime":str(d_datetime),
                    "today_date":tod,
                    "tag_cal":tag_cal,
                    "verify":verify,
                }
        return render(request,"car_details.html",datapass)
    else:
            locations=location.objects.all()
            cars1=car.objects.get(car_id=cars_id)
            comp_id=cars1.company_id.company_id
            carslist=car.objects.filter(company_id=comp_id).order_by('?')[:6]
            verify=0
            datapass={"cars":cars1,"locations":locations,"verify":verify,"carslist":carslist}
            return render(request,"car_details.html",datapass)
    

def booked_car(request):
    if 'client_id' in request.session:
        uid = request.session['client_id']
        booking_record=booking.objects.filter(users_id=uid).order_by("-booking_id")
        return render(request,"c_booked.html",{"booking":booking_record})
    else:
        return redirect("/client/user_signin/")

def booking_detail(request,booked_id):
    bookingDetails =booking.objects.get(booking_id=booked_id)
    TodayDate=datetime.now(timezone.utc)
    print("----- booking date ----",bookingDetails.from_date,"--- booking todays ---",TodayDate)
    
    # cancle durations time in hours 
    diff=bookingDetails.from_date-TodayDate
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    
    # trip Duration time
    tripDiff=bookingDetails.return_date-bookingDetails.from_date
    print("-- trip Diff ->->", tripDiff)

    tripDiffString = str(tripDiff)
    day = tripDiffString[:5]
    hour = tripDiffString[7:9]
    minutes = tripDiffString[10:12]
    seconds = tripDiffString[13:15]

    print("day: ", tripDiffString[:5]) 
    print("hours: ", tripDiffString[7:9])
    print("minutes: ", tripDiffString[10:12])
    print("seconds: ", tripDiffString[13:15])
    print("diff of hours",hours)
    carDetails =car.objects.get(car_id=bookingDetails.car_id_id)
    
    return render(request,"booking_detail.html",
    {"carDetails":carDetails,"bookingDetails":bookingDetails,
    # cancle durations
    "hours":hours,
    #trip Durations
    "day": day, "hour": hour, "min": minutes})


def payment(request,booking_id):
    if request.session.has_key('client_id'):
        book=booking.objects.get(booking_id=booking_id)
        bookingID=booking_id
        # book.payment_status=1
        # book.save()
        Amount=book.amount

        # print("-----------------",c_id)
        # car_booked=car.objects.get(car_id=c_id)
        # car_booked.available_flag=0
        # car_booked.save()
        return render(request, "payment.html", {"bookingID":bookingID,"Amount":Amount})
        # return redirect("/client/booked_car/")
    else:
        return redirect("/client/user_signin/")

def paymentMOdule(request,booking_id):
    if request.session.has_key('client_id'):
        if request.method=="POST":
            transfer = ''.join(random.choices(string.ascii_lowercase+string.digits, k=20))
            bkid=booking_id
            uid = request.session['client_id']
            print("booking_id ---> ",booking_id)
            print("paymet ID --->  ",transfer)
            pay=payments(transfer_id=transfer,booking_id_id=bkid,users_id_id=uid)
            pay.save()
            book=booking.objects.get(booking_id=booking_id)
            book.payment_status=1
            book.save()
            c_id=book.car_id.car_id
            print("-----------------",c_id)
            car_booked=car.objects.get(car_id=c_id)
            car_booked.available_flag=0
            car_booked.save()
            e=request.session['client_email']
            book_email(booking_id,uid,c_id)
            book=booking.objects.get(booking_id=booking_id)
            subject='HireCar your is booked  check the website '
            bMess="booking id=> ",book.booking_id,"car models",book.car_id.model_name,"Car Register no.",book.car_id.reg_number,"\n"
            # message= " YOu book car \n Car details \n ",bMess,"\n with payment id \n ",transfer,"\n"
            message="your car booked."
            email_from = settings.EMAIL_HOST_USER
            print('>',e)
            recipient_list=["tauqirqureshi7797@gmail.com", ]
            send_mail(subject , message , email_from , recipient_list)
            
        return redirect("/client/booked_car/")
        # return redirect("/client/booked_car/")
    else:
        return redirect("/client/user_signin/")


def book_email(bid,userid,cid):
    bookE=booking.objects.get(booking_id=bid)
    userE=users.objects.get(users_id=userid)
    carE=car.objects.get(car_id=cid)
    toEmail = userE.users_email

    merge_data={
        "username":userE.first_name,
        "carid":carE.car_id,
        "carname":carE.model_name,
        "carreg":carE.reg_number,
        "pickuplocation":bookE.pickup_location.street+bookE.pickup_location.area+bookE.pickup_location.city,
        "droplocation":bookE.drop_location.street+bookE.drop_location.area+bookE.drop_location.city,
        "totalprice":bookE.amount,
        "bookingid":bookE.booking_id,

    }

    print("to email ",toEmail)
    print("Merge data",merge_data)

    # username
    # car id
    # carname
    # pickup location
    # drop location
    # total price
    # car image
    # booking id

    subject = "Your Booking Details"
    html_body = render_to_string("email_template.html", merge_data)

    email = EmailMultiAlternatives(
        subject = subject,
        from_email= settings.EMAIL_HOST_USER,
        to=[toEmail],
    )
    os.path.join(BASE_DIR, '/client_site/static/')

    img_path=str(BASE_DIR)+"/admin_site/static/image/"+carE.img_car
    # +carE.img_car
    
    print(str(BASE_DIR)+"/admin_site/static/image/"+carE.img_car)
    print("ImageUrl: ",BASE_DIR,"------>", img_path)
    email.attach_alternative(html_body, "text/html")
    email.attach_file(img_path)
    email.send()










@csrf_exempt
def booking_car(request):
 
    if request.method == "POST":
            uid = request.session['client_id']
            print("Request POST Data: ")
            print(request.POST)
            p_location=request.POST["pickup_location"]
            d_location=request.POST["drop_location"]
            total=request.POST["total"]
            carid=request.POST["car_id"]
            p_date=request.POST["pickup_date"]
            p_date=(p_date)
            
            # p_date=datetime.strptime(p_date,parser(p_date))
            d_date=request.POST["drop_date"]
            # d_date=str(d_date)
            # d_date=datetime.strptime(d_date,"%Y-%m-%d %H:%M:%S")
            # d_date=datetime.strptime(d_date,"%Y-%m-%dT%H:%M")
            print(" ))))))))--  ",d_date)
            print(" ))))))))--  ",p_date)
            o=booking(from_date=p_date,return_date=d_date,pickup_location_id=p_location,drop_location_id=d_location,payment_status=0,amount=total,users_id_id=uid, car_id_id=carid)
            o.save() 
            return redirect("/client/booked_car/")
    else:
            return redirect("/client/booked_car/")
    

def cancelBooking(request,id):
    if 'client_id' in request.session:
        user_id = request.session['client_id']
        uuser=users.objects.get(users_id=user_id)
        bookings=booking.objects.get(booking_id=id)
        pay_id=payments.objects.get(booking_id=id)
        amt=bookings.amount
        if request.method == "POST":
            phone=request.POST["phone"]
            t_payment=request.POST["type_payment"]
            disc=request.POST["disc"]
            print("booking ->",bookings.booking_id)
            paymentCancel=cancel_payment(pay_number=phone,cancel_disc=disc,booking_id_id=bookings.booking_id,payment_id_id=pay_id.payment_id, users_id_id=user_id,type_payment=t_payment,cancel_amount=amt)
            paymentCancel.save()
            bookings.payment_status=2
            bookings.save()
            return redirect("/client/booked_car/")
        else:
            bookid=bookings.booking_id
            phone=uuser.users_phone
            return render(request,"cancellation_form.html", {"bookid":bookid,"amt":amt,"phone":phone})
    # else:
        # return redirect("/client/login/")

def user_aboutus(request):
    return render(request,"c_aboutus.html")



def clinet_login(request):
    if request.method == "POST":
        e = request.POST["c_email"]
        p = request.POST["c_password"]
        print(" ????????????? ",e,p)
        

        val = users.objects.filter(users_email=e, users_password=p ).count()
        print(" --------------- ",val)
        if val==1:
            data=users.objects.get(users_email=e,users_password=p)
            
            request.session['client_id']=data.users_id
            request.session['client_email']=data.users_email
            
            return redirect('/client/home/')
        else:    
            #    context=make_context("Invaild password and email")
            #    messages.error(request,"Invaild password and email")
            messages.error(request,"Invaild password and email")
            return render(request,"c_signin.html")
    else:
        return render(request,"c_signin.html")

def user_forgot(request):
    return render(request,"c_forgot.html")


def send_otp(request): 
    if request.method == "POST":
        otp1=random.randint(10000,99999)
        print(otp1)
        e=request.POST['email']
        print("----email-----",e)
        request.session['c_email']=e
        print(request.session['c_email'])
        obj = users.objects.filter(users_email=e).count()

        if obj == 1:
          val = users.objects.filter(users_email=e).update(otp=otp1, otp_used=0)
          subject='OTP VERIFICATION FOR HIRECAR'
          message= str(otp1)
          email_from = settings.EMAIL_HOST_USER
          recipient_list=[e,]
          send_mail(subject,message,email_from,recipient_list)
          return render(request,'c_set_password.html')
        else:
           messages.error(request,"This email not exit") 
    return render(request,'c_forgot.html')


def set_password(request):
    totp = request.POST['otp']
    npassword = request.POST['n_password']
    cpassword = request.POST['c_password']

    if npassword == cpassword:

        e = request.session['c_email']
        print(e)
        val = users.objects.filter(users_email=e,otp=totp,otp_used=0).count()
        
        if val == 1:
            ps=npassword
            # ps=hashlib.md5(npassword.encode('utf')).hexdigest()
            val = users.objects.filter(users_email=e).update(otp_used=1,users_password=ps)
            del request.session['c_email']
            return redirect("/client/user_signin/")
        else:
            messages.error(request,"OTP does not match ")
            return render(request,"c_set_password.html")
    else:
        messages.error(request,"NEW PASSWORD & CONFIRM PASSWORD DEOS NOT MATCH ")
        return render(request,"c_set_password.html")

def user_register(request):
    if request.method == "POST":
        form=RegisterForms(request.POST,request.FILES)
        print("AJAX RESPONSE : ", request.POST)
        
        print("*****************REGISTRATION FORMS ERRORS*************",form.errors)
        if form.is_valid():
            handle_uploaded_file(request.FILES['dl_image'])
            newform = form.save(commit=False)

            # newform.users_password = hashlib.md5(newform.users_password.encode('utf')).hexdigest()
            e=form.cleaned_data['dl_number']
            email=form.cleaned_data['users_email']
            print(e)
            obj = users.objects.filter(users_email=email).count()
            obj1 = users.objects.filter(dl_number=e).count()
            if obj==1:
                messages.error(request,"This email already exists")
            elif obj1==1:
                messages.error(request,"This driving licence number already exists")   
            else:
                newform.save()
                return redirect("/client/user_signin/")

            # print("#"*2,dl)
            # froms.save(commit=True)
            
        else:
            pass
    else:
       form=RegisterForms()
       
    return render(request,"c_signup.html",{"froms":form})


def user_profile(request):
    if 'client_id' in request.session:
        uid = request.session['client_id']
        u_details=users.objects.get(users_id=uid)
        return render(request,"c_Profile.html",{"u_details":u_details})
    else:
        return redirect("/client/user_signin/")

def user_update(request):
    id=request.session['client_id']
    u_details=users.objects.get(users_id=id)
    froms=P_userForms(request.POST,instance=u_details)
    print("===update_profile-from== errors====",froms.errors)
    if froms.is_valid():
        try:
            froms.save()
            return redirect("/client/user_profile/")
        except:
            print("======update_profile-from== systm====",sys.exc_info())
    return render(request,"c_Profile.html",{"u_details":u_details})


def user_logout(request):
    try:
        del request.session['client_id']
        del request.session['client_email']
        return redirect("/client/home/")
    except:
        pass
    return redirect("/client/home/")


