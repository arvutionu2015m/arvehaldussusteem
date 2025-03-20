# Generated by Django 5.1.7 on 2025-03-19 18:38

import django.db.models.deletion
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ['-created_at'], 'verbose_name': 'Arve', 'verbose_name_plural': 'Arved'},
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='paid',
        ),
        migrations.AddField(
            model_name='invoice',
            name='client_address',
            field=models.TextField(blank=True, verbose_name='Aadress'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='client_phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Telefon'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Maksetähtaeg'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='paid_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Makstud kuupäev'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('pending', 'Ootel'), ('paid', 'Makstud'), ('overdue', 'Ületähtaegne')], default='pending', max_length=10, verbose_name='Staatus'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Summa'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='client_email',
            field=models.EmailField(max_length=254, verbose_name='E-post'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='client_name',
            field=models.CharField(max_length=200, verbose_name='Kliendi nimi'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Loodud'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro (€)'), ('USD', 'US Dollar ($)'), ('GBP', 'British Pound (£)')], default='EUR', max_length=3, verbose_name='Valuuta'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(editable=False, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax_rate',
            field=models.DecimalField(decimal_places=2, default=Decimal('20.00'), max_digits=5, verbose_name='Maksumäär (%)'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax_type',
            field=models.CharField(choices=[('VAT', 'Käibemaks'), ('SALES_TAX', 'Müügimaks'), ('CORP_TAX', 'Ettevõtte tulumaks')], default='VAT', max_length=10, verbose_name='Maksutüüp'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Kogusumma'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kasutaja'),
        ),
    ]
