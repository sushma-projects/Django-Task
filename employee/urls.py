
from django.urls import path
from . import views
#from crudapp import views

urlpatterns = [
    
    path('',views.show,name='show'),
    
]
