from django.contrib import admin
from .models import Books, Authors

# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ["name", "author", "isbn"]

admin.site.register(Books,BooksAdmin)
admin.site.register(Authors)


