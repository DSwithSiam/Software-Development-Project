# Generated by Django 4.2.6 on 2023-12-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_rename_addcard_addcardmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcardmodel',
            name='car_card_pk',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
