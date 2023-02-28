from _ast import arguments

from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Category, Opportunity, Job_Registration, Job_Profile
from .forms import Job_RegistraionForm, SearchForm, LoginForm, UserRegistrationForm, UserEditForm, Job_ProfileEditForm
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.db.models import Count

def opportunity_list(request, category_slug=None, tag_slug=None):
    category = None
    categories = Category.objects.all()
    opportunitys = Opportunity.objects.filter(status='activated')

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        opportunitys = opportunitys.filter(tags__in=[tag])

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        opportunitys = opportunitys.filter(category=category)
    return render(request, 'job/list.html', {'category': category,
                                                     'categories': categories,
                                                     'opportunitys': opportunitys,
                                                     'tag': tag})


def opportunity_detail(request, id, slug):
    opportunity = get_object_or_404(Opportunity, id=id, slug=slug, status='activated')
    opportunity_add = get_object_or_404(Opportunity, id=id)


    # Registro de úsuario
    job_registrations = opportunity.job_registrations.filter(active=True)
    new_registraion = None
    cont = None

    # Postagem semelhantes
    opportunity_tags_ids = opportunity.tags.values_list('id', flat=True)
    similar_opportunity = Opportunity.activated.filter(tags__in=opportunity_tags_ids).exclude(id=opportunity.id)
    similar_opportunity = similar_opportunity.annotate(same_tags=Count('tags')).order_by('-same_tags', '-activate')[:4]

    if request.method == 'POST':
        registraion_form = Job_RegistraionForm(request.POST, request.FILES)

        form = Job_RegistraionForm(request.POST)

        nome = form.data['name']
        print(nome)
        nomes = Job_Registration.objects.filter(name=nome)


        '''if len(nomes) > 0:
            registraion_form = Job_RegistraionForm()'''

        if registraion_form.is_valid():
            new_registraion = registraion_form.save(commit=False)
            new_registraion.opportunity = opportunity
            oportunidade = Job_Registration.objects.filter(opportunity=new_registraion.opportunity)
            if len(nomes) > 0 and len(oportunidade) > 0:
                cont = 1
            else:
                new_registraion.save()
                cont = 0
    else:
        registraion_form = Job_RegistraionForm()

    return render(request, 'job/detail.html', {'job_registrations': job_registrations,
                                               'opportunity': opportunity,
                                               'new_registraion': new_registraion,
                                               'registraion_form': registraion_form,
                                               'similar_opportunity': similar_opportunity,
                                               'cont': cont, 'opportunity_add':opportunity_add},)


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
        job_user_form = Job_ProfileEditForm(instance=request.user)

    return render(request, 'job/edit.html', {'user_form': user_form, 'job_user_form': job_user_form})

@login_required
def	favorite_job(request, id):
    opportunity_add = get_object_or_404(Opportunity, id=id)
    if opportunity_add.favorites_opportunitys.filter(id=request.user.id).exists():
        opportunity_add.favorites_opportunitys.remove(request.user)
    else:
        opportunity_add.favorites_opportunitys.add(request.user)
        print(opportunity_add)
        opportunity_add.save()
    return HttpResponseRedirect(request.META['Teste'])

'''def	favorite_job(request, id, slug):
    opportunity_add = get_object_or_404(Opportunity, id=id, slug=slug, status='activated')
    profile = Job_Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        profile.favorites_opportunitys.add(opportunity_add.user)
        print(opportunity_add)
        profile.save()
    return render(request, 'job/%s' % id)'''

