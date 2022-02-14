import django
from django.conf import Settings
from Awwwards import views
from django.urls import path
from django.conf.urls.static import static
from Core import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('register', views.Register, name="Register"),
    path('login', views.Login, name="Login"),
    path('logout', views.Logout, name="Logout"),
    path('activateuser/<uidb64>/<token>',views.ActivateAccount, name = 'ActivateAccount'),
    path('resetpassword/',auth_views.PasswordResetView.as_view(template_name='ResetPassword.html'), name = 'reset_password'),
    path('resetpassword/sent/',auth_views.PasswordResetDoneView.as_view(template_name='PasswordResetSent.html'), name = 'password_reset_done'),
    path('resetpassword/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='PasswordResetConfirm.html'), name = 'password_reset_confirm'),
    path('resetpassword/success/',auth_views.PasswordResetCompleteView.as_view(template_name='PasswordResetSuccess.html'), name = 'password_reset_complete'),
    path('portfolio/add', views.AddPortfolio, name="AddPortfolio"),
    path('profile/<str:username>/edit', views.EditProfile, name="EditProfile"),
    path('profile/<str:username>/portfolio/<str:title>/edit', views.EditPortfolio, name="EditPortfolio"),
    path('profile/<str:username>/settings', views.Settings, name="Settings"),
    path('profile/<str:username>/profile', views.MyProfile, name="MyProfile"),
    path('profile/<str:username>/portfolio', views.MyPortfolio, name="MyPortfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
