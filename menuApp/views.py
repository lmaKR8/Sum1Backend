from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vistaMenu(request):
    titulo = "<h1><u>Menu Principal</u></h1>"
    detalle = """
                <h2>Elije una de las siguientes opciones:</h2>
                <ul>
                    <li><a href='tabla/'><h3>Países Favoritos</h3></a></li>
                    <li><a href='loteria/'><h3>Lotería</h3></a></li>
                </ul>
            """
    pagina = titulo + detalle
    return HttpResponse(pagina)