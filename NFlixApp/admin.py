from django.contrib import admin
from NFlixApp.models import User, Movie, Rating

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Rating)
