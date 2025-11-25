lista_funcionarios = []      #Lista de Funcionários, inicialmente vazia
id_global = 5178226          #Id inicial, começando pelo meu número do RU

#Função referente ao cadastro de novos funcionários
def cadastrar_funcionario(id_global):
    global lista_funcionarios

    print("-"*50)
    print("-" * 11, end=" ")
    print("MENU CADASTRAR FUNCIONÁRIO", end=" ")
    print("-" * 11)

    #Coleta de dados para o cadastro
    print(f"Id do Funcionário: {id_global}")
    nome = input("Por favor entre com o nome do Funcionário: ").strip()
    setor = input("Por favor entre com o setor do Funcionário: ").strip()
    salario = float(input("Por favor entre com o salário do funcionário: "))

    #Criação do dicionário dos dados coletados
    dados = {"id": id_global, "nome": nome, "setor": setor, "salario": salario}
    lista_funcionarios.append(dados.copy())       #Adiciona o dicionário à lista
    return id_global

#Função referente a consultar funcionários cadastrados
def consultar_funcionarios():
    global lista_funcionarios

    while True:
        print("-" * 50)
        print("-" * 11, end=" ")
        print("MENU CONSULTAR FUNCIONÁRIO", end=" ")
        print("-" * 11)
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Funcionários")
        print("2 - Consultar Funcionário por id")
        print("3 - Consultar Funcionário(s) por setor")
        print("4 - Retomar ao Menu Principal")
        opcao = input(">>").strip()

        if opcao == "1":      #Exibe todos funcionários cadastrados
            print("-" * 20)
            if not lista_funcionarios:
                print("Nenhum funcionário cadastrado")
            else:
                for f in lista_funcionarios:
                    print(f"ID: {f['id']}")
                    print(f"Nome: {f['nome']}")
                    print(f"Setor: {f['setor']}")
                    print(f"Salário: R${f['salario']:.2f}\n")
            print("-" * 20)

        elif opcao == "2":   #Consulta o funcionário pelo ID
            try:
                id_busca = int(input("Digite o ID do funcionário: "))
            except ValueError:
                print("ID inválido (precisa ser número inteiro).\n")
                continue

            #Busca e exibe o funcionário de acordo com o ID
            encontrado = False
            for f in lista_funcionarios:
                if f["id"] == id_busca:
                    print("-" * 20)
                    print(f"ID: {f['id']}")
                    print(f"Nome: {f['nome']}")
                    print(f"Setor: {f['setor']}")
                    print(f"Salário: R${f['salario']:.2f}\n")
                    print("-" * 20)
                    print("-" * 50)

                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.\n")

        elif opcao == "3":   #Consulta o funcionário pelo setor
            setor_busca = input("Digite o setor do(s) funcionário(s): ").strip()
            encontrados = []
            for f in lista_funcionarios:
                if f["setor"] == setor_busca:
                    encontrados.append(f)

            if not encontrados:
                print("Nenhum funcionário encontrado neste setor.\n")
            else:
                for f in encontrados:
                    print(f"ID: {f['id']}")
                    print(f"Nome: {f['nome']}")
                    print(f"Setor: {f['setor']}")
                    print(f"Salário: R${f['salario']:.2f}\n")

        elif opcao == "4":      #Retorna ao menu principal
            return

        else:                   #Validação para não digitar errado
            print("Opção inválida.\n")


def remover_funcionario():              #Função referente a remoção de funcionário pelo ID
    global lista_funcionarios

    while True:
        print("-" * 50)
        print("-" * 23, end=" ")
        print("MENU REMOVER FUNCIONÁRIO", end=" ")
        print("-" * 23)
        try:
            id_remover = int(input("Digite o ID do funcionário a ser removido: "))
        except ValueError:
            print("Id inválido!")
            continue

        #Busca e remove o funcionário de acordo com ID solicitado
        for f in lista_funcionarios:
            if f["id"] == id_remover:
                lista_funcionarios.remove(f)
                print("Funcionário removido com sucesso!\n")
                return

        print("Id inválido! Digite novamente.\n")        #Validação para que o ID seja digitado corretamente



print("Bem-vindo a empresa do Ytalo Gabriel")

#Menu principal
while True:
    print("-" * 50)
    print("-" * 17, end=" ")
    print("MENU PRINCIPAL", end=" ")
    print("-" * 17)
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Funcionários")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")
    opcao = input(">>").strip()

    if opcao == "1":                                      #Chama função de cadastro e atualiza o ID global
        id_global = cadastrar_funcionario(id_global)
        id_global += 1
    elif opcao == "2":
        consultar_funcionarios()                          #Chama a função de consulta
    elif opcao == "3":
        remover_funcionario()                             #Chama a função de remoção
    elif opcao == "4":
        break                                             #Encerra o programa

    else:                                                 #Validação para que seja digitado uma  opção válida
        print("Opção inválida.\n")