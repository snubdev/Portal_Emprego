from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'job'

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.teste, name='teste'),

    # urls para alteração de senha
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # urls para reiniciar a senha
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # urls para registro de usuário
    path('register/', views.register, name='register'),

    # urls para editar perfil do usuário
    path('edit/', views.edit, name='edit'),

    path('list', views.opportunity_list, name='opportunity_list'),
    path('search/', views.job_search, name='job_search'),
    path('<slug:category_slug>/', views.opportunity_list, name='opportunity_list_by_category'),
    path('<int:id>/<slug:slug>/', views.opportunity_detail, name='opportunity_detail'),
    path('tag/<slug:tag_slug>/', views.opportunity_list, name='opportunity_list_by_tag'),






]
