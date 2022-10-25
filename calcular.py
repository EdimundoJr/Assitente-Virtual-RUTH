
def somar(numero1,numero2):
  numero_inteiro1 = int(numero1)
  numero_inteiro2 = int(numero2)
  resultado = numero_inteiro1 + numero_inteiro2
  print(f"O resultado da soma é: {resultado}")

def diminuir(numero1,numero2):
  numero_inteiro1 = int(numero1)
  numero_inteiro2 = int(numero2)
  resultado = numero_inteiro1 - numero_inteiro2
  print(f"O resultado da subtração é: {resultado}")
    
def multiplicar(numero1,numero2):
  numero_inteiro1 = int(numero1)
  numero_inteiro2 = int(numero2)
  resultado = numero_inteiro1 * numero_inteiro2
  print(f"O resultado da multiplicação é: {resultado}")
    
def divisao(numero1,numero2):
  numero_inteiro1 = int(numero1)
  numero_inteiro2 = int(numero2)
  resultado = numero_inteiro1 / numero_inteiro2
  print(f"O resultado da divisão é: {resultado}")

def maior(numero1,numero2):
  numero_inteiro1 = int(numero1)
  numero_inteiro2 = int(numero2)
  if(numero_inteiro1 > numero_inteiro2):
    print(f"Sim, O numero {numero1} é maior que o numero {numero2}")
  else:
    print(f"Não, O numero {numero1} não é maior que o numero {numero2}")

def menor(numero1,numero2):
  numero_inteiro1 = int(numero1)
  numero_inteiro2 = int(numero2)
  if(numero_inteiro1 < numero_inteiro2):
    print(f"Sim, O numero: {numero1} é menor que o numero: {numero2}")
  else:
    print(f"Não, O numero: {numero1} não é menor que o numero: {numero2}")


def par_impar(numero1):
  numero_inteiro1 = int(numero1)
  
  if (numero_inteiro1%2) == 0:
        print(f"O numeral {numero_inteiro1} é Par")
  else:
        print(f"O numeral {numero_inteiro1} é Ímpar")
  
def primo(numero1):
  numero_inteiro1 = int(numero1)

  
 
  ePrimo = 0

  for i in range(1, (numero_inteiro1 + 1)):
        if numero_inteiro1 % i == 0:
            ePrimo += 1

  if ePrimo == 2:
        print(f'Sim o {numero_inteiro1} é primo')
  else:
        print(f'Não o {numero_inteiro1} não é primo')

def executar( numero1, operacao, numero2):
    executado = False
    
    
    if operacao == "maior":
        maior(numero1,numero2)

        executado = True
        return executado
    
    if operacao == "menor":
        maior(numero1,numero2)

        executado = True
        return executado
    
    if operacao == "primo":
        primo(numero1)

        executado = True
        return executado
      
    if operacao == "ímpar" or operacao == "par":
        par_impar(numero1)

        executado = True
        return executado
    
    if operacao == "par":
        (numero1)

        executado = True
        return executado
    
    
    if operacao == "+":
        somar(numero1,numero2)

        executado = True
        return executado
    elif operacao == "-":
        diminuir(numero1,numero2)

        executado = True
        return executado
    elif operacao == "x":
        multiplicar(numero1,numero2)

        executado = True
        return executado
    elif operacao == "dividido":
        divisao(numero1,numero2)

        executado = True
        return executado

    

CALCULAR = {
    
    "executar": executar,
    
}

if __name__ == "__main__":
  
  executar()
