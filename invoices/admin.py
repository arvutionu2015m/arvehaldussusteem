from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "client_name", "total_amount", "currency", "created_at", "is_paid")
    search_fields = ("client_name", "invoice_number")
    list_filter = ("status", "currency")

    def is_paid(self, obj):
        return obj.status == "paid"

    is_paid.boolean = True  # Kuvab administraatoris ikooni ✅ / ❌
    is_paid.short_description = "Makstud?"

