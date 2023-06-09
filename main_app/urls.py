# Step 5.2 ADD the ROUTING Boilerplate to main_app/urls
# to get your server back

from django.urls import path
from . import views

urlpatterns = [
# Step 5.3 add PATH to URLPATTERNS
path('', views.home, name='home'),
# Step 8.1 add PATH to ABOUT
path('about/', views.about, name='about')
]

# Step 8.2 touch main_app/templates/base.html
# to CREATE your BASE html to ensure
# your TEMPLATE INHERITANCE WORKS