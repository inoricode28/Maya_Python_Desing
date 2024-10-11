# ////// COMANDOS //////

import maya.cmds

''' Importando el módulo y ejecutando '''
rad = 5
maya.cmds.polySphere(radius=rad, sa=8, sh=8)

''' Cambiando el nombre del módulo '''
import maya.cmds as cafe
cafe.polyCube(h=5, w=14, d=5)

''' Cambiando el nombre del módulo como cm '''
import maya.cmds as mc
mc.polyPlane(h=14, w=18, sh=1, sw=1)

''' Modos de los comandos '''

# Create
mc.polyCube(n='cubo', w=5)

# Edit
mc.polyCube('cubo', edit=True, d=15)

# Query
longitud = mc.polyCube('cubo', query=True, w=True)

mc.polySphere(r=longitud/2)

# ////// MEL y PYTHON //////

''' Mel '''
polyCube -w 5 -h 5 -d 5 -sx 2 -sy 2 -sz 2;
move -r 0 2.5 0;

''' Python '''
mc.polyCube(w=5, h=5, d=5, sx=2, sy=2, sz=2)
mc.move(0, 2.5, 0, r=True)
