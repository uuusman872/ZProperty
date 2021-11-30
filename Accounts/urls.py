from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_user, name="login"),
    path("register", views.register_user, name="register"),
    # path('forgetpassword', views.forget_password, name='forgetpassword'),
    # path('resetPasswordValidation/<uidb64>/<token>', views.reset_password_validator, name='resetPasswordValidation'),
    # path('resetPassword', views.resetPassword, name='resetPassword'),
    path("logout", views.logout_user, name="logout"),
]
