import libsistema as lbs 
import libcrud as lbc


#CRUD clientes
def submenu():
  #variable de lista para guardar listas
  clientes = []
  a = True
  #ciclo para seleccionar las opciones
  while a:
    #llamado a la función de submenú
    lbs.subMenu('CLIENTES')
    select = input()
    if select == '7':
      a = False
    elif select == '1':
      codigo = input('digite codigo: ')
      #llamar función que no permite duplicar codigo
      codigoDuplicado = lbs.validar_codigo(clientes,codigo)
      if codigoDuplicado:
        lbs.pausaEnter('rojo','no se permiten codigos duplicados\n<ENTER>')
      else:
        #llamar función que permite insertar codigo
        vendedor = lbs.insertar(codigo)
        clientes.append(vendedor)
        #función para pausar
        lbs.pausaEnter('verde','agregado\n<ENTER>')
    elif select == '2':
      if len(clientes)>0:
        #llamar función que enlista
        lbs.listar(clientes,'clientes')  
        lbs.pausaEnter('verde','listado')
      else:
        lbs.pausaEnter('rojo','no hay elementos en la lista')
    elif select == '3':
      codigo = input('CODIGO: ')
      #llamar función que busca el codigo
      i = lbs.buscar(clientes,codigo)
      if i < 0:
        lbs.pausaEnter('rojo','el codigo no existe\n<ENTER>')
      else:
        cliente = clientes[i]
        #función para mostrar al cliente
        lbs.mostrar(cliente)
        lbs.pausaEnter('verde','consultado')
    elif select == '4':
      if len(clientes) > 0:        
        codigo = input('digite codigo: ')
         #llamado a función para buscar cliente
        i = lbs.buscar(clientes,codigo)
        if i < 0:
          lbs.pausaEnter('rojo','el codigo no existe\n<ENTER>')
        else:
          cliente = clientes[i]
          #llamado a función para buscar cliente
          lbs.mostrar(cliente)
          lbs.pausaEnter('verde','<ENTER>')
          #llamado a función para actualizar cliente
          lbs.actualizar(cliente,clientes)
          input() 
      else:
        lbs.pausaEnter('rojo','no hay codigos en lista\n<ENTER>')
    elif select == '5':
      if len(clientes) > 0:
          codigo = input('CODIGO: ')
          #llamado a función que busca cliente
          i = lbs.buscar(clientes,codigo)
          if i < 0:
            lbs.pausaEnter('rojo','codigo no existente\n<ENTER>')
          else:
            cliente = clientes[i]
            #llamado a función que muestra al cliente
            lbs.mostrar(cliente)
            #llamado a función que elimina al cliente
            lbs.eliminar(i,clientes)
    elif select == '6':
      #llamado a función que guarda la lista clientes que contiene la lista de cada cliente
      lbc.guardar(clientes,'clientes.dat')
      lbs.pausaEnter('verde','guardado\n<ENTER>')
    else:
      lbs.pausaEnter('rojo','selecciones una de las opciones')