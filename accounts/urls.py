from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . views import home
from .views import save_field_order
from django.urls import path
from .views import delete_employee

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change-password/', views.change_password, name='change_password'),
    
    # Corrected form route - only one correct definition
    path('form-builder/', views.form_builder, name='form_builder'), 
    path('save-form/', views.save_form, name='save_form'),

    path('profile/', views.profile, name='profile'),
    path('save-field-order/', save_field_order, name='save_field_order'),
    path('home/', home, name='home'),
    path('accounts/profile-setup/', views.profile_setup, name='profile-setup'), 
    path('create_employee/', views.create_employee, name='create_employee'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path("delete_employee/<int:employee_id>/", delete_employee, name="delete_employee"),


    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
