from django.shortcuts import render

# Create your views here.

# Step 6.0  Define the HOME VIEW function
# and render a non-existing template:
def home(request):
    # Step 6.1 include a .html file extension to HOME
    # to return to home page
    return render(request, 'home.html')