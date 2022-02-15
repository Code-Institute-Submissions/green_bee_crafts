from django.contrib import admin
from .models import Market


# Register your models here.
class MarketAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'when',
        'where',
        'cost',
        'image',
    )

    ordering = ('name',)


admin.site.register(Market)
