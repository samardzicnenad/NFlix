# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
    idmovie = models.IntegerField(primary_key=True, db_column='idMovie') # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True) # Field name made lowercase.
    reldate = models.CharField(max_length=12L, db_column='RelDate', blank=True) # Field name made lowercase.
    vidreldate = models.CharField(max_length=12L, db_column='VidRelDate', blank=True) # Field name made lowercase.
    urlimdb = models.TextField(db_column='urlIMDB', blank=True) # Field name made lowercase.
    unknown = models.IntegerField(null=True, db_column='Unknown', blank=True) # Field name made lowercase.
    action = models.IntegerField(null=True, db_column='Action', blank=True) # Field name made lowercase.
    adventure = models.IntegerField(null=True, db_column='Adventure', blank=True) # Field name made lowercase.
    animation = models.IntegerField(null=True, db_column='Animation', blank=True) # Field name made lowercase.
    children_s = models.IntegerField(null=True, db_column="Children's", blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    comedy = models.IntegerField(null=True, db_column='Comedy', blank=True) # Field name made lowercase.
    crime = models.IntegerField(null=True, db_column='Crime', blank=True) # Field name made lowercase.
    documentary = models.IntegerField(null=True, db_column='Documentary', blank=True) # Field name made lowercase.
    drama = models.IntegerField(null=True, db_column='Drama', blank=True) # Field name made lowercase.
    fantasy = models.IntegerField(null=True, db_column='Fantasy', blank=True) # Field name made lowercase.
    film_noir = models.IntegerField(null=True, db_column='Film-Noir', blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    horror = models.IntegerField(null=True, db_column='Horror', blank=True) # Field name made lowercase.
    musical = models.IntegerField(null=True, db_column='Musical', blank=True) # Field name made lowercase.
    mystery = models.IntegerField(null=True, db_column='Mystery', blank=True) # Field name made lowercase.
    romance = models.IntegerField(null=True, db_column='Romance', blank=True) # Field name made lowercase.
    sci_fi = models.IntegerField(null=True, db_column='Sci-Fi', blank=True) # Field name made lowercase. Field renamed to remove unsuitable characters.
    thriller = models.IntegerField(null=True, db_column='Thriller', blank=True) # Field name made lowercase.
    war = models.IntegerField(null=True, db_column='War', blank=True) # Field name made lowercase.
    western = models.IntegerField(null=True, db_column='Western', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'movie'

class Rating(models.Model):
    idrating = models.IntegerField(primary_key=True, db_column='idRating') # Field name made lowercase.
    iduser = models.IntegerField(db_column='idUser') # Field name made lowercase.
    idmovie = models.IntegerField(db_column='idMovie') # Field name made lowercase.
    rating = models.FloatField(db_column='Rating') # Field name made lowercase.
    timestamp = models.CharField(max_length=15L, db_column='TimeStamp', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'rating'

class User(models.Model):
    iduser = models.IntegerField(primary_key=True, db_column='idUser') # Field name made lowercase.
    age = models.IntegerField(null=True, db_column='Age', blank=True) # Field name made lowercase.
    sex = models.CharField(max_length=1L, db_column='Sex', blank=True) # Field name made lowercase.
    occupation = models.CharField(max_length=45L, db_column='Occupation', blank=True) # Field name made lowercase.
    zip = models.CharField(max_length=10L, db_column='ZIP', blank=True) # Field name made lowercase.
    username = models.CharField(max_length=15L, db_column='Username') # Field name made lowercase.
    password = models.CharField(max_length=15L, db_column='Password') # Field name made lowercase.    
    class Meta:
        db_table = 'user'