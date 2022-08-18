from django.contrib import admin
from .models import Category, Opportunity


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'author',
                    'image', 'wage', 'description', 'activated',
                    'create', 'update', 'status']
    list_display = ['category', 'title', 'activated']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'activated'
    ordering = ['status', 'activated']

