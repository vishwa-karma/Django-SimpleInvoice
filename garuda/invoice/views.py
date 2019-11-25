from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.dates import MonthArchiveView
from .models import Invoice, Invoicee, Client
from .forms import InvoiceForm

# Create your views here.
class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 12

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
    template_name = 'invoice/invoice_form.html'
    fields = '__all__'

class InvoiceEdit(UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/invoice_edit.html'

class InvoiceDelete(DetailView):
    model = Invoice
    template_name = 'invoice/invoice_confirm_delete.html'
    success_url = reverse_lazy('invoice-list')

class InvoiceMonthArchiveView(MonthArchiveView):
    queryset = Invoice.objects.all()
    date_field = "invoice_date"
    allow_future = True

def RecipientView(request, r_name):
    recipent = Invoice.objects.all().filter(invoicee_name__exact=r_name)
    return render(request, 'invoice/list_by_name.html', {'recipent':recipent})
