from django.db import models



class Form(models.Model):
    meslekSec =((None,'Lutfen Bir Meslek seciniz'),('Öğretmen','ögretmen'),('Muhendis','muhendis'),('Doktor','doktor'),('polis','polis'),('Diger','diger'))
    isim = models.CharField(verbose_name="isim", max_length=100,blank=False)
    email = models.EmailField(verbose_name="email",null=True,blank=False, max_length=100)
    meslek = models.CharField(choices=meslekSec, null=True,blank=False, max_length=100)
    mesaj = models.TextField(verbose_name="mesaj",null=True,blank=False,max_length=300)
    class Meta:
        verbose_name_plural="Gelen Formlar"
    def __str__(self):
        return self.isim
    




    