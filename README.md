Practicar el uso de expresiones regulares para extraer diversos tipos de información de un texto, similar a cómo podríamos extraer datos relevantes de un documento o correo electrónico en un entorno profesional.

A continuación, encontrarán un texto con información importante relacionada con una reunión del curso de programación. El objetivo es utilizar expresiones regulares para identificar y extraer diferentes elementos de este texto, tales como: nombres, correos electrónicos, teléfonos, fechas, direcciones, entre otros.

Extraer: 

Nombres completos: Todos los nombres de las personas mencionadas en el texto.

Correos electrónicos: Extraer todas las direcciones de correo electrónico.

Fechas: Localizar todas las fechas mencionadas en el texto.

Horas: Extraer las horas indicadas (por ejemplo, 10:00 AM, 5:00 PM).

Teléfonos: Identificar los números de teléfono mencionados.

Direcciones físicas: Extraer todas las direcciones mencionadas, incluidas calles, números de oficina, etc.

Enlaces web: Extraer todas las URLs o enlaces mencionados.

Títulos de temas: Identificar los nombres de los temas o asuntos mencionados en el texto (por ejemplo, "gestión de proyectos ágiles").

Organización de la empresa: Extraer los nombres de las empresas o instituciones mencionadas (por ejemplo, "empresa.com", "dominio.com").

Referencias:
https://support.google.com/a/answer/1371415?hl=es

Operador	Descripción
.	Coincide con cualquier carácter excepto saltos de línea.
^	Coincide con el inicio de una línea o cadena.
$	Coincide con el final de una línea o cadena.
*	Coincide con 0 o más repeticiones del elemento anterior.
+	Coincide con 1 o más repeticiones del elemento anterior.
?	Coincide con 0 o 1 repetición del elemento anterior.
{n,m}	Coincide con entre n y m repeticiones del elemento anterior.
[]	Coincide con cualquier carácter dentro de los corchetes. Ejemplo: [abc] coincide con "a", "b" o "c".
`	`
()	Agrupa expresiones, creando una subexpresión.
\d	Coincide con cualquier dígito (equivalente a [0-9]).
\D	Coincide con cualquier carácter que no sea un dígito.
\w	Coincide con cualquier carácter de palabra (letras, números y guión bajo).
\W	Coincide con cualquier carácter que no sea una palabra.
\s	Coincide con cualquier espacio en blanco (espacio, tabulador, salto de línea).
\S	Coincide con cualquier carácter que no sea un espacio en blanco.
Caracteres especiales:
\\: Para incluir un carácter de barra invertida (se necesita un escape).
^: Al principio de un conjunto, significa "negación". Ejemplo: [^a-z] coincide con cualquier cosa que no sea una letra minúscula.
