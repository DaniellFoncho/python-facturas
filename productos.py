import libsistema as lbs 
import libcrud as lbc

#submenú para productos
def submenu():

    #variable para almacenar a los datos
    productos = []
    a = True
    #ciclo para mostrar opciones
    while a:  
      #llamar a la función que muestra las opciones a seleccionar
      lbs.subMenu('PRODUCTOS')
      select = input()
      if select == '7':
        a = False

      elif select == '1':
        codigo = input('digite codigo: ')
        #llamado a función que valida codigo
        codigoDuplicado = lbs.validar_codigo(productos,codigo)
        if codigoDuplicado:
          lbs.pausaEnter('rojo','no se permiten codigos duplicados\n<ENTER>')
        else:
          #llamado a función que inserta producto
          producto = lbs.insertarProducto(codigo)
          productos.append(producto)
          #función para pausar
          lbs.pausaEnter('verde','agregado\n<ENTER>')

      elif select == '2':
        #llamado a función que lista productos
        lbs.listarProducto(productos,'productos')
        print('Fin De Listar')
        input()

      elif select == '3':
        codigo = input('CODIGO: ')
        #llamado a función que busca productos
        i = lbs.buscar(productos,codigo)
        if i < 0:
          lbs.pausaEnter('rojo','el codigo no existe\n<ENTER>')
        else:
          producto = productos[i]
          #llamado a función que muestra productos
          lbs.mostrarProducto(producto)
          lbs.pausaEnter('verde','consultado\n<ENTER>')


      elif select == '4':
        if len(productos) > 0:
          codigo = input('CODIGO: ')
          #llamado a función que busca productos
          i = lbs.buscar(productos,codigo)

          if i < 0:
            lbs.pausaEnter('rojo','el codigo no existe\n<ENTER>')
          else:
            producto = productos[i]
            #llamado a función que muestra producto
            lbs.mostrarProducto(producto)
            lbs.pausaEnter('verde','<ENTER>')
            #llamado a función que actualiza producto
            lbs.actualizarProducto(producto,productos)
            input() 
        else:
          lbs.pausaEnter('rojo','no hay codigos en lista\n<ENTER>')

      elif select == '5':
        if len(productos) > 0:
          codigo = input('CODIGO: ')
          #llamado a función que busca productos
          i = lbs.buscar(productos,codigo)
          if i < 0:
            print('CODIGO NO ENCONTRADO')
          else:
            producto = productos[i]
            #llamado a función que muestra productos
            lbs.mostrar(producto)
            #llamado a función que elemina productos
            lbs.eliminar(i,productos)

      elif select == '6':
        #llamado a función que guarda productos
        lbc.guardar(productos,'productos.dat')
        lbs.pausaEnter('verde','guardado\n<ENTER>')
    else:
      lbs.pausaEnter('rojo','selecciones una de las opciones')