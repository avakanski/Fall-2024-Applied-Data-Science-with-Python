from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('predict/', views.predict_class, name='predict'),
] 