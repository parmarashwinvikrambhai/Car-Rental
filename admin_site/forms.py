from django import forms
from admin_site.models import car,company,location,users




class CompanyForms(forms.ModelForm):
    class Meta:
        model = company
        fields = ['company_name']

class CarForms(forms.ModelForm):
    img_car = forms.FileField()
    class Meta:
        model = car
        fields = ['car_id','reg_number','model_name','img_car','model_year','available_flag','mileage','fuels_type','no_seats','cost','car_type','transmission','refund_amt','pick_drop_charge','company_id']


class LocationForms(forms.ModelForm):
    class Meta:
        model = location
        fields = ['location_id','street','area','city']


class UsForms(forms.ModelForm):
    class Meta:
        model = users
        fields = ['first_name','last_name','users_addres']

        