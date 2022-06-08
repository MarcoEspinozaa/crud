from m7_python.models import *

#Create
def insertar_inmuebles(data):
    id_user = data[0]
    id_tipo_inmueble = data[1]
    id_comuna = data[2]
    id_region = data[3]
    nombre_inmueble = data[4]
    descripcion = data[5]
    m2_contruido = data[6]
    m2_terreno = data[7]
    numero_estacionamientos = data[8]
    numero_banos = data[9]
    numero_hab = data[10]
    direccion = data[11]
    precio_mensual = data[12]

    inm = Inmuebles(
        id_user = id_user,
        id_tipo_inmueble = id_tipo_inmueble,
        id_comuna = id_comuna,
        id_region = id_region,
        nombre_inmueble = nombre_inmueble,
        descripcion = descripcion,
        m2_contruido = m2_contruido,
        m2_terreno = m2_terreno,
        numero_estacionamientos = numero_estacionamientos,
        numero_banos = numero_banos,
        numero_hab = numero_hab,
        direccion = direccion,
        precio_mensual = precio_mensual)

    inm.save()

#Read
def get_all_inmuebles():
    inm = Inmuebles.objects.all()
    return inm

#Update
def actualizar_descripcion_inmueble(id_inmueble, new_descripcion):
    Inmuebles.objects.filter(pk = id_inmueble).update(descripcion = new_descripcion)

#Delete
def eliminar_inmueble(id_inmueble):
    Inmuebles.objects.get(id = id_inmueble).delete()

