# Generated by Django 5.0.7 on 2024-11-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_complaint_email_remove_complaint_feedback_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]