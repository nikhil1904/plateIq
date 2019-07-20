from django.db import models
from django.contrib.postgres.fields import JSONField
from .validators import validate_file_extension
from django.contrib.auth.models import User
# Create your models here.


class IsDeletedManager(models.Manager):
    """
    Manager to filter/exclude is deleted field true.
    """

    def get_queryset(self):
        return super(IsDeletedManager, self).get_queryset().exclude(is_deleted=True)


class BaseModel(models.Model):
    """
    BaseModel is abstract base model that is used by other
    models to have general information to other models.

    :Note: This model is not created in the database.

    """
    # when the entry was created.
    created = models.DateTimeField(auto_now_add=True)
    # when the entry was modified.
    modified = models.DateTimeField(auto_now=True)
    # which user created the entry.
    created_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_created', null=True, blank=True, on_delete=models.CASCADE)
    # which user updated the entry.
    updated_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_updated', null=True, blank=True, on_delete=models.CASCADE)
    # is deleted is to keep the information of soft delete.
    is_deleted = models.BooleanField(default=False)
    objects = IsDeletedManager()

    class Meta:
        abstract = True


class Invoice(BaseModel):

    invoice_file = models.FileField(blank=False, null=False, validators=[validate_file_extension])
    name = models.CharField(max_length=32, null=True, blank=True)
    comment = models.CharField(max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.invoice_file.name
        super(Invoice, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class InvoiceState(BaseModel):
    Pending = 0
    Digitized = 1
    Declined = 2

    STATE_CHOICES = ((Pending, 'Pending'),
                     (Digitized, 'Digitized'),
                     (Declined, 'Declined'))
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=STATE_CHOICES, default=0)

    def __str__(self):
        return str(self.invoice)


class InvoiceSummary(BaseModel):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=32, null=True, blank=True)
    invoice_from = models.CharField(max_length=256, null=True, blank=True)
    invoice_to = models.CharField(max_length=256, null=True, blank=True)
    issue_date = models.DateField(null=True,blank=True)
    due_date = models.DateField(null=True, blank=True)
    subtotal = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    amount_due = models.DecimalField(max_digits=16, decimal_places=2, null=True, blank=True)
    items = JSONField(default=dict, null=True)

    def __str__(self):
        return str(self.invoice)

