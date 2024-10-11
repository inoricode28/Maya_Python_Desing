import maya.cmds as cafe

# Crear la base del peine
cafe.polyCube(h=2, w=41, d=3)  # Base larga y plana del peine
cafe.move(0, 1, 0)  # Posiciona la base ligeramente hacia arriba

# Función para crear los dientes del peine
def tabla(name, alt, ubic):
    cafe.polyCube(n=name, w=1, h=alt, d=1, sx=2, sy=2, sz=2)  # Creación de un diente
    cafe.move(ubic, alt / 2 + 2, 0)  # Ajusta la posición en relación a la base

# Crear las tablas (dientes del peine)
for i in range(0, 22, 2):
    tabla(f'diente_{i}', 6, i - 10)  # Altura de 6, ubicaciones espaciadas uniformemente
