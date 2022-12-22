from django.contrib import admin
from .models import Category, Opportunity, Job_Registration, Job_Profile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'author',
                    'image', 'wage', 'description', 'activate',
                    'create', 'update', 'status', 'hr']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'activate'
    ordering = ['status', 'activate']


@admin.register(Job_Registration)
class Job_RegistrationAdmin(admin.ModelAdmin):
    list_display = ['opportunity', 'name', 'email', 'created', 'active']
    list_filter = ('active', 'created', 'updated')
    search_fields = ['opportunity']


@admin.register(Job_Profile)
class Job_ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth']