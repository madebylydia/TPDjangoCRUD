from django.urls import path

from . import views

urlpatterns = [
    path("", views.bibliotheque),
    # Livres
    path("livre/", views.bibliotheque_livre),
    path("livre/all/", views.bibliotheque_livre_all),
    path("livre/<int:id>/", views.bibliotheque_livreId),
    path('livre/fromcategorie/<int:id>/', views.bibliotheque_livre_from_categorie),
    path("livre/update/<int:id>/", views.bibliotheque_livre_updateId),
    # Livres : API
    path("api/livre/", views.bibliotheque_api_livre),
    path("api/livre/fromcategorie/<int:id>/", views.bibliotheque_api_livre_fromcategorieId),
    path("api/livre/update/<int:id>/", views.bibliotheque_api_livre_updateId),
    path("api/livre/delete/<int:id>/", views.bibliotheque_api_livre_deleteId),
    
    # Catégories
    path("categorie/", views.bibliotheque_categorie),
    path("categorie/all", views.bibliotheque_categorie_all),
    path("categorie/<int:id>/", views.bibliotheque_categorieId),
    path("categorie/update/<int:id>/", views.bibliotheque_categorie_updateId),
    # Catégories : API
    path("api/categorie/", views.bibliotheque_api_categorie),
    path("api/categorie/update/<int:id>/", views.bibliotheque_api_categorie_updateId),
    path("api/categorie/delete/<int:id>/", views.bibliotheque_api_categorie_deleteId),
]
