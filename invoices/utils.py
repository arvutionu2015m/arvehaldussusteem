import qrcode
import stripe
import io
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY  # Stripe API võti `settings.py`-st

def generate_invoice_pdf(invoice):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Pealkiri
    title = Paragraph(f"<b>ARVE #{invoice.invoice_number}</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Kliendi info
    client_info = f"""
    <b>Kliendi nimi:</b> {invoice.client_name}<br/>
    <b>E-post:</b> {invoice.client_email}<br/>
    <b>Maksetähtaeg:</b> {invoice.due_date.strftime('%d.%m.%Y') if invoice.due_date else "Pole määratud"}
    """
    elements.append(Paragraph(client_info, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Arve tabel
    data = [
        ["Toode/Teenuse nimetus", "Kogus", "Hind", "Käibemaks (%)", "Kokku"],
        ["Teenused", "1", f"{invoice.amount} {invoice.currency}", f"{invoice.tax_rate}%", f"{invoice.total_amount} {invoice.currency}"]
    ]
    
    table = Table(data, colWidths=[2.5 * inch, 1 * inch, 1.5 * inch, 1.5 * inch, 1.5 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Stripe makselingi loomine
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": invoice.currency.lower(),
                "product_data": {"name": f"Arve #{invoice.invoice_number}"},
                "unit_amount": int(invoice.total_amount * 100),  # Stripe kasutab sente
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="http://127.0.0.1:8000/payment-success/",
        cancel_url="http://127.0.0.1:8000/payment-cancel/",
    )
    stripe_payment_url = session.url

    # QR-koodi genereerimine Stripe makselingiga
    qr = qrcode.make(stripe_payment_url)
    qr_path = f"invoice_qr_{invoice.invoice_number}.png"
    qr.save(qr_path)

    # Lisa QR-kood PDF-i
    elements.append(Paragraph("<b>Maksa QR-koodi abil:</b>", styles["Normal"]))
    elements.append(Spacer(1, 6))
    elements.append(Image(qr_path, width=150, height=150))
    elements.append(Spacer(1, 12))

    # Kokkuvõte ja makselink
    summary_text = f"""
    <b>Kogusumma:</b> {invoice.total_amount} {invoice.currency}<br/>
    <b>Staatus:</b> <font color="{'green' if invoice.status == 'paid' else 'red'}">{'Makstud' if invoice.status == 'paid' else 'Ootel'}</font>
    """
    elements.append(Paragraph(summary_text, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Lisa makselink ReportLabis
    link_text = f'<u><font color="blue">Maksa kohe Stripe kaudu</font></u>'
    link = Paragraph(f'<link href="{stripe_payment_url}">{link_text}</link>', styles["Normal"])
    elements.append(link)
    elements.append(Spacer(1, 12))

    doc.build(elements)
    buffer.seek(0)
    return buffer
