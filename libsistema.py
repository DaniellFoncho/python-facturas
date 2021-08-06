import os
from tabulate import tabulate
import time
from datetime import datetime

#-------------------FUNCIONES GENERALES-------------------
#colores
def setColor(col):
    color= '\033[37m' # WHITE = '\033[37m'por default
    if (col=="negro"):
        color=  '\033[30m' # BLACK = '\033[30m'    
    elif (col=="rojo"):
        color= '\033[31m'    # RED = '\033[31m'      
    elif (col=="verde"):
        color= '\033[32m'  # GREEN = '\033[32m'        
    elif (col=="amarillo"):
        color= '\033[33m'  # YELLOW = '\033[33m'
    elif (col=="azul"):        
        color = '\033[34m' # BLUE = '\033[34m'          
    elif (col =="magenta"):
        color =  '\033[35m'# MAGENTA = '\033[35m'             
    elif (col=="cyan"):
        color =  '\033[36m' # CYAN = '\033[36m' 
    return color

#pausar 
def pausaEnter(color,texto):
    print('\n\n')
    mensaje = setColor(color) + texto + setColor("ninguno")
    input(mensaje)

#pausar
def pausaSegundos(color,texto,segundos):
  print('\n\n')
  mensaje = setColor(color) + texto + setColor("ninguno")
  print(mensaje)
  time.sleep(segundos)

def SetLimpiar():
  os.system('clear')

#------------------FUNCIONES PARA MENÚS-------------------
#menú principal
def menuPrincipal():
  os.system('clear')
  print(tabulate([
    ["***   ALMACÉN MARKET - CYCLE   ***"]]))
  print(31*'-')
  print('\t\tMENÚ PRINCIPAL')
  print(31*'-')
  print(tabulate([['VENDEDOR[1]'],
                  ['CLIENTE [2]'],
                  ['PRODUCTO[3]'],
                  ['VENTAS  [4]'],
                  ['GRAFICAS[5]'],
                  ['SALIR   [6]']],tablefmt="github"))

#submenú vendedor, cliente, producto
def subMenu(titulo):
  os.system('clear')
  print(tabulate([
    ["***   ALMACÉN MARKET - CYCLE   ***"]]))
  print(31*'-')
  print('\t\tMENÚ',titulo)
  print(31*'-')
  if titulo == 'GRAFICAS':
    print(tabulate([['VENTAS * PRODUCTOS [1]'],
                    ['VENTAS * VENDEDORES[2]'],
                    ['SALIR              [3]']],tablefmt="github"))
  elif titulo != 'VENTAS':
    print(tabulate([['INSERTAR  [1]'],
                    ['LISTAR    [2]'],
                    ['CONSULTAR [3]'],
                    ['ACTUALIZAR[4]'],
                    ['ELIMINAR  [5]'],
                    ['GUARDAR   [6]'],
                    ['SALIR     [7]']],tablefmt="github"))
  else:
    print(tabulate([['INSERTAR  [1]'],
                    ['LISTAR    [2]'],
                    ['CONSULTAR [3]'],
                    ['ANULAR    [4]'],
                    ['GUARDAR   [5]'],
                    ['SALIR     [6]']],tablefmt="github"))

#---------FUNCIONES PARA CLIENTES Y VENDEDORES-----------

#insertar codigo y nombre de vendedor,cliente
def insertar(codigo):
  os.system('clear')
  nombre = input('digite nombre: ')
  registro = [codigo, nombre]
  return registro

#listar vendedor y cliente
def listar(lista,titulo):
  os.system('clear')
  print(tabulate([[titulo]],tablefmt="github"))
  print(tabulate(lista,['Codigo','Nombre'],tablefmt="github"))

#mostrar vendedor y cliente
def mostrar(lista):
  os.system('clear')
  print(tabulate([['Codigo','Nombre'],lista],tablefmt="github"))

#actualizar vendedor y cliente
def actualizar(elemento,lista):
  os.system('clear')
  print(tabulate([['inserte 1 para cambiar codigo,\ninserte 2 para cambiar nombre']]))
  msg = input('codigo[1] o nombre[2]:')
  if msg == '1':
    continuar = 'S'
    codigo_usado = True
    while codigo_usado:
      os.system('clear')
      codigo = input('digite un nuevo codigo: ')
      codigo_usado = False
      for i in lista:
        if codigo == i[0]:
          pausaEnter('rojo','el codigo se encuentra en uso\n<ENTER>')
          codigo_usado = True
      print(tabulate([['presione S para continuar,presione\ncualquier tecla para salir']]))
      continuar = input().upper()
      if continuar != 'S':
        codigo_usado = False
        pausaEnter('verde','...<doble ENTER>')
    if continuar == 'S':
      elemento[0] = codigo
      pausaEnter('verde','finalizado\n<doble ENTER>')
  elif msg == '2':
    elemento[1] = input('digite un nuevo nombre')
  else:
    print('digite 1 para cambiar codigo,\ndigite 2 para cambiar nombre')

