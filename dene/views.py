from django.shortcuts import render,reverse,HttpResponseRedirect,HttpResponse
from dene.form import FormDene
from django.contrib import messages
from dene.models import Form
import time


def ilk(request):
    if request.method == "POST":
       form = FormDene(data=request.POST or None)
       if form.is_valid():
           caged = form.save(commit=True)
           form.save()
           msg = "Formunuz başarılı bir şekilde gönderilmiştir"
           messages.success(request,msg)
           form.clean()
           #return HttpResponse("CAGEDDD")
           return HttpResponseRedirect(reverse('dene'))

    form = FormDene(data=request.POST or None)
    return render(request,"form.html",context={'form':form})
    