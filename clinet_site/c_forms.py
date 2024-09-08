from django import forms
from admin_site.models import users


class RegisterForms(forms.ModelForm):
    dl_image = forms.FileField()
    class Meta:
        model = users
        fields = ['dl_number','dl_image','first_name','last_name','users_email','users_password','users_addres','users_phone']

class P_userForms(forms.ModelForm):
    class Meta:
        model = users
        fields = ['first_name','last_name','users_addres']