#-----FUNCIONES PARA VENDEDOREs, CLIENTES Y PRODUCTOS-----

#eliminar listas de la lista
def eliminar(ind,lista):
  print(tabulate([['para continuar seleccione 1,\npara no seguir seleccione 2']]))
  eliminar = input()
  if eliminar == '1':
    lista.pop(ind)
    pausaEnter('verde','eliminado\n<ENTER>')
  elif eliminar == '2':
    pausaEnter('ninguno','...<ENTER>')
  else:
    pausaEnter('rojo','no seleccionó opciones\n<ENTER>')

#buscar vendedor, cliente y producto
def buscar(lista,codigoBuscado):
    posicion = -10000000
    for indice, elemento in enumerate(lista):
      if lista[indice][0] == codigoBuscado:
        return indice
    return posicion

#validar codigos
def validar_codigo(lista,codigoBuscado):
  os.system('clear')
  for i in lista:
    if i[0] == codigoBuscado:
      return True
    return False

#----------------FUNCIONES PARA PRODUCTOS-----------------
#insertar codigo y nombre de vendedor,cliente
def insertarProducto(codigo):
  os.system('clear')
  nombre = input('digite nombre: ')
  color = input('digite color: ')
  precio = int(input('digite precio: '))
  a = True
  tipo = ''
  while a:
    print(tabulate([['Nacional [1]-Importada[2]']]))
    tipo = input('digite tipo: ')
    if tipo == '1':
      tipo = 'nacional'
      a = False
    elif tipo == '2':
      tipo = 'importada'
      a = False
    else:
      a = True
  registro = [codigo,nombre,color,precio,tipo]
  return registro

#listar los productos
def listarProducto(lista,titulo):
  os.system('clear')
  print(tabulate([[titulo]],tablefmt="github"))
  print(tabulate(lista,['Codigo','Nombre','Color','Precio','Tipo'],tablefmt="github"))

#mostrar los productos
def mostrarProducto(lista):
  os.system('clear')
  print(tabulate([['Codigo','Nombre','Color','Precio','Tipo'],lista],tablefmt="github"))

#actualizar un producto
def actualizarProducto(elemento,lista):
  os.system('clear')
  print(tabulate([['inserte 1 para cambiar codigo,\ninserte 2 para cambiar nombre\ninserte 3 para cambiar color\ninserte 4 para cambiar precio\ninserte 5 para cambiar tipo',]]))
  msg = input('codigo[1]-nombre[2]-color[3]-precio[4]-tipo[5]: ')
  if msg == '1':
    continuar = 'S'
    codigo_usado = True
    while codigo_usado:
      os.system('clear')
      codigo = input('digite un nuevo codigo: ')
      codigo_usado = False
      for i in lista:
        if codigo == i[0]:
          pausaEnter('rojo','el codigo se encuentra en uso\n<ENTER>')
          codigo_usado = True
      print(tabulate([['presione S para continuar,presione\ncualquier tecla para salir']]))
      continuar = input().upper()
      if continuar != 'S':
        codigo_usado = False
        pausaEnter('verde','...<doble ENTER>')
    if continuar == 'S':
      elemento[0] = codigo
      pausaEnter('verde','finalizado\n<doble ENTER>')
  elif msg == '2':
    continuar = 'S'
    nombre_usado = True
    while nombre_usado:
      os.system('clear')
      nombre = input('digite un nuevo nombre: ')
      nombre_usado = False
      for i in lista:
        if nombre == i[1]:
          pausaEnter('rojo','el nombre se encuentra en uso\n<ENTER>')
          nombre_usado = True
      print(tabulate([['presione S para continuar,presione\ncualquier tecla para salir']]))
      continuar = input().upper()
      if continuar != 'S':
        codigo_usado = False
        pausaEnter('verde','...<doble ENTER>')
    if continuar == 'S':
      elemento[1] = nombre
      pausaEnter('verde','finalizado\n<doble ENTER>')
  elif msg == '3':
    elemento[2] = input('digite un nuevo color: ')
    pausaEnter('verde','actualizado\n<doble ENTER>')
  elif msg == '4':
    elemento[3] = int(input('digite un nuevo precio: '))
    pausaEnter('verde','actualizado\n<doble ENTER>')
  elif msg == '5':
    if elemento[4] == 'nacional':
       elemento[4] = 'importada'
       pausaEnter('verde','tipo actualizado\n<doble ENTER>')
    elif elemento[4] == 'importada':
       elemento[4] = 'nacional'
       pausaEnter('verde','tipo actualizado\n<doble ENTER>')
  else:
    print('digite 1 para cambiar codigo,\ndigite 2 para cambiar nombre')

