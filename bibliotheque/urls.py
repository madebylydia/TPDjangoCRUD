from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_creation_livre),
    path('all/', views.front_all_livres),
    path('update/<int:id>/', views.front_update_livre),

    path('<int:id>/', views.crud_livre_read),
    path('api/', views.crud_livre_create),
    path('api/<int:id>/', views.crud_livre_read),
    path('api/update/<int:id>/', views.crud_livre_update),
    path('api/delete/<int:id>/', views.crud_livre_delete),
]
