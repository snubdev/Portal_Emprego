from django.shortcuts import render, get_object_or_404
from .models import Category, Opportunity


def opportunity_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    opportunitys = Opportunity.objects.filter(status='activated')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        opportunitys = opportunitys.filter(category=category)
    return render(request, 'job/list.html', {'category': category,
                                                     'categories': categories,
                                                     'opportunitys': opportunitys})

def opportunity_detail(request, id, slug):
    opportunity = get_object_or_404(Opportunity, id=id, slug=slug, status='activated')

    return render(request, 'job/detail.html', {'opportunity': opportunity})
