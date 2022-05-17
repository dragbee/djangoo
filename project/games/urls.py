from django.urls import path
from . import views

urlpatterns = [

    #Games
    path('index/', views.index),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path("liste/", views.liste),
    path("delete/<int:id>/", views.delete),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("updatetraitement/<int:id>/", views.updatetraitement),

    #Categories
    path('ajout2/', views.ajout2),
    path('traitement2/', views.traitement2),
    path("liste2/", views.liste2),
    path("affiche2/<int:id>/", views.affiche2),
    path("delete2/<int:id>/", views.delete2),
    path("update2/<int:id>/", views.update2),
    path("updatetraitement2/<int:id>/", views.updatetraitement2),

]
