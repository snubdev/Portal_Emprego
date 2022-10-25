from django.shortcuts import render, get_object_or_404
from .models import Category, Opportunity, Job_Registration
from .forms import Job_RegistraionForm, SearchForm
from django.contrib.postgres.search import SearchVector


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

    job_registrations = opportunity.job_registrations.filter(active=True)
    new_registraion = None

    if request.method == 'POST':
        registraion_form = Job_RegistraionForm(request.POST, request.FILES)
        if registraion_form.is_valid():
            new_registraion = registraion_form.save(commit=False)
            new_registraion.opportunity = opportunity
            new_registraion.save()
    else:
        registraion_form = Job_RegistraionForm()

    return render(request, 'job/detail.html', {'job_registrations': job_registrations,
                                               'opportunity': opportunity,
                                               'new_registraion': new_registraion,
                                               'registraion_form': registraion_form})

def job_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Opportunity.published.annotate(search=SearchVector('title'),).filter(search=query)
    return render(request, 'job/search.html', {'form': form,
                                               'query': query,
                                               'results': results})
