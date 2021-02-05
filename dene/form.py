from django import forms
from dene.models import Form
from django.core.exceptions import ValidationError


class FormDene(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('isim','email','meslek','mesaj')
    
    def __init__(self,*args,**kwargs):
        super(FormDene, self).__init__(*args,**kwargs)
        for field  in self.fields:
            self.fields[field].required=True
       
    def clean(self):
        isim = self.cleaned_data.get("isim")
        if len(isim) <= 5:
              self.add_error('isim','isim soyisim 5 karakterden küçük olamaz') 
            

    def clean_email(self):
        email = self.cleaned_data.get('email',None)
        if ".com" not in email:
            self.add_error("email","hatalı bir mail adresi girdiniz")
        return email
