import libsistema as lbs 
import libcrud as lbc


#CRUD vendedores
def submenu():
  #variable de lista para guardar listas
  vendedores = []
  a = True
  #ciclo para seleccionar las opciones
  while a:
    #llamado a la función de submenú
    lbs.subMenu('VENDEDORES')
    select = input()
    if select == '7':
      a = False
    elif select == '1':
      codigo = input('digite codigo: ')
      #llamar función que no permite duplicar codigo
      codigoDuplicado = lbs.validar_codigo(vendedores,codigo)
      if codigoDuplicado:
        lbs.pausaEnter('rojo','no se permiten codigos duplicados\n<ENTER>')
      else:
        #llamar función que permite insertar codigo
        vendedor = lbs.insertar(codigo)
        vendedores.append(vendedor)
        #función para pausar
        lbs.pausaEnter('verde','agregado\n<ENTER>')
    elif select == '2':
      if len(vendedores)>0:
        #llamar función que enlista
        lbs.listar(vendedores,'vendedores')  
        lbs.pausaEnter('verde','listado')
      else:
        lbs.pausaEnter('rojo','no hay elementos en la lista')
    elif select == '3':
      codigo = input('CODIGO: ')
      #llamar función que busca el codigo
      i = lbs.buscar(vendedores,codigo)
      if i < 0:
        lbs.pausaEnter('rojo','el codigo no existe\n<ENTER>')
      else:
        vendedor = vendedores[i]
        #función para mostrar al vendedor
        lbs.mostrar(vendedor)
        lbs.pausaEnter('verde','consultado')
    elif select == '4':
      if len(vendedores) > 0:        
        codigo = input('digite codigo: ')
         #llamado a función para buscar vendedor
        i = lbs.buscar(vendedores,codigo)
        if i < 0:
          lbs.pausaEnter('rojo','el codigo no existe\n<ENTER>')
        else:
          vendedor = vendedores[i]
          #llamado a función para buscar vendedor
          lbs.mostrar(vendedor)
          lbs.pausaEnter('verde','<ENTER>')
          #llamado a función para actualizar vendedor
          lbs.actualizar(vendedor,vendedores)
          input() 
      else:
        lbs.pausaEnter('rojo','no hay codigos en lista\n<ENTER>')
    elif select == '5':
      if len(vendedores) > 0:
          codigo = input('CODIGO: ')
          #llamado a función que busca vendedor
          i = lbs.buscar(vendedores,codigo)
          if i < 0:
            lbs.pausaEnter('rojo','codigo no existente\n<ENTER>')
          else:
            vendedor = vendedores[i]
            #llamado a función que muestra al vendedor
            lbs.mostrar(vendedor)
            #llamado a función que elimina al vendedor
            lbs.eliminar(i,vendedores)
    elif select == '6':
      #llamado a función que guarda la lista vendedores que contiene la lista de cada vendedor
      lbc.guardar(vendedores,'vendedores.dat')
      lbs.pausaEnter('verde','guardado\n<ENTER>')
    else:
      lbs.pausaEnter('rojo','selecciones una de las opciones')