#Apenas a tela de visualização
while True:
    print("==================")
    print("Sitema de Cadastro")
    print("==================")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")
    #Funcionalidades
    #Se o usario digitar o valor 1, vai ser exebido
    # a ação abaixo:
    if (opcao == "1"):
        print("======================")
        print("===Tela de Cadastro===")
        print("======================")
    #se digitar 2, abre a tela de login
    elif(opcao == "2"):
        print("======================")
        print("====Tela de Login=====")
        print("======================")
    #se digitar 3, sai da execução
    elif(opcao == "3"):
        print("Você está saindo do cadastro, até mais!")
        break
    #Se não for nem 1,2 ou 3, mostrar erro e repetir código
    else:
        print("Valor digitado, inválido, use apenas números inteiros do menu")
    