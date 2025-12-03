from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)} # put a comma if a tuple has a single item
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
