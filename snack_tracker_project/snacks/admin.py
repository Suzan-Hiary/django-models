from django.contrib import admin

# Register your models here.
from .models import Snack 

#added model to admin
admin.site.register(Snack)