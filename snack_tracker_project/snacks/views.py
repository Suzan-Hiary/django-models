from django.db import models
from django.shortcuts import render

# Create your views here.
from django.views.generic import  ListView ,DetailView
from .models import Snack


class HomePageView(ListView):
    template_name = 'home.html'
    model=Snack


class BlogDetailsView(DetailView):
    template_name = 'post_detail.html'
    model = Snack