from django.shortcuts import render, get_object_or_404
from .models import Category, Opportunity, Job_Registration, Job_Profile
from .forms import Job_RegistraionForm, SearchForm, LoginForm, UserRegistrationForm, UserEditForm, Job_ProfileEditForm
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


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
    results = ()

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Opportunity.objects.annotate(search=SearchVector('title'),).filter(search=query)
    return render(request, 'job/search.html', {'form': form,
                                               'query': query,
                                               'results': results})


# views de login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')

                else:
                    return HttpResponse('Disable My Job')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'job/login.html', {'form': form})


@login_required
def teste(request):
    return render(request, 'job/teste.html', {'section': teste})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Job_Profile.objects.create(user=new_user)
            return render(request, 'job/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'job/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        job_user_form = Job_ProfileEditForm(instance=request.user.job_user, data=request.POST)

        if user_form.is_valid() and job_user_form.is_valid():
            user_form.save()
            job_user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        job_user_form = Job_ProfileEditForm(instance=request.user.job_user)

    return render(request, 'job/edit.html', {'user_form': user_form, 'job_user_form': job_user_form})