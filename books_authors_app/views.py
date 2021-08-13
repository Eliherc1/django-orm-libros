from django.shortcuts import render, redirect
from .models import *

def book(request):
    contexto={
        'libros' : Book.objects.all(),
    }
    return render(request, 'add_libros.html', contexto)


def procesar_book(request):
    print(request.POST)

    libro = Book.objects.create(
        title  = request.POST['book_title'],
        description  = request.POST['book_desc'],
        
    )

    return redirect("/")

def author(request):
    contexto={
        'autores' : Author.objects.all(),
    }
    return render(request, 'add_autores.html', contexto)

def procesar_autor(request):
    print(request.POST)

    autor = Author.objects.create(
        first_name  = request.POST['author_nombre'],
        last_name  = request.POST['author_apellido'],
        notas  = request.POST['author_notas'],
    )

    return redirect("/authors")

def ver_libro(request,num):
    autores= Book.objects.get(id=num).authors.all()
    libro= Book.objects.get(id=num)
    contexto={ 'libros': libro ,
                'autores': autores ,
                #'authors': Author.objects.all() ,
                'aut': Author.objects.exclude(id__in=autores.values_list('id',flat=True)) ,
            }
    return render(request, 'ver_libro.html', contexto)



def ver_autor(request,num):
    libros= Author.objects.get(id=num).books.all()
    autor= Author.objects.get(id=num)
    contexto={ 'autores': autor ,
                'libros': libros ,
                #'books': Book.objects.all() ,
                'lib': Book.objects.exclude(id__in=libros.values_list('id', flat=True))
              
            }
    return render(request, 'ver_autor.html', contexto)

def asociar_libro(request , id_autor):
    print(request.POST)
    id_libro = request.POST['libro_a']
    libro = Book.objects.get(id=id_libro)
    autor = Author.objects.get(id=id_autor)

    libro.authors.add(autor)
    return redirect(f"/authors/{id_autor}")

def asociar_autor(request , id_libro):
    print(request.POST)
    id_autor = request.POST['autor_l']
    autor = Author.objects.get(id=id_autor)
    libro = Book.objects.get(id=id_libro)

    autor.books.add(libro)
    return redirect(f"/books/{id_libro}")

def eliminar_libro(request, lib):
    libro_objeto = Book.objects.get(id=lib)
    print("-"*20, libro_objeto)
    libro_objeto.delete()

    return redirect("/")

def eliminar_autor(request, aut):
    autor_objeto = Author.objects.get(id=aut)
    print("-"*20, autor_objeto)
    autor_objeto.delete()

    return redirect("/authors")