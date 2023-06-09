from django.shortcuts import render

#Step 10.3 ADD your guitars for your ALL, my guy

guitars = [
    {'name': 'Les Paul', 'brand': 'Gibson', 'description': 'The GOAT', 'Date Manufactured': '1952'},
    {'name': 'Telecaster', 'brand': 'Fender', 'description': 'snarling and classic. Prince''s go-to which says it all', 'Date Manufactured': '1951'},
    {'name': 'ES-355', 'brand': 'Gibson', 'description': 'the most iconic of all semi-hollowbody double cutaways. Versatile enough to fit the style of BB King, Leo Nocentelli and Paul Westerberg.', 'Date Manufactured': '1958'},
    {'name': 'SG', 'brand': 'Gibson', 'description': 'Lengedary, lightweight, lightning-faast double cutaway. Sings especially well with P-90 pickups.', 'Date Manufactured': '1961'},
    {'name': 'Stratocaster', 'brand': 'Fender', 'description': 'music''s most famous instrument. If you''ve heard a song, chances are you''ve heard a Strat. ', 'Date Manufactured': '1954'}
]

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
    return render(request, 'guitars/index.html', {
        'guitars': guitars
    })