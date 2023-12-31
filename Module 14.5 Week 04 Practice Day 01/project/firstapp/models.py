from django.db import models

class MyModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    time_field = models.TimeField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    integer_field = models.IntegerField()
    float_field = models.FloatField()
    json_field = models.JSONField()
    generic_ip_address_field = models.GenericIPAddressField()
    image_field = models.ImageField(upload_to='images/')
    ositive_small_integer_field = models.PositiveSmallIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    slug_field = models.SlugField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()