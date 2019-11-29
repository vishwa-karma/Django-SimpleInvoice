from django.contrib import admin
from .models import Invoicee, Invoice, Client, Vendor, Location

# Register your models here.
admin.site.register(Invoicee)
admin.site.register(Invoice)
admin.site.register(Client)
admin.site.register(Vendor)
admin.site.register(Location)