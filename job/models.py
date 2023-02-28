from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('job:opportunity_list_by_category', args=[self.slug])


class ActivatedManager(models.Manager):
    def get_queryset(self):
        return super(ActivatedManager, self).get_queryset().filter(status='activated')


n = 0


class Opportunity(models.Model):
    STATUS_CHOICES = (
        ('disable', 'Disabled'),
        ('activated', 'Activated')
    )

    STATUS_Hiring_Regime = (
        ('', ''),
        ('clt', 'CLT (Efetivo)'),
        ('pj', 'Pessoa Jurídica'),
        ('temporario', 'Temporario'),
        ('estagio', 'Estágio'),
        ('trainee', 'Trainne')
    )

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique_for_date='activate')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_opportunity')
    image = models.ImageField(upload_to=f'{n+1} - opportunity/%Y/%m/%d', blank=True)
    wage = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    activate = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='disable')
    hr = models.CharField(max_length=20, choices=STATUS_Hiring_Regime, default='')
    benefits = models.TextField(blank=True)

    objects = models.Manager()
    activated = ActivatedManager()

    tags = TaggableManager()

    class Meta:
        ordering = ('-activate',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job:opportunity_detail', args=[self.id, self.slug])


class Job_Registration(models.Model):
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='job_registrations')
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=11)
    curriculum = models.FileField(upload_to='pdfs/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return f'Application made by {self.name} for the position {self.opportunity}'


class Job_Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    favorites_opportunitys = models.ManyToManyField(Opportunity, blank=True, related_name='favorites_opportunitys')

    def __str__(self):
        return f'Perfil do usuário {self.user.username}'