#-----------------FUNCIONES PARA VENTAS-------------------

#mostrar los clientes
def mostrar_clientes(lista):
  os.system('clear')
  print(tabulate([['CLIENTES']],tablefmt="github"))
  print(tabulate(lista,tablefmt="github"))
  pausaEnter('verde','cargado\n<ENTER>')

#mostrar los vendedores
def mostrar_vendedores(lista):
  print(tabulate([['VENDEDORES']],tablefmt="github"))
  print(tabulate(lista,tablefmt="github"))
  pausaEnter('verde','cargado\n<ENTER>')

#mostrar los productos
def mostrar_productos(lista):
  print(tabulate([['PRODUCTOS']],tablefmt="github"))
  print(tabulate(lista,tablefmt="github"))
  pausaEnter('verde','cargado\n<ENTER>')

#insertar las ventas
def inserta_venta(vend,cli,lista):
  factura = input("NUMERO FACTURA:")
  existe = validar_codigo(lista,factura)
  if existe:
    print('CODIGO DUPLICADO-NO PERMITIDO')
  else:
    #información especifica de la venta
    mostrar_clientes(cli)
    mostrar_vendedores(vend)
    c = ''
    while len(c)<1:
      cliente  = input("digite codigo del cliente: ")
      for i in cli:
        if i[0] == cliente:
          c = i
          print(tabulate([c]))
    v = ''
    while len(v)<1:
      vendedor  = input("digite codigo del vendedor: ")
      for i in vend:
        if i[0] == vendedor:
          v = i
          print(tabulate([v])) 
    fecha = datetime.now() 
    estado = '1'  #1 activa 2 anulada
    if estado == '1':
      estado = 'activo'
    pausaEnter('verde','comprobado\n<ENTER>')
    os.system('clear')
    registro = [factura,c,v,fecha.strftime('%d/%m/%Y'),estado]
    return registro

#insertar los detalles
def inserta_detalle(pro,vent):
    p = ''
    while len(p)<1:
      producto  = input("digite codigo del producto: ")
      for i in pro:
        if i[0] == producto:
          p = i
          print(tabulate([p]))

    cantidad = int(input('CANTIDAD: '))
    precio = p[3]
    subtotal = cantidad * precio
    tipo = p[4]
    if tipo == 'nacional':
      porcentajeIva = 0.10
      iva = subtotal * porcentajeIva
      total = subtotal + iva
    elif tipo == 'importada':
      porcentajeIva = 0.20
      iva = subtotal * porcentajeIva
      total = subtotal + iva
    

    registro = [vent, p, cantidad,precio,subtotal, iva, total]
    return registro

#listado de ventas
def listar_ventas(lista):
  for elemento in lista:
    print(tabulate([['VENTAS'],['N° Factura','Cliente','Vendedor','Fecha','Estado','Subtotal','IVA','Total',],elemento],tablefmt="github"))

#Función que permite mostrar la lista de ventas especificamente
def mostrar_venta(lista):
  print(tabulate([['N° Factura','Cliente','Vendedor','Fecha','Estado','Subtotal','IVA','Total'],lista],tablefmt="github"))

#Función que permite mostrar los detalles especificamente
def mostrar_detalles(cod,lista):
  detalles = []
  for indice, elemento in enumerate(lista):
    if elemento[0] == cod:
      detalles.append(elemento)
  print(tabulate(detalles,['N° Factura','Producto','Cantidad','Precio','Subtotal','IVA','Total'],tablefmt="github"))

#anular el estado de la venta
def anular(e):
  print(tabulate([['anular factura SI[S]-NO[N]']]))
  nula = input().upper()
  if nula == 'S':
    ingreso = True
    while ingreso:
      estado = 'anulada'
      ingreso = False
      for i in e:
        if estado != e[4]:
          print(setColor('verde')+'FACTURA ACTIVA'+setColor('ninguno'))
          ingreso = True
          continuar = input('continuar-SI[S]-NO[N] ').upper()
          if continuar == 'S':
            e[4] = estado
            ingreso = False
            pausaEnter('verde','venta anulada\n<ENTER>')
          elif continuar != 'S':
            ingreso = False
            pausaEnter('rojo','venta no anulada\n<ENTER>')
  elif nula != 'S':
    pausaEnter('verde','retrocediendo acción\n<ENTER>')

#---------------------------GRAFICAS------------------------------
def mostrar_facanulada(null):
  print(tabulate([['FAC - ANULADAS']]))
  print(tabulate([null],tablefmt="github"))
  pausaEnter('verde','cargado\n<ENTER>')
