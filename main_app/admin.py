from django.contrib import admin

# Import your models here
from .models import Guitar

# Register your models here.
admin.site.register(Guitar)