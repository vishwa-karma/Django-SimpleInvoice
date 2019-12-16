from django.urls import path
from .views import InvoiceListView, InvoiceDetailView, InvoiceCreateView, InvoiceEdit, InvoiceDelete, InvoiceMonthArchiveView, dummy
from . import views
from django.views.generic.dates import ArchiveIndexView
from .models import Invoice

urlpatterns = [
    #path('', InvoiceListView.as_view(), name='invoice-list'),
    path('', views.seva, name='seva-kitchen'),
    path('poster/', views.seva_poster, name='seva-poster'),
    path('tiffin/', views.seva_tiffin, name='seva-tiffin'),
    path('pitara/', views.seva_pitara, name='seva-pitara'),
    path('food/', views.seva_food, name='seva-food'),
    path('news/', views.seva_news, name='seva-news'),
    path('jars/', views.seva_jars, name='seva-jars'),
    path('<int:pk>', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('<int:pk>/edit/', InvoiceEdit.as_view(), name='invoice-update'),
    path('<int:pk>/delete/', InvoiceDelete.as_view(), name='invoice-delete'),
    path('archive/', ArchiveIndexView.as_view(model=Invoice, date_field = 'invoice_date'), name = 'invoice-archive'),
    # Example: /2012/08/
    path('<int:year>/<int:month>/',
         InvoiceMonthArchiveView.as_view(month_format='%m'),
         name="archive_month_numeric"),
    # Example: /2012/aug/
    path('<int:year>/<str:month>/',
         InvoiceMonthArchiveView.as_view(),
         name="archive_month"),
    path('invoicee/<str:r_name>/', views.RecipientView, name = 'recipient'),
    path('client/<str:c_name>/', views.ListbyClient, name = 'client'),
    path('vendor/<str:v_name>/', views.ListbyVendor, name = 'vendor'),    
    path('dummy/<int:pk>', dummy, name = 'dummy'),
    path('render/pdf/<int:pk>', views.GeneratePdf.as_view(), name = 'pdf_print'),
]