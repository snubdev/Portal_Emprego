from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'job'

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.teste, name='teste'),
    path('list/', views.opportunity_list, name='opportunity_list'),
    path('search/', views.job_search, name='job_search'),
    path('<slug:category_slug>/', views.opportunity_list, name='opportunity_list_by_category'),
    path('<int:id>/<slug:slug>/', views.opportunity_detail, name='opportunity_detail'),

]
