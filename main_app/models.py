from django.db import models

# Create your models here.
class Guitar(models.Model):
    # Step 5.1 add FIELDS (charField lol Garfield, cat puns)
    # use CharField for a small text input
    # image = models.ImageField(upload_to='uploads/% Y/% m/% d', max_width=300)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    date = models.IntegerField()
    description = models.TextField(max_length=371)
    played = models.TextField(max_length=371)
    for_sale = models.BooleanField(default=False)
    price = models.DecimalField(default=0000.00, decimal_places=2, max_digits=10)

# VID 2 (Models) Step 6.0 MIGRATIONS
# make MIGRATIONS to update the database with your new MODEL
# be very very CAREFUL as this can cause a loss of data if done compulsively

# Step 6.1 -- SHOW MIGRATIONS
# show migrations to see what needs to be updated
# python3 manage.py showmigrations

# Step 6.2 -- RUN MIGRATIONS
# run migrations to link new MODEL to DATABASE
# python3 manage.py migrate

# if done correctly you'll get rad green OK messages
# and a 0001_initial file in your migrations directory

# VID 2 (Models) Step 7.0 ORM

# Step 7.1 use ORM to CRUD Data in a PYTHON INTERACTIVE SHELL
# python3 manage.py shell
# this will load a >>> prompt meaning ORM is active

# Step 7.2 (C - CREATE) IMPORT model to DB
# >>> from main_app.models import Guitar
# test by pressing enter

# Step 7.3 RETRIEVE all OBJECTS using all()
# >>> Guitar.objects.all()
# should return a QuerySet

# Step 7.4 CREATING a NEW OBJECT 
# all data must be provided as a KWARG
# >>> g = Guitar(
# name="Esquire Telecaster", 
# brand='Fender',
# description='Snarling, visceral, bright and an absolute classic. Prince''s go-to which says it all', 
# date='1951', 
# played='Prince, Curtis Mayfield, Joe Strummer, Bruce Springsteen, Keith Richards, J. Spaceman, Jonny Greenwood',
# for_sale=True,
# price=22450.00
# )

# confirm by entering g in python shell

# Step 7.5 SAVE the NEW OBJECT to DATABASE
# enter g.__dict__ to see the new Object's info
# use save() and check it was assigned an ID
# >>> g.save()
# >>> g.id 

# Step 7.6 CONFIRM the NEW OBJECT is in DB
# >>> Guitar.objects.all()
# should return a QuerySet with an object

# Step 7.7 ADD a STR METHOD to MODEL
# changing this INSTANCE METHOD does not impact the DATABASE,
# therefore no makemigrations are necessary

def __str__(self):
    return f'{self.name} ({self.id})'

# Step 7.8 RELOAD the SHELL
# use exit() or crtl+D to leave the shell
# relaunch the shell using python3 manage.py shell
# RE-IMPORT your MODEL
# from main_app.models import Guitar


# Step 7.9 (U - UPDATE) UPDATE an OBJECT

# to view the FIRST ROW of your DB use first()
# to view the LAST ROW of your DB use last()
# SELECT the attribute using first() or last()
# then OVERRIDE the VALUE you want using dot notation
# then SAVE it using save()
# (Example)
# >>> g = Guitars.objects.first()
# >>> g
#  <Guitars: Esquire Telecaster>
# >>> g.name = 'Telecaster'
# >>> g.save()
# >>> g
# <Guitars: Telecaster>

# Step 7.10 FILTERING / QUERING for RECORDS objects.filter()
# these kinds of queries are called FIELD LOOKUPS
# >>> Guitars.objects.filter(name="Telecaster")
# <QuerySet [<Guitars: Telecaster>]>

# you can use contains, gte and lte to filter search
# >>> Guitars.objects.filter(name_contains='Caster')
# >>> Guitars.objects.filter(date_lte=1951)

# Step 7.11 RETURN A SINGLE RECORD / SINGLE OBJECT get()
# use GET METHOD and provide an ID #
# >>> Guitars.objects.get(id=1)

# Step 7.12 ORDERING OBJECTS (SHORTING) order_by('')
# use the ORDER BY METHOD
# >>> Guitars.objects.order_by('date')

# for DESCENDING ORDER use a negative sign before string
# Guitars.objects.order_by('-date')

# it can be INDEXED too if you need
# >>> Guitars.objects.order_by('-date')[0]