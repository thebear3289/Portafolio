# web/models.py
import uuid
from django.db import models

class Flan(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    is_private = models.BooleanField(default=False, null=True, blank=True)
    nuevo_atributo = models.CharField(max_length=50, null=True, blank=True)  # Atributo adicional

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.customer_name}"
