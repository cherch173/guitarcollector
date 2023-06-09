from django.shortcuts import render

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