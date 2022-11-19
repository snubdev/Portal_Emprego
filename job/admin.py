from django.contrib import admin
from .models import Category, Opportunity, Job_Registration, Job_User


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'author',
                    'image', 'wage', 'description', 'activated',
                    'create', 'update', 'status', 'hr']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'activated'
    ordering = ['status', 'activated']


@admin.register(Job_Registration)
class Job_RegistrationAdmin(admin.ModelAdmin):
    list_display = ['opportunity', 'name', 'email', 'created', 'active']
    list_filter = ('active', 'created', 'updated')
    search_fields = ['opportunity']


@admin.register(Job_User)
class Job_UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth']