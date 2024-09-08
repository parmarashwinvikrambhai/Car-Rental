import email
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

 
#1
class users(models.Model):
    users_id = models.AutoField(primary_key=True)
    dl_number=models.CharField(null=False,max_length=15)
    dl_image=models.CharField(null=False,max_length=200)
    first_name= models.CharField(null=False,max_length=20)
    last_name=models.CharField(null=False,max_length=20)
    users_email=models.EmailField(null=False,max_length=100)
    users_password=models.CharField(null=False,max_length=100)
    users_addres=models.CharField(null=False,max_length=250)
    users_phone=models.BigIntegerField(null=False)
    is_verify=models.IntegerField(default=0)
    is_admin=models.IntegerField(default=0)
    otp = models.CharField(max_length=10,null=True,default=0)
    otp_used = models.IntegerField(default=0)

    class Meta:
        db_table="users"

#2
class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    company_name=models.CharField(null=False,max_length=20)

    class Meta:
        db_table="company"

#3
class car(models.Model):
    car_id=models.AutoField(primary_key=True)
    reg_number=models.CharField(null=False,max_length=11)
    model_name=models.CharField(null=False,max_length=20)
    img_car=models.CharField(null=False,max_length=200)
    model_year=models.CharField(max_length=20,null=False)
    available_flag=models.IntegerField()
    mileage=models.CharField(null=False,max_length=25)
    fuels_type=models.CharField(null=False,max_length=20)
    no_seats=models.IntegerField()
    cost=models.FloatField(null=False)
    car_type=models.CharField(max_length=20)
    transmission=models.CharField(max_length=20)
    company_id=models.ForeignKey(company, on_delete=models.PROTECT)
    refund_amt=models.IntegerField()
    pick_drop_charge=models.IntegerField()
    class Meta:
        db_table="car"

#4  
class location(models.Model):
    location_id=models.AutoField(primary_key=True)
    street=models.CharField(null=False,max_length=50)
    area=models.CharField(null=False,max_length=50)
    city=models.CharField(null=False,max_length=50)

    class Meta:
        db_table="location"

#5
class booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    from_date=models.DateTimeField()
    return_date=models.DateTimeField()
    pickup_location=models.ForeignKey(location, on_delete=models.PROTECT,related_name='pickup_location')
    drop_location=models.ForeignKey(location, on_delete=models.PROTECT,related_name='drop_location')
    payment_status=models.IntegerField()
    amount=models.FloatField()
    users_id=models.ForeignKey(users, on_delete=models.PROTECT)
    car_id=models.ForeignKey(car, on_delete=models.PROTECT)

    class Meta:
        db_table="booking"

class payments(models.Model):
    payment_id=models.AutoField(primary_key=True)
    transfer_id=models.CharField(null=False,max_length=30)
    booking_id=models.ForeignKey(booking,on_delete=models.PROTECT)
    users_id=models.ForeignKey(users,on_delete=models.PROTECT)
    class Meta:
        db_table="payments"

class cancel_payment(models.Model):
    cancel_payment_id=models.AutoField(primary_key=True)
    pay_number=models.BigIntegerField(null=False)
    cancel_disc=models.CharField(null=False,max_length=500)
    booking_id=models.ForeignKey(booking, on_delete=models.PROTECT)
    payment_id=models.ForeignKey(payments, on_delete=models.PROTECT)
    users_id=models.ForeignKey(users, on_delete=models.PROTECT)
    type_payment=models.CharField(null=False,max_length=20)
    cancel_amount=models.FloatField()
    class Meta:
        db_table="cancel payment"


# class feedbacks(models.Model):
#     feedbacks_id = models.AutoField(primary_key=True)
#     suggestion_date = models.DateField(null=False)
#     users_id = models.ForeignKey(users, on_delete=models.PROTECT)
#     suggestion = models.CharField(null=False, max_length=200)
#     #rate = models.IntegerField(5)
#     # car_id = models.ForeignKey(car, on_delete=models.PROTECT)
#     class Meta:
#         db_table = "feedbacks"


# class favourit(models.Model):
#     favourit_id=models.AutoField(primary_key=True)
#     users_id=models.ForeignKey(users, on_delete=models.PROTECT)
#     car_id = models.ForeignKey(car, on_delete=models.PROTECT)
#     added_date=models.DateField()
#     class Meta:
#         db_table = "favourit"
