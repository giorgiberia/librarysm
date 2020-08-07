from django.contrib import admin
from catalog import models

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author','status','takenBy')
    ordering = ('name',)
    search_fields = ('name', 'takenBy')


admin.site.register(models.Book,BookAdmin)


admin.site.register(models.Author)