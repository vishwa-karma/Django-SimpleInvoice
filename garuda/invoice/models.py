from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Invoicee(models.Model):
    r_name = models.CharField(verbose_name = "Recipient", max_length = 50, unique = True)
    email_id = models.EmailField(verbose_name = "Email ID", unique = True)
    phone_num = models.CharField(verbose_name = "Phone", unique=True, max_length=15)

    def __str__(self):
        return self.r_name

    def get_absolute_url(self):
        return reverse('invoicee-detail', kwargs={'pk': self.pk})

class Client(models.Model):
    c_name = models.CharField(verbose_name = "Client", max_length = 70, unique = True)
    c_adrress = models.TextField(verbose_name="Address")
    location = models.CharField(max_length = 50)

    def __str__(self):
        return self.c_name

class Invoice(models.Model):
    invoice_num = models.CharField(max_length = 10, unique = True)
    invoice_date = models.DateField(auto_now=False, default=timezone.now())
    service = models.CharField(max_length = 100)
    unt_price = models.IntegerField()
    n_days = models.IntegerField()
    total_price = models.IntegerField(blank=True, editable=False, )
    cab_price = models.IntegerField(default=0)
    client_name = models.ForeignKey(Client, to_field='c_name', on_delete=models.PROTECT)
    invoicee_name = models.ForeignKey(Invoicee, to_field='r_name', on_delete=models.PROTECT)

    def calculate_total_price(self):
        total_price = self.unt_price * self.n_days
        total_price += self.cab_price

        return total_price

    def save(self, *args, **kwargs):
        self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)
    
    def __str__(self):
        firlds = (self.invoice_date, self.invoice_num, self.invoicee_name, self.client_name)
        return str(firlds)