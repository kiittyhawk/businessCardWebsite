from django.urls import path
from .views.detail import PostDetailView
from .views.index import HomePageView
from .views.register import UserRegisterView, logout_Us
from .views.login import UserLoginView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', logout_Us, name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('<slug:pk>/', PostDetailView.as_view(), name='articles_detail'),
]