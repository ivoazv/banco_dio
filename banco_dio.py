from time import sleep
import datetime
data_atual = datetime.datetime.now().strftime("%d/%m/%y " "%H:%M")
extrato =[]
vezes_de_saque = 0
saldo = (sum(extrato))
while True:
   print ("""SEJA BEM VINDO AO BANCO DIO!
1- Depósito
2- Saque
3- Extrato
4- Sair""")
   opcao = (input("Digite a opção desejada: "))
   if opcao == "1": #bloco de depósito
      print ("""########## DEPÓSITO ##########""")
      while True:
         valor = float(input("Digite o valor a ser depositado: "))
         while True:
            if valor > 0:
               extrato.append(+ valor)
               saldo = (sum(extrato))
               break
            else:
               print ("valor inválido.")
         sleep(1)
         print ("...efetuando depósito...")
         sleep(3)
         print("O depósito foi efetuado com sucesso")
         sleep(0.7)
         resposta = input("Deseja fazer outro depósito? (s/n) ")
         if resposta == "s":
            print ("Um momento por favor...")
            sleep(3)
         elif resposta == "n":
            break
   #fim do bloco de depósito

   if opcao == "2": #bloco de saque
      sleep(2)
      print ("""########## SAQUE ##########""")
      while True:
         print ("""NOTAS DE R$20,OO
NOTAS DE R$50,00
NOTAS DE R$100,00""")
         valor_saque = int(input("Digite o valor que deseja sacar: R$"))
         if valor_saque > 500:
            print ("O valor máximo para cada saque é de R$500,00")
            continue
         if valor_saque <= saldo:
            if valor_saque < 20:
               print ("R$20,00 é o mínimo para saque")
            elif valor_saque % 20 == 0 or valor_saque % 50 == 0 or valor_saque % 100 == 0:
               vezes_de_saque += 1
               if vezes_de_saque <= 3:
                  extrato.append(- valor_saque)
                  print ("Aguarde a contagem de notas")
                  sleep(2)
                  print ("Obrigado! Até a próxima! ;)")
                  break
               else:
                  sleep(1)
                  print ("Número de saques excedido")
                  sleep(1)
               break
            else:
               print ("Opção inválida")
         if valor_saque > saldo:
            sleep(1)
            print ("Limite insuficiente")
            sleep(2)
         break

   #fim do bloco de saque

   if opcao == "3": #bloco da condição extrato
      sleep(2)
      print (""" ########## EXTRATO ##########""")
      saldo = (sum(extrato)) 
      for v in (extrato):
         print (f"{data_atual} R${v:.2f}")
      print (f"    Total:R${saldo:.2f}")
   if opcao == "4":
      print ("Obrigado! Até a próxima! ;)")
      break
   if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4":
      print ("Opção inválida!")
