from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('rout',views.routing),
    path('pyt', views.pyth),
    path('pytex',views.pythonex),
]