from django.urls import path
from home import views


urlpatterns = [

    # The home page
path('', views.index, name='index'),    

]