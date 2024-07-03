import os

def parse_csv(nombre_archivo:str)->list: 
    """Esta funcion parsea un archivo .csv"""
    lista_elementos = [] 
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r") as archivo:
            primer_linea = archivo.readline()
            primer_linea = primer_linea.replace("\n","")
            lista_claves = primer_linea.split(",")
            
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                diccionario_aux = {} 
                
                for i in range(len(lista_claves)):
                    diccionario_aux[lista_claves[i]] = lista_valores[i]
                
                
                lista_elementos.append(diccionario_aux)
                
        
        return lista_elementos

lista_preguntas = parse_csv("preguntas.csv")
def convertir_correcta_a_int(preguntas):
    for pregunta in preguntas:
        pregunta['correcta'] = int(pregunta['correcta'])
    return preguntas

lista_preguntas =convertir_correcta_a_int(lista_preguntas)

def mostrar_top(lista_elementos:list):

    if lista_elementos:
        informacion = "TOP\n NOMBRE | PUNTUACION| FECHA |\n"
        for puntaje in lista_elementos:
            for clave in puntaje:
                informacion += str(puntaje[clave]) + " | "

            informacion += "\n" 
        return informacion
    
