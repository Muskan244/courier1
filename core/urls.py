from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'), # url for the homepage
    path('index/', views.index, name='index'), #url for the signup page
    path('admin/', views.sign_in, name='sign_in'), # url for the signin page
]