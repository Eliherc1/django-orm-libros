from django.urls import path
from . import views


urlpatterns = [
    path('', views.book),
    path('procesar_libro', views.procesar_book),
    path('authors/', views.author),
    path('authors/procesar_autor', views.procesar_autor),
    path('books/<int:num>', views.ver_libro),
    path('authors/<int:num>', views.ver_autor),
    path('eliminar_libro/<int:lib>', views.eliminar_libro),
    path('eliminar_autor/<int:aut>', views.eliminar_autor),
    path('asociar_libro/<int:id_autor>', views.asociar_libro),
    path('asociar_autor/<int:id_libro>', views.asociar_autor),
]
