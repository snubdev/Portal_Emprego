from django import forms
from .models import Category, Opportunity


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = {'name', 'slug'}


class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = {'category', 'title', 'slug', 'author',
                  'image', 'wage', 'description', 'activated', 'status'}
