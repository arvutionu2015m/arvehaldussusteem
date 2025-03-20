from django.urls import path
from .views import home, create_invoice, invoice_detail, send_invoice_email, delete_invoice, download_invoice, pay_invoice, invoice_list, payment_success, payment_cancel
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", home, name="home"),
    path("create/", create_invoice, name="create_invoice"),
    path("invoices/", invoice_list, name="invoice_list"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("invoice/<int:invoice_id>/", invoice_detail, name="invoice_detail"),
    path("download-invoice/<int:invoice_id>/", download_invoice, name="download_invoice"),
    path("send-invoice/<int:invoice_id>/", send_invoice_email, name="send_invoice"),  # VÄGA OLULINE!
    path("delete-invoice/<int:invoice_id>/", delete_invoice, name="delete_invoice"),
    path("pay/<int:invoice_id>/", pay_invoice, name="pay_invoice"),
    path("payment-success/", payment_success, name="payment_success"),
    path("payment-cancel/", payment_cancel, name="payment_cancel"),
]
