# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from NFlixApp.models import User, Movie, Rating
from django.db.models import Q

from random import randrange

idOwner, nameOwner, startLetter = 0, "", "A"


def index(request):
    global idOwner, nameOwner, startLetter
    note = "Please enter your username and password."
    if request.method == "POST":
        username = request.POST.get("UserName", "")
        password = request.POST.get("Password", "")

        if username == "" or password == "":
            note = "Neither username nor password can be blank! Please, try again!"
            return render(request, "NFlixApp/index.html", {"note": note, "username": username})
        tryUser = User.objects.filter(username = username, password = password)
        if tryUser.exists():
            idOwner, nameOwner = tryUser[0].iduser, username
            return HttpResponseRedirect("/NFlixApp/recs/")
        else:
            note = "The username or password you entered is incorrect! Please, try again!"
            return render(request, "NFlixApp/index.html", {"note": note, "username": username})
    else:
        idOwner, nameOwner, startLetter = 0, "", "A"
    return render(request, "NFlixApp/index.html", {"note": note, "username": ""})


def register(request):
    global idOwner, nameOwner
    username, password, confirm_password, age, ssex, occupation, zip_code = "", "", "", "", "F", "", ""
    note="Use the form below to create a new account"
    sexlist = [("F", "Female"), ("M", "Male")]
        
    if request.method == "POST":
        username = request.POST.get("UserName", "")
        password = request.POST.get("Password", "")
        confirm_password = request.POST.get("ConfirmPassword", "")
        age = request.POST.get("Age", "")
        ssex = request.POST.get("Sex", "")
        occupation = request.POST.get("Occupation", "")
        zip_code = request.POST.get("ZIP", "")
        
        if username == "" or password == "" or zip_code == "" or age== "":
            note = "All fields are required! Please, try again!"
            return render(request, "NFlixApp/register.html", {"note": note, "username": username, "age": age, "sexlist": sexlist,
                                                              "ssex": ssex, "occupation": occupation, "zip_code": zip_code})
        if password != confirm_password:
            note = "Passwords do not match! Please, try again!"
            return render(request, "NFlixApp/register.html", {"note": note, "username": username, "age": age, "sexlist": sexlist,
                                                              "ssex": ssex, "occupation": occupation, "zip_code": zip_code})
        try:
            nAge = int(age)
        except:
            note = "Age must be number between 2 and 122! Please, try again!"
            return render(request, "NFlixApp/register.html", {"note": note, "username": username, "age": "", "sexlist": sexlist,
                                                              "ssex": ssex, "occupation": occupation, "zip_code": zip_code})
        if int(age)<2 or int(age)>122:
            note = "Age must be number between 2 and 122! Please, try again!"
            return render(request, "NFlixApp/register.html", {"note": note, "username": username, "age": "", "sexlist": sexlist,
                                                              "ssex": ssex, "occupation": occupation, "zip_code": zip_code}) 
        try:
            nAge = int(zip_code)
        except:
            note = "ZIP code must be 5 digit number! Please, try again!"
            return render(request, "NFlixApp/register.html", {"note": note, "username": username, "age": age, "sexlist": sexlist,
                                                              "ssex":ssex, "occupation": occupation, "zip_code": ""})
        if int(zip_code)<0 or int(zip_code)>99999 or len(zip_code) != 5:
            note = "ZIP code must be 5 digit number! Please, try again!"
            return render(request, "NFlixApp/register.html", {"note": note, "username": username, "age": age, "sexlist": sexlist,
                                                              "ssex": ssex, "occupation": occupation, "zip_code": ""})
        tryUser = User.objects.filter(username = username)
        if tryUser.exists():
            note = "Username already exist! Please, try again!"
            return render(request, "NFlixApp/register.html", {"note": note, "username": "", "age": age, "sexlist": sexlist,
                                                              "ssex": ssex, "occupation": occupation, "zip_code": zip_code})
        else:
            newUser = User(age = age, sex = ssex, occupation = occupation, zip = zip_code, username = username, password = password)
            newUser.save()
            newU = User.objects.filter(username = username)
            idOwner, nameOwner = newU[0].iduser, username
            return HttpResponseRedirect("/NFlixApp/recs/")
    return render(request, "NFlixApp/register.html", {"note": note, "username": "", "sexlist": sexlist, "ssex": ssex})


def recs(request):
    global idOwner, nameOwner, startLetter
    slCopy = startLetter
    if idOwner == 0: #Attempt to hit this page directly - don't allow; redirect to home
        nameOwner = ""
        return HttpResponseRedirect("/NFlixApp/")
    if request.method == "POST":
        for key in request.POST.keys():
            if key not in ["rmovie", "csrfmiddlewaretoken", "mr"]: # 3 parameters that POST sends, check for additional
                startLetter = key
        rmovie = request.POST.get("rmovie", "")
        mrating = float(request.POST.get("mr", ""))
        if startLetter == "Rate" and rmovie != "": #user pressed "RATE" button
            getMovie=Movie.objects.filter(title=rmovie)
            if getMovie.exists():
                tryRating, created = Rating.objects.get_or_create(iduser = idOwner, idmovie = getMovie[0].idmovie,
                  defaults={'rating': mrating})
                if not created:
                    newRating = Rating(idrating = tryRating.idrating, iduser = idOwner, idmovie = getMovie[0].idmovie, rating = mrating)
                    newRating.save()
            else:
                newMovie = Movie(title=rmovie)
                newMovie.save()
                newM=Movie.objects.filter(title=rmovie)
                newRating = Rating(iduser = idOwner, idmovie = newM[0].idmovie, rating = mrating)
                newRating.save()
    if startLetter == "Rate":
        startLetter= slCopy
    getMovies = Movie.objects.filter(Q(title__startswith=startLetter) | Q(title__startswith=startLetter.lower())).order_by('title')
    return render(request, "NFlixApp/recs.html", {"note": "", "response": getMovies, "startLetter": startLetter, "idUser": idOwner, "username": nameOwner})


def receng(request):
    global idOwner, nameOwner
    searchuser = ""
    result = ""
    note = ""
    if idOwner == 0: #Attempt to hit this page directly - don't allow; redirect to home
        nameOwner = ""
        return HttpResponseRedirect("/NFlixApp/")
    if request.method == "POST":
        searchuser = request.POST.get("UserName", "")
        try:
            nSearchUser = int(searchuser)
        except:
            note = "User ID must be numeric! Please, try again!"
            return render(request, "NFlixApp/receng.html", {"note": note, "idUser": str(idOwner), 
                "username":nameOwner, "searchuser": ""})
        userRates = Rating.objects.filter(iduser = int(searchuser))
        if userRates.exists():
            from rec_engine import SimpleRecEngine
            from database import InMemoryDB
            db = InMemoryDB()
            
            db.loadNFDB()
        
            from similarity import Euclidian
            sim = Euclidian()
            
            engine = SimpleRecEngine(db, sim)
            result = engine.topN(int(searchuser), 25) #25 is parameter that can be changed - number of movies returned
            return render(request, "NFlixApp/receng.html", {"note": note, "response": result, 
                "username":nameOwner, "idUser": idOwner, "searchuser": searchuser})
        else:
            note = "That user hasn't rated any movie, so he/she cannot receive any recommendation!"
            return render(request, "NFlixApp/receng.html", {"note": note, "response": result, 
                "username":nameOwner, "idUser": idOwner, "searchuser": searchuser})
    return render(request, "NFlixApp/receng.html", {"note": note, "idUser": str(idOwner), "username": nameOwner})