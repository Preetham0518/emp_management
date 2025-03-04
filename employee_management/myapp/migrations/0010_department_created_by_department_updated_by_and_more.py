# Generated by Django 5.1.4 on 2025-01-06 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_department_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='designation',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='designation',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='location',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='location',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='skill',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='skill',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
