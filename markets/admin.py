from django.contrib import admin
from .models import Markets

# Register your models here.
class MarketsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        
    )

    ordering = ('name',)

admin.site.register(Markets, MarketsAdmin)
