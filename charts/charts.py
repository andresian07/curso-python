import matplotlib.pyplot as plt # importando la libreria y usando el apartado pyplot

def generator():
  labels = ["a", "b", "c"]
  values = [300, 230, 156]
  fig, ax = plt.subplots()# aqui se crean dos variables que crean las cordenadas y la figura
  ax.pie(values,labels=labels) # aqui estamos guardando los valores y los nombres de cada uno en la grafica
  plt.savefig("pie.png")# aqui creamos una imagren y la guardamos en el proyecto
  plt.close# debemos hacer esto para cerrar el programa

  