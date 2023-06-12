# Step 5.2 ADD the ROUTING Boilerplate to main_app/urls
# to get your server back

from django.urls import path
from . import views

urlpatterns = [
# Step 5.3 add PATH to URLPATTERNS
path('', views.home, name='home'),
# Step 8.1 add PATH to ABOUT
path('about/', views.about, name='about'),
# Step 10.1 add PATH for ALL
path('guitars/', views.guitars_index, name='index'),
# (Models) Part 2 - Step 10.2
# DEFINE ROUTE for DETAILS PAGE (Show functionality)
path('guitars/<int:guitar_id>/', views.guitars_detail, name='detail')
]

# Step 8.2 touch main_app/templates/base.html
# to CREATE your BASE html to ensure
# your TEMPLATE INHERITANCE WORKS

 