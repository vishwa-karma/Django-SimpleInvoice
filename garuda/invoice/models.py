from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Invoicee(models.Model):
    r_name = models.CharField(verbose_name = "Recipient", max_length = 50, unique = True)
    email_id = models.EmailField(verbose_name = "Email ID", unique = True)
    phone_num = models.CharField(verbose_name = "Phone", unique=True, max_length=15)
    bank = models.CharField(verbose_name = "Bank Name", max_length = 50)
    branch = models.CharField(verbose_name = "Branch Name", max_length = 50)
    acc_no = models.CharField(verbose_name = "Account #", max_length = 50)
    ifsc = models.CharField(verbose_name = "IFS Code", max_length = 12)
    pan_no = models.CharField(verbose_name = "PAN #", max_length = 10)

    def __str__(self):
        return self.r_name


class Client(models.Model):
    c_name = models.CharField(verbose_name = "Client", max_length = 70, unique = True)

    def __str__(self):
        return self.c_name

class Location(models.Model):
    location = models.CharField(verbose_name = 'Location', max_length = 50, unique = True)

    def __str__(self):
        return self.location

class Vendor(models.Model):
    v_name = models.CharField(verbose_name = "Vendor", max_length = 70, unique = True)
    v_address = models.TextField(verbose_name="Address", unique= True)

    def __str__(self):
        return self.v_name

class Invoice(models.Model):
    invoice_num = models.CharField(verbose_name = "Invoice Number", max_length = 10, unique = True)
    po_number =  models.CharField(verbose_name = "Purchase Order Number", max_length = 20, unique = True, null=True)
    invoice_date = models.DateField(auto_now=False, default=timezone.now)
    service = models.CharField(max_length = 100)
    unt_price = models.IntegerField(verbose_name = "Unit Price")
    n_days = models.IntegerField(verbose_name="No. of Days")
    #total_price = models.IntegerField(blank=True, editable=False)
    cab_price = models.IntegerField(default=0)
    total_price_no_tax = models.IntegerField(blank=True, editable=False,)
    sgst = models.IntegerField(verbose_name = 'SGST', blank=True, editable=True)
    gst = models.IntegerField(verbose_name='GST', blank=True, editable=False, default=0)
    grand_total = models.IntegerField(blank=True, editable=False)

    vendor_name = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    #v_address = models.ForeignKey(Vendor, related_name='vendor_address', to_field='v_address', on_delete=models.PROTECT, editable=True, blank=True)

    invoicee_name = models.ForeignKey(Invoicee,  on_delete=models.PROTECT)
    #invoicee_mail = models.ForeignKey(Invoicee, related_name='invoicee_email', to_field='email_id', on_delete=models.PROTECT, editable=False, null=True)
    #invoicee_phone = models.ForeignKey(Invoicee, related_name='phone', to_field='phone_num', on_delete=models.PROTECT, editable=False, null=True)
    
    client_name = models.ForeignKey(Client, on_delete=models.PROTECT)
    client_loc = models.ForeignKey(Location, on_delete=models.PROTECT)
    po_upload = models.FileField(verbose_name="Upload Purchase Order", upload_to="po", )
    
    def calculate_total_price_no_tax(self):
        total_price = self.unt_price * self.n_days
        total_price_no_tax = total_price + self.cab_price

        return total_price_no_tax

    def calculate_tax(self):
        total_price = self.unt_price * self.n_days
        sgst = total_price * 0.09

        return sgst

    def calc_grand_total(self):
        grand_total = self.total_price_no_tax + self.sgst * 2

        return grand_total

    def cal_gst(self):
        gst = self.sgst * 2

        return gst

    def save(self, *args, **kwargs):
        self.sgst = self.calculate_tax()
        self.total_price_no_tax = self.calculate_total_price_no_tax()
        self.grand_total = self.calc_grand_total()
        self.gst = self.cal_gst()
        super().save(*args, **kwargs)
    
    def __str__(self):
        #firlds = (self.invoice_date, self.invoice_num, self.invoicee_name, self.client_name)
        return self.invoice_num

    def get_absolute_url(self):
        return reverse('invoice-list')