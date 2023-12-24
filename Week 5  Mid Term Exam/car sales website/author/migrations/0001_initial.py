# Generated by Django 4.2.6 on 2023-12-24 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image', models.ImageField(upload_to='car/', verbose_name='image')),
                ('car_name', models.CharField(max_length=30)),
                ('car_price', models.IntegerField(default=0)),
                ('car_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('car_decription', models.CharField(blank=True, max_length=200, null=True)),
                ('car_brand', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
