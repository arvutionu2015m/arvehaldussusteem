from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
import uuid

# Valuuta valikud
CURRENCY_CHOICES = [
    ("EUR", "Euro (€)"),
    ("USD", "US Dollar ($)"),
    ("GBP", "British Pound (£)"),
]

# Maksutüübi valikud
TAX_CHOICES = [
    ("VAT", "Käibemaks"),
    ("SALES_TAX", "Müügimaks"),
    ("CORP_TAX", "Ettevõtte tulumaks"),
]

# Arve staatused
STATUS_CHOICES = [
    ("pending", "Ootel"),
    ("paid", "Makstud"),
    ("overdue", "Ületähtaegne"),
]


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Kasutaja seos
    invoice_number = models.CharField(max_length=20, unique=True, editable=False)
    client_name = models.CharField(max_length=200, verbose_name="Kliendi nimi")
    client_email = models.EmailField(verbose_name="E-post")
    client_address = models.TextField(blank=True, verbose_name="Aadress")
    client_phone = models.CharField(max_length=15, blank=True, verbose_name="Telefon")

    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Summa")
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="EUR", verbose_name="Valuuta")
    tax_type = models.CharField(max_length=10, choices=TAX_CHOICES, default="VAT", verbose_name="Maksutüüp")
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("20.00"), verbose_name="Maksumäär (%)")
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Kogusumma")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending", verbose_name="Staatus")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Loodud")
    due_date = models.DateField(null=True, blank=True, verbose_name="Maksetähtaeg")
    paid_at = models.DateTimeField(null=True, blank=True, verbose_name="Makstud kuupäev")

    def save(self, *args, **kwargs):
        """Automaatne arve numbrite genereerimine ja kogusumma arvutamine"""
        if not self.invoice_number:
            self.invoice_number = str(uuid.uuid4().hex[:10]).upper()  # Unikaalne arve ID
        self.total_amount = self.amount + (self.amount * self.tax_rate / Decimal(100))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Arve #{self.invoice_number} - {self.client_name}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Arve"
        verbose_name_plural = "Arved"
