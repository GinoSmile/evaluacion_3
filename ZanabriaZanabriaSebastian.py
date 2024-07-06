def Procesar_lista_de_estudiantes():
    import csv
    alumnos=[]
    with open('ListaCurso5B.csv','r',newline="") as archivo:
        leer=csv.DictReader(archivo)
        for elements in leer:
            rut=elements['Rut']
            nombre=elements['Nombre']
            nota1=elements['Nota 1']
            nota2=elements['Nota 2']
            alumnos.append({'rut':rut,
                            'nombre':nombre,
                            'nota 1':nota1,
                            'nota 2':nota2
                            })
        return(alumnos)
    
def Registrar_estudiante():
    alumnos=[]
    rut=input("Ingrese el rut del estudiante:\n")
    nombre=input("Ingrese el nombre y apellido del estudiante:\n")
    nota1=float(input("Ingrese la primera nota\n"))
    nota2=float(input("Ingrese la segunda nota:\n"))
    alumnos ={'rut':rut,'nombre':nombre,'nota 1':nota1,'nota 2':nota2}
    print("Se ha registrado al alumno con exito")
    return(alumnos)
    

def Modificar_nota():
    modificar=input("Ingrese el rut del estudiante:\n")
    for rut in lista:
        if modificar==rut['rut']:
            new_nota=int(input("Desea modificar la nota 1 o la nota 2?\n"))
            if new_nota==1:
                nueva_nota1=float(input("Ingrese la nuvea nota 1:\n"))
                rut['nota 1']=nueva_nota1
            elif new_nota==2:
                nueva_nota2=float(input("Ingrese la nuvea nota 1:\n"))
                rut['nota 2']=nueva_nota2
            else:
                print("ingrese una opcion valida")
        print(rut['nombre'],rut['nota 1'],rut['nota 2'])


def Eliminar_estudiante():
    rut=input("Ingrese el rut del estudiante que desea eliminar:\n")
    for i in lista:
        if rut==i['rut']:
            print("esta seguro que desea eliminar a ",i['nombre'],"?(si/no)")
            respuesta=input("").lower()
            if respuesta=="si":
                lista.remove(i)

def Generar_promedio_de_notas():
    pass

def Generar_acta_de_cierre_de_curso():
    pass

def Salir():
    pass
lista=[]
while True:
    print("Buen dia profesor, que desea hacer hoy?")
    op=int(input("1.-Procesar lista de estudiantes.\n2.-Registrar estudiante.\n3.-Modificar nota.\n4.-Eliminar estudiante.\n5.-Generar promedio de notas.\n6.-Generar acta de cierre de curso.\n7.-Salir.\n"))
    if op==1:
        list_estudents=Procesar_lista_de_estudiantes()
        if list_estudents!=None:
            lista = list_estudents
    if op==2:
        registrar=Registrar_estudiante()
        lista.append(registrar)
    if op==3:
        Modificar_nota()
    if op==4:
        pass
    if op==5:
        pass
    if op==6:
        pass
    if op==7:
        pass