from django.contrib import admin

from .models import (
    Hall, Review
)


admin.site.register(
    [Hall, Review]
)