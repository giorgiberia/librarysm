from django.contrib import admin
from catalog import models

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    fields = ('name', 'author', 'status', 'takenBy', 'taken_at')
    list_display = ('name', 'author','status','takenBy','taken_at')
    ordering = ('name',)
    search_fields = ('name', 'takenBy')

admin.site.register(models.Book,BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


admin.site.register(models.Author)
