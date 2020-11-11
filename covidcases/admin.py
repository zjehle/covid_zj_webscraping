from django.contrib import admin
from .models import Country,State,County
admin.site.register(County)
admin.site.register(State)
admin.site.register(Country)
