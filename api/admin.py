from django.contrib import admin
from .models import Chemical, ChemCompo, Commodity
# Register your models here.

admin.site.register([Chemical, ChemCompo, Commodity])