from django.shortcuts import render, get_list_or_404, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.http import HttpRequest
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.dates import MonthArchiveView
from .models import Invoice, Invoicee, Client, Vendor
from .forms import InvoiceForm, InvoiceCreateForm
from django.http import HttpResponse
from django.views.generic import View
from invoice.utils import Render
from django.contrib.auth.forms import UserCreationForm


def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


# Create your views here.
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    
class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice/invoice_detail1.html'

    def get_context_data(self, **kwargs):
        inv = super().get_context_data(**kwargs)
        return inv


class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceCreateForm
    template_name = 'invoice/invoice_form.html'
    # fields = '__all__'


class InvoiceEdit(UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoice/invoice_edit.html'


class InvoiceDelete(DeleteView):
    model = Invoice
    template_name = 'invoice/invoice_confirm_delete.html'
    success_url = reverse_lazy('invoice-list')


class InvoiceMonthArchiveView(MonthArchiveView):
    queryset = Invoice.objects.all()
    date_field = "invoice_date"
    allow_future = True


def RecipientView(request, r_name):
    recipent = Invoice.objects.filter(invoicee_name__r_name=r_name)
    return render(request, 'invoice/list_by_name.html', {'recipent': recipent})


def ListbyClient(request, c_name):
    queryset = Invoice.objects.filter(client_name__c_name=c_name)
    recipent = get_list_or_404(queryset)
    return render(request, 'invoice/list_by_client.html', {'recipent': recipent})


def ListbyVendor(request, v_name):
    queryset = Invoice.objects.all().filter(vendor_name__v_name=v_name)
    recipent = get_list_or_404(queryset)
    return render(request, 'invoice/list_by_vendor.html', {'recipent': recipent})


class GeneratePdf(View):

    def get(self, request, pk):
        invoices = Invoice.objects.get(pk=pk)
        data = {
            'object': invoices
        }
        pdf = Render.render('invoice/invoice_print.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def dummy1(request, pk):
    queryset = Invoice.objects.filter(pk=pk)
    recipent = get_object_or_404(queryset)
    queryset1 = Vendor.objects.filter(invoice=pk)
    queryset2 = Invoicee.objects.filter(invoice=pk)
    invoicee = get_object_or_404(queryset2)
    vendor = get_object_or_404(queryset1)
    print(type(invoicee))
    output = {'a': recipent,
              'b': vendor,
              'c': invoicee}
    return render(request, 'invoice/invoice_detail2.html', {'data': output})


def dummy(request, pk):
    queryset = Invoice.objects.get(pk=pk)
    # output = get_object_or_404(queryset)

    return render(request, 'invoice/invoice_detail3.html', {'data': queryset})


def seva(request):
    return render(request, 'seva/home.html')


def seva_poster(request):
    return render(request, 'seva/poster.html')


def seva_tiffin(request):
    return render(request, 'seva/tiffin.html')


def seva_jars(request):
    return render(request, 'seva/jars.html')


def seva_pitara(request):
    return render(request, 'seva/pitara.html')


def seva_news(request):
    return render(request, 'seva/In_The_News.html')


def seva_food(request):
    return render(request, 'seva/excess_food.html')
