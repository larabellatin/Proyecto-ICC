#Programa Principal

Temas = ['Variables', 'Estructuras de Control Selectivas', 'Estructuras de Control Repetitivas', 'Listas', 'Funciones', 'Strings']

print("¡Hola!")
print("Podemos revisar los siguientes temas:"'\n')

for i in Temas:
  print(f"{Temas.index(i)+1}. " + i)

def variables():
  ### info de variables
    print("variables")

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
