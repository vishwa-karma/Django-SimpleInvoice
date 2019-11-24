from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Invoice, Invoicee, Client

# Create your views here.
class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InvoiceDetailView(DetailView):
    model = Invoice

    def get_invoice_data(self, **kwargs):
        inv = super().get_context_data(**kwargs)
        return inv

class InvoiceCreateView(CreateView):
    model = Invoice
    fields = '__all__'