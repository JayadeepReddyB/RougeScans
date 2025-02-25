from django.urls import path
from .views import UserRegisterView, Login

urlpatterns = [
    path('register',UserRegisterView.as_view(), name = 'signup'),
    path('login', Login.as_view(), name = 'signin')
]