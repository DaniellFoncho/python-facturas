import libsistema as lbs 
import libcrud as lbc
import matplotlib.pyplot as plt

#almacenar facturas anuladas
def listar_Facanuladas(lista):
  registro = []
  for elemento in lista:
    if elemento[4] == 'anulada':
      registro.append(elemento[0])
  return registro

#Función que retorna el total vendido de un producto
def getTotalProducto(an,det,pro):
  suma = 0
  for elemento in det:
    if elemento[1][0] == pro:
      for elemento2 in an:
        if elemento[0] == elemento2:
          elemento[6] = 0
          suma += elemento[6]
        else:
          suma += elemento[6]
  return suma

#Función que retorna el total vendido de un vendedor
def getTotalVendedor(vent,vend):
  suma = 0
  for elemento in vent:
    if elemento[2][0] == vend:
      if elemento[4] == 'anulada':
        elemento[7] = 0
        suma += elemento[7]
      else:       
        suma += elemento[7]
  return suma

#variables para cargar archivos
productos = []
detalles = []
vendedores = []
ventas = []

#funcion que carga los archivos
productos = lbc.cargar(productos,'productos.dat')
detalles = lbc.cargar(detalles,'detalles.dat')
vendedores = lbc.cargar(vendedores,'vendedores.dat')
ventas = lbc.cargar(ventas,'ventas.dat')

#Llamado a la función que retorna las facturas anuladas
anulada = listar_Facanuladas(ventas)


#---------------------PRODUCTOS----------------------
#Eje X para productos
ejeXproductos = []
for elemento in productos:
  ejeXproductos.append(elemento[0])

#Eje Y para productos
ejeYproductos = []
for elemento in ejeXproductos:
  total = getTotalProducto(anulada,detalles,elemento)
  ejeYproductos.append(total)


#---------------------VENDEDORES------------------------
#Eje X para vendedores
ejeXvendedores = []
for elemento in vendedores:
  ejeXvendedores.append(elemento[0])

#Eje Y para vendedores
ejeYvendedores = []
for elemento in ejeXvendedores:
  total = getTotalVendedor(ventas,elemento)
  print(total)
  ejeYvendedores.append(total)


#-------------------------MENÚ--------------------------
#submenú
def submenu():
  
  
#Bucle que permite entrar al submenú
  adentro = True
  while adentro:
    #mostrar submenú llamando función
    lbs.subMenu('GRAFICAS')
    ingreso = input()
    
    if ingreso == '3':
      adentro = False

    elif ingreso == '1':
      lbs.SetLimpiar()
      lbs.listar_ventas(ventas)
      lbs.mostrar_productos(productos)
      lbs.mostrar_facanulada(anulada)      
      #histograma de ventas por producto
      plt.figure(figsize=(3,3))
      plt.bar(ejeXproductos,ejeYproductos, label='productos')
      plt.show()
 
    elif ingreso == '2':
      lbs.SetLimpiar()
      lbs.listar_ventas(ventas)
      lbs.mostrar_productos(productos)
      lbs.mostrar_facanulada(anulada) 
      #diagrama cirucular ventas x vendedor
      plt.figure(figsize=(3,3))
      plt.pie(ejeYvendedores, labels = ejeXvendedores,autopct='%0.1f%%')
      plt.show()
