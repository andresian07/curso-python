print("aqui escribire un pequeño codigo de calculadora")

numero1 = int(input(" escribe un numero = "))
numero2 = int(input(" escribe un numero = "))
opcion = int(input("escribe opcion de operacion = "))

print(" escribe 1 para sumar\n2 para restar\n3 para multiplicar\n4 para dividir")

def calculadora(n1,n2):
 if opcion == 1:
  print(n1 + n2)
 elif opcion == 2:
  print(n1 - n2)
 elif opcion == 3:
  print(n1 * n2)
 elif opcion == 4:
  print(n1 / n2)
 else:
  print(" tu opcion es incorrecta ")

calculadora(numero1,numero2)