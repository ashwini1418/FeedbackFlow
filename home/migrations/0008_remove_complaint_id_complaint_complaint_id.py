# Generated by Django 5.0.7 on 2024-11-23 14:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_complaint_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='id',
        ),
        migrations.AddField(
            model_name='complaint',
            name='complaint_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
