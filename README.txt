Complejidad Computacional
Programa 1: Algoritmos No deterministicos
Alumna: Ana Valeria Deloya Andrade

* Ruta más corta

Este problema se encuentra en el archivo "rmc.py" dentro de la carpeta src.

En el archivo de texto "rmc.txt" se encuentra la gráfica, la primer línea contiene a los vértices, en la segunda
va a estar el valor k, y es a partir de la tercera línea que tenemos las aristas de la forma "1,2,3" donde los primeros dos elementos 
son los vértices que la conforman y el tercer elemento es el peso de la arista.

* 3-SAT

Este problema se encuentra en el archivo "3sat.py" dentro de la carpeta src.

Debemos tener una formula booleana en un archivo de texto "3sat_archivo.txt",
es importante que la formula sea de este estilo:

( x + -y + z ) * ( -x + y + -z ) * ( -x + y + z ) * ( x + y + -z )

Con cada elemento sepadado por un espacio en blanco.

Para compilar y ejecutar:

	python3 3sat.py 3sat_archivo.txt
