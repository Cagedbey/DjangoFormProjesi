from django.urls import path
from dene.views import ilk

urlpatterns = [
    path('',ilk,name="dene")

]