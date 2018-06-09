#Programa Principal

Temas = ['Variables', 'Estructuras de Control Selectivas', 'Estructuras de Control Repetitivas', 'Listas', 'Funciones', 'Strings']

print("¡Hola!")
print("Podemos revisar los siguientes temas:"'\n')

for i in Temas:
  print(f"{Temas.index(i)+1}. " + i)

def yourturn():
  a = input('\t')
  return a

def variables():
  ### info de variables
    print("Lo primero que debes saber sobre las variables es que se usan para almacenar información de cualquier tipo.")
    print("Se usan así:")
    print('\t'"a = 1+2")
    print("La variable 'a' almacena el valor de 1+2, o sea 3.")
    print("Ahora tú intenta definir una variable b con el número 4 como valor en la siguiente línea.")
    b = yourturn()
    if b.replace(' ','') == "b=4":
      print("¡Buen trabajo!")
    else:
      print("Tu respuesta debería verse similar a esto: b = 4")
    print('')
    print("Las variables también pueden almacenar texto.")
    print("Para esto, deben ser declaradas entre comillas de la siguiente manera: a = 'valor'.")
    print("En la siguiente línea declara una variable 'nombre' cuyo valor sea tu primer nombre.")
    global nombre
    c = yourturn().replace(' ','')
    nombre = nombre.replace('nombre=','').replace('"', '').capitalize()
    print(f"Un gusto conocerte, {nombre}")


def estructurasdecontrolselectivas():
  ### info de variables
    print("selectivas")

def estructurasdecontrolrepetitivas():
  ### info de variables
    print("repetitivas")

def listas():
  ### info de variables
    print("listas")

def funciones():
  ### info de variables
    print("funciones")

def strings():
  ### info de variables
    print("strings")


def question():
  answer = int(input('\n'"Ingresa el número del tema que deseas aprender hoy: "))
  if answer - 1 in range(0, len(Temas)):
    t = Temas[answer-1].lower()
    x = t.replace(' ', '')
    print("¡Buena elección!")
    print(f"Hoy aprenderemos {t}.")
    eval(f"{x}()")
  else:
    print("Lo sentimos, el número ingresado no es válido.")
    question()

question()
