# Desafio de Projeto - desenvolver um sistema Bancário

menu = '''
    ------------- Sistema Bancário - V1 -------------

    Operações

    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Sair
     
    -------------------------------------------------

'''
deposito = 0 #variável deve aceitar apenas valores positivos
saque = 0
extrato = []
valor_limite = 500
numero_saques = 0
#LIMITE_SAQUE = 3
nova_operacao = 'S'
opcao = 0 
saldo = 0


print(menu,end='\n')


while nova_operacao == 'S':
    
    opcao = int(input('Informe a opção desejada: ')) 

    if opcao == 1: 

        deposito = float(input('Informe o valor a ser depositado: '))

        if deposito > 0:
            print()
            print(f'Depósito confirmado de R${deposito:.2f}')         

            extrato.append(f'Depósito de R${deposito:.2f}')         

            saldo += deposito          

            print()
            nova_operacao = input('Deseja realizar uma nova_operacao [S] Sim | [N] Não? ')

            if nova_operacao == 'N':
                    print('Obrigado por utilizar nosso sistema')   
                    break   
        else:
            print('Valor informado é inválido!')

        print()               
        

    elif opcao == 2:
        saque = int(input('Informe o valor do saque: '))

        if saque > 500:
            print('Valor máximo de saque ultrapassado')                

            print()
            nova_operacao = input('Deseja realizar uma nova_operacao [S] Sim | [N] Não? ')        

        elif numero_saques < 3 and saque <= 500:                  

            print(f'Saque confirmado de R${saque:.2f}')  
            
            extrato.append(f'Saque de R${saque:.2f}')
            
            numero_saques += 1
            
            print()
            nova_operacao = input('Deseja realizar uma nova_operacao [S] Sim | [N] Não? ')

            saldo -= saque  

            if nova_operacao == 'N':
                print('Obrigado por utilizar nosso sistema')   
                break   

            print()        
        
        else:
            print('Você atingiu o número máximo de saques diários!')

            print()

            nova_operacao = input('Deseja realizar uma nova_operacao [S] Sim | [N] Não? ')

            if nova_operacao == 'N':
                print('Obrigado por utilizar nosso sistema')   
                break   

            print()
            
        
    elif opcao == 3:      
        
        print(' Extrato '.center(80,'#'))

        if extrato == []:
            print('Não foram realizadas movimentações!')
        else:
            print()
            for valor in extrato:
                print(valor,end='\n')
            
            print()
            print(f'Seu saldo é de {saldo:.2f}')
            print(''.center(80,'#'))      

            nova_operacao = 'N'      

            print()
                
            nova_operacao = input('Deseja realizar uma nova_operacao [S] Sim | [N] Não? ')
            
            if nova_operacao == 'N':
                print('Obrigado por utilizar nosso sistema')   
                break   

            print()

    elif opcao == 4:        
        print('Obrigado por utilizar nosso sistema')   
        break            


    else:
        print('Opção inválida!')     
      



