from django.urls import path
from .views.index import HomePageView
from .views.login import UserLoginView, logout_Us

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_Us, name='logout'),
]