from django.urls import path
from .views import InvoiceListView, InvoiceDetailView, InvoiceCreateView

urlpatterns = [
    path('', InvoiceListView.as_view(), name='invoice-list'),
    path('<int:pk>', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
]