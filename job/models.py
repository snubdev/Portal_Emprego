from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Opportunity(models.Model):
    STATUS_CHOICES = (
        ('disable', 'Disabled'),
        ('activated', 'Activated')
    )

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique_for_date='activated')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_opportunity')
    image = models.ImageField(upload_to='opportunity/%Y/%m/%d', blank=True)
    wage = models.DecimalField(max_digits=5, decimal_places=True)
    description = models.TextField(blank=True)
    activated = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='disable')

    class Meta:
        ordering = ('-activated',)

    def __str__(self):
        return self.title



