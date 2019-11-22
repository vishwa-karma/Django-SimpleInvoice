from django.contrib import admin
from invoice.models import Invoicee, Invoice, Client

# Register your models here.
admin.site.register(Invoicee)
admin.site.register(Invoice)
admin.site.register(Client)