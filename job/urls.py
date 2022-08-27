from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('category/', views.category, name='category'),
    path('opportunity/', views.opportunity, name='opportunity')

]