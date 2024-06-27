from django.urls import path

from .views import api_view
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('save/', views.save_data, name='save_data'),
    path('count/', views.get_count, name='get_count'),
    path('api/data/<int:pk>/', api_view, name='api_view'),
]