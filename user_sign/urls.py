from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserView

app_name = 'user_sign'

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('log-in/', LoginView.as_view()),
    path('user-view/', UserView.as_view()),
    path('log-out/', LogoutView.as_view()),
]