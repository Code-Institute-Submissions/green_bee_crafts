from django.contrib import admin
from .models import Upcycle


# Register your models here.
class UpcycleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'information',
        'author',
        'image',
    )

    ordering = ('name',)


admin.site.register(Upcycle)
