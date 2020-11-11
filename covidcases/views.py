from django.shortcuts import render
from django.http import JsonResponse
from .models import Country, State, County

def index(request):
    countries=Country.objects.all()
    states=State.objects.all()
    counties=County.objects.all()
    context={"countries":countries,"states":states,"counties":counties}
    return render(request,"covidcases/index.html",context)

def update(request):
    countryname= request.GET['countryname']
    countrycases = request.GET['countrycases']
    countrydeaths = request.GET['countrydeaths']
    countryrecovered = request.GET['countryrecovered']
    statename = request.GET['statename']
    statecases = request.GET['statecases']
    statedeaths = request.GET['statedeaths']
    staterecovered = request.GET['staterecovered']
    countyname = request.GET['countyname']
    countycases = request.GET['countycases']
    countydeaths = request.GET['countydeaths']
    countyrecovered = request.GET['countyrecovered']

    country,newcountry= Country.objects.update_or_create(name=countryname,defaults={'cases':countrycases,"deaths":countrydeaths,"recovered":countryrecovered})
    state,newstate= State.objects.update_or_create(name=statename,defaults={'country_id':country,"cases":statecases,'deaths':statedeaths,'recovered':staterecovered})
    county,newcounty= County.objects.update_or_create(name=countyname,defaults={'state_id':state,'cases':countycases,'deaths':countydeaths,'recovered':countyrecovered})
    return JsonResponse({"success":True})

#/update?countryname=United States&countrycases=0&countrydeaths=1&countryrecovered=2&statename=Texas&statecases=3&statedeaths=4&staterecovered=5&countyname=Dallas&countycases=7&countydeaths=8&countyrecovered=9
