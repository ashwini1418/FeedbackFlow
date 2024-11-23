# Generated by Django 5.0.7 on 2024-11-23 13:56

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_complaint_timestamp'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='email',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='feedback_id',
        ),
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Pending', max_length=50),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='category',
            field=models.CharField(choices=[('Hostel', 'Hostel'), ('Academic', 'Academic')], max_length=50),
        ),
    ]
