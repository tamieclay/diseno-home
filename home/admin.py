from django.contrib import admin

from home.models import FeaturedProducts, MainProducts

# Register your models here.
admin.site.register(MainProducts)

admin.site.register(FeaturedProducts)