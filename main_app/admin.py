from django.contrib import admin

# Import your models here
from .models import Guitar, Using

# Register your models here.
admin.site.register(Guitar)
# Lab pt 4 register USING Class
admin.site.register(Using)