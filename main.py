import libsistema as lbs
import vendedores,clientes,productos,ventas,grafica
#variable booleana para entrar al ciclo
a = True

#ciclo para elegir opciones en el menú
while a:
  #llamado a función que muestra el menú
  lbs.menuPrincipal()
  select = input()
  if select == '6':
    a = False
  elif select == '1':
    vendedores.submenu()
  elif select == '2':
    clientes.submenu()
  elif select == '3':
    productos.submenu()
  elif select == '4':
    ventas.submenu()
  elif select == '5':
    grafica.submenu()
