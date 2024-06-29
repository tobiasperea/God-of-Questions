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
