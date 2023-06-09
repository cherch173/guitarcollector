# Step 5.2 ADD the ROUTING Boilerplate to main_app/urls
# to get your server back

from django.urls import path
from . import views

urlpatterns = [
# Step 5.3 add PATH to URLPATTERNS
path('', views.home, name='home'),
]