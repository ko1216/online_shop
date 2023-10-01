from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, verify_email, verification_failed, CustomLoginView

app_name = UsersConfig.name


urlpatterns = [
    path('', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/<str:uidb64>/<str:token>/', verify_email, name='verify_email'),
    path('verification_failed/', verification_failed, name='verification_failed'),
]
