from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('', views.opportunity_list, name='opportunity_list'),
    path('<slug:category_slug>/', views.opportunity_list, name='opportunity_list_by_category'),
    path('<int:id>/<slug:slug>/', views.opportunity_detail, name='opportunity_detail'),
    path('search/', views.job_search, name='job_search'),
]