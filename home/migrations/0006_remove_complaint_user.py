# Generated by Django 5.0.7 on 2024-11-23 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_complaint_category_alter_complaint_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='user',
        ),
    ]
