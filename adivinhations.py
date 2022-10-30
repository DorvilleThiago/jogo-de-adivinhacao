import random
from time import sleep

def Gerar(a,b):
  a = random.randint(a,b)
  return a

def GetBestPlayer():
  if len(jogadores) == 0:
    return "Nenhum jogador jogou ainda"
  a = 999
  for player in jogadores:
    if player[1] < a:
      a = player[1]
      bestplayer = player[0]
  return f"Melhor jogador: {bestplayer} com {a} tentativas"
    

def Menu():
  print("-"*50)
  print("Joguinho da Adivinhação".center(50))
  print("Você deve adivinhar o número entre 0 e 100".center(50))
  print("-"*50)
  print(" ")
  print("[0] Jogar")
  print("[1] Exibir Resultado")
  print("[2] Sair")

def Game():
  print("="*30)
  print("Adivinhe um valor entre 0 e 100")
  print("="*30)

def SpacePrint(a):
  print(" ")
  print(a)
  print(" ")

def CheckName(name):
  for player in jogadores:
    if player[0] == name:
      return True
  return False

def GetNamePos(name):
  contador = 0
  for player in jogadores:
    if player[0] == name:
      return contador
    return "não encontrado"

def SetScorePos(pos,score):
  jogadores[pos][1] = score

def GetScoreByPos(pos):
  return jogadores[pos][1]

def GetSalvo():
  try:
    salvo
  except NameError:
    return 100
  else:
    return salvo

def GetRight():
  try:
    right
  except NameError:
    return 0
  else:
    return right

jogadores = []

while True:
  sleep(1)
  Menu()
  choice = input("\n> ").strip()
  if choice == "0": #Jogar
    nome = input("Digite seu nome > ")

    salvo = None
    right = None
    del salvo
    del right

    if CheckName(nome): #Se o nome já existir
      randint = Gerar(0,100)
      contador = 0
      while True:

        adivinhado = input("Digite sua resposta > ").strip()

        if adivinhado.isnumeric():
          adivinhado = int(adivinhado)
          if adivinhado > randint: #se input for maior
                try:
                  salvo
                except:            
                  print(randint)
                  SpacePrint(f"Incorreto, a resposta está entre {GetRight()} e {adivinhado}")
                  contador = contador + 1
                  salvo = adivinhado
                  continue
                else:
                  if adivinhado > salvo:
                    SpacePrint("Derrota, Você digitou um número que não estava entre os corretos")
                    break
                  else:
                    print(randint)
                    SpacePrint(f"Incorreto, a resposta está entre {GetRight()} e {adivinhado}")
                    contador = contador + 1
                    salvo = adivinhado
                    continue
          elif adivinhado < randint: #se input for menor
                try:
                  right
                except:
                  print(randint)
                  SpacePrint(f"Incorreto, a resposta está entre {adivinhado} e {GetSalvo()}")
                  contador = contador + 1
                  right = adivinhado
                  continue
                else:
                  if adivinhado < right:
                    SpacePrint("Derrota, Você digitou um número que não estava entre os corretos")
                    break
                  else:
                    print(randint)
                    SpacePrint(f"Incorreto, a resposta está entre {adivinhado} e {GetSalvo()}")
                    contador = contador + 1
                    right = adivinhado
                    continue
          else:
              SpacePrint("Correto, você venceu!")
              position = GetNamePos(nome)
              if contador+1 < GetScoreByPos(position):
                SetScorePos(position, contador+1)
              break
        
        else:
          SpacePrint("ERRO; Caractere inválido")
    else: #Se o nome não existir
      randint = Gerar(0,100)
      jogador = [nome]
      contador = 0
      while True:

        adivinhado = input("Digite sua resposta > ").strip()

        if adivinhado.isnumeric():
          adivinhado = int(adivinhado)
          if adivinhado > randint: #se input for maior
              try:
                salvo
              except:            
                SpacePrint(f"Incorreto, a resposta está entre {GetRight()} e {adivinhado}")
                contador = contador + 1
                salvo = adivinhado
                continue
              else:
                if adivinhado > salvo:
                  SpacePrint("Derrota, Você digitou um número que não estava entre os corretos")
                  break
                else:
                  SpacePrint(f"Incorreto, a resposta está entre {GetRight()} e {adivinhado}")
                  contador = contador + 1
                  salvo = adivinhado
                  continue
          elif adivinhado < randint: #se input for menor
              try:
                right
              except:
                SpacePrint(f"Incorreto, a resposta está entre {adivinhado} e {GetSalvo()}")
                contador = contador + 1
                right = adivinhado
                continue
              else:
                if adivinhado < right:
                  SpacePrint("Derrota, Você digitou um número que não estava entre os corretos")
                  break
                else:
                  SpacePrint(f"Incorreto, a resposta está entre {adivinhado} e {GetSalvo()}")
                  contador = contador + 1
                  right = adivinhado
                  continue
          else:
              SpacePrint("Correto, você venceu!")
              jogador.append(contador+1)
              jogadores.append(jogador)
              break
              
        else:
          SpacePrint("ERRO; Caractere inválido")
        

  elif choice == "1": #Exibir resultado
    print(" ")
    print(GetBestPlayer())
    print(jogadores)
    print(" ")
  elif choice == "2": #Sair
    SpacePrint("Programa finalizado")
    break
  else:
    SpacePrint("ERRO; Valor inválido")