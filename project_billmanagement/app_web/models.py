from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_title = models.CharField(max_length=200, null=False, blank=False)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=200, null=True, blank=True)
    # product price needs to update only when new month starts after the end of current month and report is generated
    current_product_price = models.FloatField(null=False, blank=False)
    tax_rate = models.FloatField(null=False, blank=False)
    product_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_title

class ProductPriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    old_price = models.FloatField(null=False, blank=False)
    new_price = models.FloatField(null=False, blank=False)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Price change for {self.product.product_title} on {self.changed_at}"

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.product_title}"

class Customer(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ProductInvoice(models.Model):
    PAYMENT_METHODS = [
        ('CREDIT_CARD', 'Credit Card'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('ESEWA', 'E-Sewa'),
        ('KHALTI', 'Khalti'),
        ('FONEPAY', 'Fonepay'),
        ('IMEPAY', 'IME Pay'),
        ('CASH', 'Cash'),
    ]
    invoice_number = models.IntegerField(null=False, blank=False)
    issued_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=False, blank=False)
    reference_number = models.CharField(max_length=200, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.FloatField(null=False, blank=False)
    vat_amount = models.FloatField(null=False, blank=False)
    pay_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, null=False, blank=False)
    payment_proof = models.FileField(upload_to='payment_proofs/', null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.customer.first_name} {self.customer.last_name}"

class ProductInvoiceItem(models.Model):
    invoice = models.ForeignKey(ProductInvoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    unit_price = models.FloatField(null=False, blank=False)
    total_price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f"Item {self.product.product_title} for Invoice {self.invoice.invoice_number}"

