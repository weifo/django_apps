from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trans/<request_id>',views.test,name='test')
]