from re import X


def adicao(x, y):
  return x + y


def subtracao(x, y):

  return x - y


def multiplicacao(x, y):
  return x * y


def divisao(x, y):
  return x / y

  
def calculadora():
  print("1.adicao")
  print("2.subtracao")
  print("3.multiplicacao")
  print("4.divisao")
while True:
  escolha =input("Escolha(1/2/3/4):")
  if escolha in('1','2','3','4'):
    x =int(input("Digite o primeiro numero:"))
    y =int(input("Digite o segundo numero:"))
    if escolha=='1':
     print( "Resultado:",adicao(x,y))
    if escolha=='2':
     print( "Resultado:",subtracao(x,y))
    if escolha=='3':
      print( "Resultado:",multiplicacao(x,y))
    if escolha=='4':
      if y !=0:
         print( "Resultado:",divisao(x,y))
      else:
       print("Divisão não é permitida com 0")
  continuar = input("deseja continuar?(s/n")
  if continuar=="n":
   print("Calculadora Encerrada!")
   break  
          
