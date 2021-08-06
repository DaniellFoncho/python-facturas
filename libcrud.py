import pickle 
import libsistema as lbs 

#----------------------GENERAL--------------------------

#Función para guardar listas en archivos
def guardar(lista,titulo):
  archivo = open(titulo,'wb')
  pickle.dump(lista, archivo)
  archivo.close

#Función para cargar archivos en listas de variables
def cargar(lista,titulo):
  try:
    archivo = open(titulo,'rb')
    lista = pickle.load(archivo)
    lbs.pausaSegundos('verde',)
    print('se cargó el archivo')
  except:
    print('error al cargar',3)
  return lista


