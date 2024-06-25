
def parcear_csv(ruta):
    archivo = open(ruta, "r")
    for linea in archivo:
        print(linea, end="")

parcear_csv("preguntas.csv")


