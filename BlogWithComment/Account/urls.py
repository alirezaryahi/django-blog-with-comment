from django.urls import path
from .views import Login, register, Logout

urlpatterns = [
    path('login', Login),
    path('register', register),
    path('logout', Logout)
]
