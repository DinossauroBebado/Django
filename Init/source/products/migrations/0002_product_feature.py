# Generated by Django 4.0.2 on 2022-02-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
