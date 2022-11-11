from django.shortcuts import render

# Create your views here.
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import get_object_or_404
from .models import MainProducts,FeaturedProducts



def index(request):
    data = MainProducts.objects.all()
    context = {
        'data' : data
    }
    return render(request,"homepage/index.html", context)