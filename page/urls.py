from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_list_views, name='PageList'),
    path('about/', views.about_us_views, name='About'),
    path('contact/', views.contact_us_views, name='Contact'),
]