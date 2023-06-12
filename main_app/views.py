from django.shortcuts import render
# (Models) Step 8.0 IMPORT the CAT MODEL
from .models import Guitar

# Create your views here.

# Step 6.0  Define the HOME VIEW function
# and render a non-existing template:
def home(request):
    # Step 6.1 include a .html file extension to HOME
    # to return to home page
    return render(request, 'home.html')

# Step 7.0 mkdir main_app/templates 
# to CREATE a TEMPLATES DIRECTORY for all template files 
# (will always be html in Django)

# Step 7.1 create a home.html file in the GUI and go there

# Step 8.1 define ABOUT function
def about(request):
    return render(request, 'about.html')

# Step 10.2 define the ALL function
def guitars_index(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    return render(request, 'guitars/index.html', {
        'guitar': guitar
    })

# DEFINE the DETAILS Function
def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    return render(request, 'guitars/detail.html', {
        'guitar': guitar
    })