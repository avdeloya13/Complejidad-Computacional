Complejidad Computacional
Programa 1: Algoritmos No deterministicos
Alumna: Ana Valeria Deloya Andrade

* Ruta más corta


* 3-SAT

Este problema se encuentra en el archivo "3sat.py" dentro de la carpeta src.

Debemos tener una formula booleana en un archivo de texto, es importante que la formula sea de este estilo:

( x + -y + z ) * ( -x + y + -z ) * ( -x + y + z ) * ( x + y + -z )

Con cada elemento sepadado por un espacio en blanco. El nombre de nuestro archivo es "3sat_archivo.txt"

Para compilar y ejecutar:

	python3 3sat.py 3sat_archivo.txt
