# Generated by Django 2.2.3 on 2019-07-20 08:10

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import invoice.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('invoice_file', models.FileField(upload_to='', validators=[invoice.validators.validate_file_extension])),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('comment', models.CharField(blank=True, max_length=256, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_invoice_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_invoice_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvoiceSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('invoice_number', models.CharField(blank=True, max_length=32, null=True)),
                ('invoice_from', models.CharField(blank=True, max_length=256, null=True)),
                ('invoice_to', models.CharField(blank=True, max_length=256, null=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('amount_due', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('items', django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_invoicesummary_created', to=settings.AUTH_USER_MODEL)),
                ('invoice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invoice.Invoice')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_invoicesummary_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvoiceState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('state', models.IntegerField(choices=[(0, 'Pending'), (1, 'Digitized'), (2, 'Declined')], default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_invoicestate_created', to=settings.AUTH_USER_MODEL)),
                ('invoice', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.Invoice')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_invoicestate_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
