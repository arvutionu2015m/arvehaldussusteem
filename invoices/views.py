from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice
from .forms import InvoiceForm
from django.core.mail import EmailMessage
from django.contrib import messages
from .utils import generate_invoice_pdf
from django.template.loader import render_to_string
from django.http import FileResponse
from django.utils.html import strip_tags
from django.utils.timezone import now
import stripe
from .models import Invoice
from decimal import Decimal

stripe.api_key = "sk_test_51MGhlHFHOhOaGyjmWRw9emtELKB1DoFgvfuiUDlIGiPpuCcIf74PZ7HKKGgoc4LLtVcbmBxDnnLvBEtNvj4AtUhQ00UCCmcvSx"

def payment_success(request):
    return render(request, "payment_success.html")

def payment_cancel(request):
    return render(request, "payment_cancel.html")

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, "invoice_list.html", {"invoices": invoices})

def pay_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": invoice.currency.lower(),
                "product_data": {"name": f"Arve #{invoice.invoice_number}"},
                "unit_amount": int(invoice.total_amount * 100),
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="https://http://127.0.0.1:8000/payment-success/",
        cancel_url="https://http://127.0.0.1:8000/payment-cancel/",
    )
    
    return redirect(session.url)

def send_invoice_email(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)

    try:
        pdf = generate_invoice_pdf(invoice)
        subject = f"Teie arve #{invoice.invoice_number}"
        html_message = render_to_string("emails/invoice_email_template.html", {"invoice": invoice})
        plain_message = strip_tags(html_message)  # Tekstiversioon HTML kirjast
        from_email = "arnopps@gmail.com"
        to_email = [invoice.client_email]

        email = EmailMessage(subject, plain_message, from_email, to_email)
        email.attach_alternative(html_message, "text/html")  # Lisab HTML-versiooni
        email.attach(f"invoice_{invoice.invoice_number}.pdf", pdf.getvalue(), "application/pdf")
        email.send()

        invoice.sent_at = now()
        invoice.save()
        
    except Exception as e:
        return render(request, "invoice_sent.html", {"invoice": invoice, "error": str(e)})

    return render(request, "invoice_sent.html", {"invoice": invoice})

def download_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    pdf = generate_invoice_pdf(invoice)
    response = FileResponse(pdf, as_attachment=True, filename=f"invoice_{invoice.invoice_number}.pdf")
    return response

def home(request):
    invoices = Invoice.objects.all()
    return render(request, "home.html", {"invoices": invoices})

def create_invoice(request):
    if request.method == "POST":
        client_name = request.POST.get("client_name")
        client_email = request.POST.get("client_email")
        amount = Decimal(request.POST.get("amount"))  # Kasuta Decimal
        tax_rate = Decimal(request.POST.get("tax_rate"))  # Kasuta Decimal
        total_amount = amount + (amount * tax_rate / Decimal(100))  # Decimal jagamise probleem lahendatud
        status = request.POST.get("status")

        invoice = Invoice.objects.create(
            user=request.user,  # Lisa sisse logitud kasutaja
            client_name=client_name,
            client_email=client_email,
            amount=amount,
            tax_rate=tax_rate,
            total_amount=total_amount,
            status=status
        )

        messages.success(request, f"Arve #{invoice.invoice_number} loodud edukalt!")
        return redirect("home")

    return render(request, "create_invoice.html")

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, "invoice_detail.html", {"invoice": invoice})

def send_invoice_email(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    pdf = generate_invoice_pdf(invoice)
    
    email = EmailMessage(
        subject=f"Teie arve {invoice.invoice_number}",
        body="Siin on Teie arve PDF-formaadis.",
        from_email="arnopps@gmail.com",
        to=[invoice.client_email],
    )
    email.attach(f"invoice_{invoice.invoice_number}.pdf", pdf.getvalue(), "application/pdf")
    email.send()

    return render(request, "invoice_sent.html", {"invoice": invoice})

def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice.delete()
    return redirect("home")
