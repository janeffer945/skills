# Generated by Django 4.2.3 on 2023-08-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_contact_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(default='no description '),
        ),
    ]
