from django.shortcuts import render, get_object_or_404
from .models import Category, Opportunity
from .forms import CategoryForm, OpportunityForm


def category(request):
    text = False
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            text = True
    else:
        category_form = CategoryForm()

    return render(request, 'job/category.html', {'category_form': category_form, 'text': text})


def opportunity(request):
    text = False
    if request.method == 'POST':
        opportunity_form = OpportunityForm(request.POST)
        if opportunity_form.is_valid():
            opportunity_form.save()
            text = True
    else:
        opportunity_form = OpportunityForm

    return render(request, 'job/opportunity.html', {'opportunity_form': opportunity_form, 'text': text})