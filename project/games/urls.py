from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path("liste/", views.liste),
    path("delete/<int:id>/", views.delete),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("updatetraitement/<int:id>/", views.updatetraitement),
]
