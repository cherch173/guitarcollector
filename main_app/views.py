from django.shortcuts import render, redirect
# LAB pt 3 (CBVs) Step 1.4.1 IMPORT CreateView
# Step 2.3 IMPORT UpdateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# LAB pt 2 (Models) Step 8.0 IMPORT the CAT MODEL
from .models import Guitar
from .forms import UsingForm

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
def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {
        'guitars': guitars
    })

# DEFINE the DETAILS Function
def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    using_form = UsingForm()
    return render(request, 'guitars/detail.html', {
        'guitar': guitar,
        'using_form': using_form
    })

def add_use(request, guitar_id):
    form = UsingForm(request.POST)
    if form.is_valid():
        new_use = form.save(commit=False)
        new_use.guitar_id = guitar_id
        new_use.save()
    return redirect('detail', guitar_id=guitar_id)

# LAB pt 3 (CBVs) - Part 1.4.2 CREATE the CLASS for CREATE(New)
class GuitarCreate(CreateView):
    model = Guitar
    fields = '__all__'
    success_url = '/guitars'

# Part 2.4 - CREATE the CLASSES for UPDATE & DELETE

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = '__all__'
    success_url = '/guitars'

class GuitarDelete(DeleteView):
    model = Guitar
    success_url = '/guitars'

    