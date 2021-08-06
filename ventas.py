import libsistema as lbs 
import libcrud as lbc

#menú para ventas
def submenu():

#variables tipo lista para archivos
  vendedores = []
  clientes = []
  productos = []
  detalles = []
  ventas = []
  
#cargar los archivos llamando funciones
  vendedores = lbc.cargar(vendedores,'vendedores.dat')
  clientes = lbc.cargar(clientes,'clientes.dat')
  productos = lbc.cargar(productos,'productos.dat')

#bucle para seleccionar las opciones
  a = True
  while a:
    #llamado del menú que muestra las opciones
    lbs.subMenu('VENTAS')
    select = input()
    if select == '6':
      a = False
    elif select == '1':
        #Llama función que permite insertar ventas
        venta = lbs.inserta_venta(vendedores,clientes,ventas)
        lbs.mostrar_productos(productos)

        suma_subtotales = 0
        suma_iva = 0
        suma_total = 0

        while True:
            #llama función que inserta detalles de la venta
              detalle = lbs.inserta_detalle(productos,venta[0])
              #agregar los detalles a la variable que pertenece
              suma_subtotales = suma_subtotales + detalle[4]
              suma_iva        = suma_iva + detalle[5]
              suma_total      = suma_total + detalle[6]
              #agregando lista a lista
              detalles.append(detalle)
              respuesta = input('agregar otro producto SI/NO: ')[:1]
              if respuesta.upper() != 'S':
                break
          #detalles especificos al final de la venta para la hora de listar
        venta.append(suma_subtotales)
        venta.append(suma_iva)
        venta.append(suma_total)
          #agregando lista a lista
        ventas.append(venta)
        lbs.pausaEnter("verde","finalizado\n<ENTER>") 


    elif select == '2':
      
      #listado de las ventas
      lbs.listar_ventas(ventas)
      #llamado a pausa
      lbs.pausaEnter("verde","listado\n<ENTER>")

    elif select == '3':
      codigo = input('digita codigo de la factura: ')
      #llamado a función que busca si el codigo anterior corresponde a alguna factura
      i = lbs.buscar(ventas,codigo)
      if i < 0:
        print('N° DE FACTURA NO ENCONTRADO')
      else:
        venta = ventas[i]
        #función que muestra la venta de acuerdo al codigo encontrado
        lbs.mostrar_venta(venta)
        print(130*'-')
        #comparar el codigo encontrado con los codigos de los detalles
        lbs.mostrar_detalles(codigo,detalles)
        input()

    elif select == '4':
      if len(ventas) > 0:
          codigo = input('CODIGO: ')
          #llamado a función que busca el codigo dentro de la venta
          i = lbs.buscar(ventas,codigo)
          if i < 0:
            print('CODIGO NO ENCONTRADO')
          else:
            venta = ventas[i]
            #mostrar la venta
            lbs.mostrar_venta(venta)
            #anular la venta
            lbs.anular(venta)
      else:
        lbs.pausaEnter('rojo','no hay ventas en la lista')

    elif select == '5':
      #guardar venta y detalles
      lbc.guardar(ventas,'ventas.dat')
      lbc.guardar(detalles,'detalles.dat')
      lbs.pausaSegundos('verde','factura alamacenada',3)