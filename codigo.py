import re

# Cargar texto desde archivo
with open("carta.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Expresiones regulares
regex_nombres = re.findall(r'\b[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+ [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\b', texto)
regex_correos = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', texto)
regex_fechas = re.findall(r'\b\d{1,2} de [a-zA-ZáéíóúÁÉÍÓÚ]+\b', texto)
regex_horas = re.findall(r'\b\d{1,2}:\d{2} (AM|PM)\b', texto)
regex_telefonos = re.findall(r'\+\d{1,3} \d{3} \d{3} \d{3}', texto)
regex_direcciones = re.findall(r'Calle\s\w+\s\d{1,4},\s*oficina\s\d{1,4}', texto)
regex_urls = re.findall(r'https?://[^\s]+', texto)
regex_temas = re.findall(r'gestión de proyectos ágiles', texto, re.IGNORECASE)
regex_dominios = re.findall(r'@([\w\.-]+\.\w+)', texto)

# Eliminar duplicados con set y volver a lista
def limpiar(lista):
    return sorted(set(lista))

# Results
print("Nombres completos:", limpiar(regex_nombres))
print(" Correos electrónicos:", limpiar(regex_correos))
print(" Fechas:", limpiar(regex_fechas))
print(" Horas:", limpiar(re.findall(r'\b\d{1,2}:\d{2} (AM|PM)\b', texto)))
print(" Teléfonos:", limpiar(regex_telefonos))
print(" Direcciones físicas:", limpiar(regex_direcciones))
print(" Enlaces web:", limpiar(regex_urls))
print(" Títulos de temas:", limpiar(regex_temas))
print(" Dominios de correos:", limpiar(regex_dominios))
