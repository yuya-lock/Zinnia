from django.db import models

from accounts.models import User


class Hall(models.Model):
    name = models.CharField(max_length=255)
    picture = models.FileField(null=True, upload_to='hall_picture/')
    info = models.CharField(max_length=1000, null=True)
    industry_type = models.CharField(max_length=255)
    business_hours = models.CharField(max_length=255, null=True)
    capacity = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=32)
    website = models.URLField(null=True)
    prefecture = models.CharField(max_length=32)
    region = models.CharField(max_length=32)
    buss = models.CharField(max_length=255, null=True)
    train = models.CharField(max_length=255, null=True)
    is_able = models.BooleanField(default=True)

    class Meta:
        db_table = 'halls'

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=1000, null=True)
    rate = models.PositiveIntegerField(null=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    hall = models.ForeignKey(
        Hall, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return self.title
