from django.contrib import admin

# Import your models here
from .models import Guitar, Using

# Register your models here.
admin.site.register(Guitar)
admin.site.register(Using)