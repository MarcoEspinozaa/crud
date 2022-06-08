import os
import time
import django

# Código que se agrega para ocupar el archivo dentro de cualquier carpeta que no sea la raiz #

#import sys
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE','proyecto_m7.settings')
django.setup()

from m7_python.models import Inmuebles,Region

def get_list_inmuebles(name,descr):
    lista_inmuebles = Inmuebles.objects.filter(nombre_inmueble__contains = name).filter(descripcion__contains = descr)

    archi1 = open("datos.txt","w")
    for item in lista_inmuebles.values():
        archi1.write('=== Prueba de primer método ===\n')
        archi1.write(str(item))
        archi1.write("\n")
    archi1.close()

    return lista_inmuebles

resultado = get_list_inmuebles('Providencia','Cocina')


def get_list_inmuebles_by_comuna(comuna):
    select = f"""
    SELECT A.id, A.nombre_inmueble, A.descripcion
    FROM public.m7_python_inmuebles as A
    INNER JOIN public.m7_python_region as B
    ON A.id_region_id = B.id
    INNER JOIN public.m7_python_comuna as C
    ON A.id_comuna_id = C.id
    WHERE C.comuna LIKE '%%{str(comuna)}%%' 
    """

    results = Inmuebles.objects.raw(select)

    archi1 = open("datos.txt","a")
    for item in results:
        archi1.write("\n")
        archi1.write('=== Prueba de segundo método ===\n')
        archi1.write(f'Título: {item.nombre_inmueble}\nDescripción: {item.descripcion}')
        archi1.write("\n")
    archi1.close()

get_list_inmuebles_by_comuna("Bernardo")


def get_list_inmuebles_region(id):
    region = str(Region.objects.filter(id=id).values()[0]["region"])

    lista_inmuebles = Inmuebles.objects.filter(id_region_id = id)

    archi1 = open("datos.txt","a")
    archi1.write("\n")
    archi1.write('=== Prueba de tercer método ===\n')
    for item in lista_inmuebles.values():
        archi1.write(f'Region: {region}\n')
        archi1.write(f'Título: {str(item["nombre_inmueble"])}\n')
        archi1.write("\n")
    archi1.close()

get_list_inmuebles_region(16)


def get_list_inmuebles_by_region(region):
    select = f"""
    SELECT A.id, A.nombre_inmueble, A.descripcion
    FROM public.m7_python_inmuebles as A
    INNER JOIN public.m7_python_region as B
    ON A.id_region_id = B.id
    INNER JOIN public.m7_python_comuna as C
    ON A.id_comuna_id = C.id
    WHERE B."region" LIKE '%%{str(region)}%%'
    """
    results = Inmuebles.objects.raw(select)

    archi1 = open("datos.txt","a")
    archi1.write("\n")
    archi1.write('=== Prueba de cuarto método ===\n')
    for item in results:
        archi1.write(f'Título: {item.nombre_inmueble}\nDescripción: {item.descripcion}\n')
        archi1.write("\n")
    archi1.close()

get_list_inmuebles_by_region("Metrop")