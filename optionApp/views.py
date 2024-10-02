from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def vistaTabla(request):
    titulo = "<h1><u>Países Favoritos</u></h1>"
    detalle = """
                <style>
                    th, td {
                        border: 1px solid black;
                        padding: 10px;
                        text-align: center;
                    }
                    
                    #encabezado {
                        background-color: gray;
                        color: mintcream;
                    }
                    
                    #fila {
                        background-color: mintcream;
                    }
                </style>
    
                <h2>Estos son mis países favoritos:</h2>
                <table>
                    <tr id='encabezado'>
                        <th>País</th>
                        <th>Continente</th>
                        <th>Bandera</th>
                    </tr>
                    <tr id='fila'>
                        <td>Chile</td>
                        <td>Sudamérica</td>
                        <td><img src='https://upload.wikimedia.org/wikipedia/commons/7/78/Flag_of_Chile.svg' width='150' height='100'></td>
                    </tr>
                    <tr id='fila'>
                        <td>China</td>
                        <td>Asia</td>
                        <td><img src='https://upload.wikimedia.org/wikipedia/commons/f/fa/Flag_of_the_People%27s_Republic_of_China.svg' width='150' height='100'></td>
                    </tr>
                    <tr id='fila'>
                        <td>Nueva Zelanda</td>
                        <td>Oceanía</td>
                        <td><img src='https://upload.wikimedia.org/wikipedia/commons/3/3e/Flag_of_New_Zealand.svg' width='150' height='100'></td>
                    </tr>
                </table>
                <br>
            """
    volver = "<a href='/'><h3>Volver</h3></a>"
    pagina = titulo + detalle + volver
    return HttpResponse(pagina)

def vistaLoteria(request):
    titulo = "<h1><u>Lotería</u></h1>"
    detalle = "<h2>Estos son los números de la suerte en este momento:</h2>"
    
    numeros_loteria = random.sample(range(1,101),10) #elije 10 números aleatorios entre 1 y 100, y los deja en una lista
    numeros_loteria.sort() #ordena los números de menor a mayor
    numeros_loteria = str(numeros_loteria) #convierte los númros a texto
    numeros_loteria = numeros_loteria.replace(',','][') #cambia las comas por []
    
    volver = "<a href='/'><h3>Volver</h3></a>"
    pagina = titulo + detalle + numeros_loteria + volver
    return HttpResponse(pagina)
