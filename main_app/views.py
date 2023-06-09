from django.shortcuts import render

#Step 10.3 ADD your guitars for your ALL, my guy

guitars = [
    {'name': 'Les Paul', 'brand': 'Gibson', 'description': 'The GOAT', 'date': '1952', 'played': 'Duane Allman, Adam Jones, Jimmy Page'},
    {'name': 'Telecaster', 'brand': 'Fender', 'description': 'Snarling, visceral, bright and an absolute classic. Prince''s go-to which says it all', 'date': '1951', 'played': 'Prince, Curtis Mayfield, Joe Strummer, Bruce Springsteen, Keith Richards, J. Spaceman, Jonny Greenwood'},
    {'name': 'ES-355', 'brand': 'Gibson', 'description': 'The most iconic of all semi-hollowbody double cutaways. Versatile enough to fit any genre (and we do mean any genre).', 'date': '1958', 'played': 'B.B. King, Paul Westerberg, Leo Nocentelli, Gary Clark Jr.'},
    {'name': 'Stratocaster', 'brand': 'Fender', 'description': "Music's most famous instrument. If you''ve heard a song, chances are you''ve heard a Strat. ", 'date': '1954', 'played': 'David Gilmour, Jimi Hendrix, George Harrison, Eddie Hazel, Buddy Guy' },
    {'name': 'SG', 'brand': 'Gibson', 'description': "Lightweight, lightning-faast and absolutely legendary: this double cutaway. Sings especially well with P-90 pickups.", 'date': '1961', 'played': 'Derek Trucks, Tony Iommi, Carlos Santana, Jeff Tweedy'},
    {'name': '360', 'brand': 'Rickenbacker', 'description': 'Arguably the sound of the summer of love. Iconic, psychedlic, and truly an individual.', 'date': '1958', 'played': 'Tom Petty, John Lennon, Martin Gore'},
    {'name': 'Jazzmaster', 'brand': 'Fender', 'description': 'The Alt Queen. One-of-a-kind shimmer laced with beautiful enveloping lows not normally found in a Fender, the Jazzmaster has been the cutting edge of every indie movement.', 'date': '1958', 'played': 'Thom Yorke, Robert Smith, Thurston Moore, Tom Verlaine, Lee Ronaldo, Elvis Costello'},
    {'name': '', 'brand': '', 'description': '', 'date': '', 'played': ''},
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