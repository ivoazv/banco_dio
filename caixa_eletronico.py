def menu():
   print ("#" * 30)
   print ("""SEJA BEM VINDO AO BANCO DIO!
[1] => Depósito
[2] => Saque
[3] => Extrato
[4] => Criar novo usuário
[5] => Criar nova conta
[6] => Listar contas
[7] => Sair""")
   print ("#" * 30)




def deposito(saldo, valor_dep, espelho, /):
   while True:
      print ("""########## DEPÓSITO ##########""")
      valor_dep = float(input("Digite o valor a ser depositado: "))
      if valor_dep > 0:
         espelho.append(valor_dep)
         saldo = (sum(espelho))
         saldo + valor_dep
         print ("...efetuando depósito...")
         print ("O depósito foi efetuado com sucesso")
         break
      else:
         print ("valor inválido.")
         break


def saque(*, saldo, espelho):
   global numero_saques
   while True:
      print ("""########## SAQUE ##########""")
      print ("""NOTAS DE R$20,OO
NOTAS DE R$50,00
NOTAS DE R$100,00""")
      valor_saque = int(input("Digite o valor que deseja sacar: R$"))
      saldo = (sum(espelho))
      if numero_saques >= 3:
         print ("Limite de saques excedido!")
         break
      else:
         if valor_saque > 500:
            print ("O máximo permitido para saque é o valor de R$500")
            break
         elif valor_saque >=20: #começo do bloco verdadeiro
            if valor_saque <= saldo:
               saldo - valor_saque
               espelho.append(- valor_saque)
               numero_saques = numero_saques + 1
               print ("Aguarde a contagem de notas")
               break
            elif valor_saque > saldo:
               print ("Saldo insuficiente!")
               break
         elif valor_saque < 20:
            print ("O valor mínimo para saque é de R$20,00!") 
            break
         else:
            print ("Valor inválido!")
            continue
   return numero_saques





def extrato(saldo, /, espelho):
   saldo = (sum(espelho))
   print ("""########## EXTRATO ##########""")
   for v in (espelho):
      print (f"\t\tR${v:.2f}")
   print ("=" * 30)
   print (f"Total:\t\tR${saldo:.2f}")
   print ("=" * 30)



def filtrar_usuario(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
   return usuarios_filtrados[0] if usuarios_filtrados else None





def criar_usuario(usuarios):
   cpf = input("Informe o CPF (somente números): ")
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print ("Usuário já cadastrado!")
      return

   nome = input("Informe o nome completo: ")
   data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
   endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla do estado): ")

   usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

   print ("######Usuário criado com sucesso!######")




def criar_conta(agencia, numero_conta, usuarios):
   cpf = input("Informe o CPF do usuário: ")
   usuario = filtrar_usuario(cpf, usuarios)

   if usuario:
      print("\n Conta criada com sucesso!")
      return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

   print ("Usuário não encontrado!")



def listar_contas(contas):
   for conta in contas:
      print (f"""Agência:{conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']['nome']} """)



def main():
   while True:
      menu()
      opcao = int(input("Digite a opção que deseja: "))
      if opcao == 1:
         deposito(saldo, valor_dep, espelho)
      elif opcao == 2:
         saque(saldo=saldo, espelho=espelho)
      elif opcao == 3:
         extrato(saldo, espelho=espelho)
      elif opcao == 4:
         criar_usuario(usuarios)
      elif opcao == 5:
         numero_conta = len(contas) + 1
         conta = criar_conta(AGENCIA, numero_conta, usuarios)
         contas.append(conta)
      elif opcao == 6:
         listar_contas(contas)
      elif opcao == 7:
         print ("Obrigado! Até mais ;)")
         break



espelho = []
valor_dep = 0
saldo = 0
usuarios = []
contas = []
numero_saques = 0
AGENCIA = "001"


main()


