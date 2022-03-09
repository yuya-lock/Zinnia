from django.contrib import admin

from .models import (
    Hall, Review, Rating
)


admin.site.register(
    [Hall, Review, Rating]
)