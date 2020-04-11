from django.urls import path
from accounts import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('register/step1' ,views.register ,name="Register"),
    path('register/step2', views.first, name="Register1"),
    path('login/' ,views.loginuser ,name="Login"),
    path('logout' ,views.logout_view ,name="Logout"),
    path('dashboar/', views.dashbord, name='Dashbord'),
    path('profile/',views.profile_view,name="profile"),
    path('change-password', views.change_password, name="change_password"),
    path('viewprofile', views.viewp_rofile, name="viewprofile"),
    path('reset-password', PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),
    path('reset-password/done', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password/complete/',
    PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),
]