# Generated by Django 4.2.1 on 2023-06-02 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yummy_app', '0004_alter_producer_rating_alter_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producer',
            name='rating',
        ),
    ]