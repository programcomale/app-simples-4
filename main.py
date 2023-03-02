#----------Lista e Dicionário--------------------------------------------------------------------------------------
funcionarios = list()
funcionario = dict()
#----------Funções-------------------------------------------------------------------------------------------------
#----------INÍCIO Função Cadastrar Funcionários--------------------------------------------------------------------------------
def cadastrar_funcionario(id):
    while True:
        print('Você selecionou a opção de Cadastrar Peça')
        print(f"O ID do Funcionário é: {id :0>4}")
        nome = str(input("Nome: ")).strip()
        id = int(input("ID: "))
        setor = str(input("Setor: ")).strip()
        salario = int(input("Salário: "))
        funcionario = {"Nome": nome,
                       "ID": id,
                       "Setor": setor,
                       "Salário": salario,
                       }
        funcionarios.append(funcionario.copy())
        while True:
            pergunta = str(
                input("Gostaria de cadastrar mais um funcionario (S/N): ")).upper()[0]
            if pergunta in "SN":
                break
            print("Opção inválida, por favor responda com S ou N.")
        if pergunta == "N":
            break
#----------FIM Função Cadastrar Funcionários--------------------------------------------------------------------------------


#----------INÍCIO Função Consultar Funcionários--------------------------------------------------------------------------------
def consultar_funcionarios():
    while True:
        try:
            print("MENU DE CONSULTA DE FUNCIONÁRIOS")
            consultar = int(input("Entre com a opção desejada\n1- Consultar Todos os Funcionários\n2- Consultar Funcionários por ID\n3- Consultar Funcionários por Setor\n4- Retornar\n-->"))
            if consultar == 1:
                print("-=" * 30)
                for funcionario in funcionarios:
                    for key, value in funcionario.items():
                        print(f"{key} : {value}")
                    print("-=" * 30)
            elif consultar == 2:
                print("Você Selecionou a Opção Consultar Funcionários por ID")
                entrada = int(input("Digite o ID: "))
                print("-=" * 30)
                for funcionario in funcionarios:
                    if (funcionario["ID"] == entrada):
                        for key, value in funcionario.items():
                            print(f"{key} : {value}")
                        print("-=" * 30)
            elif consultar == 3:
                print("Você Selecionou a Opção Consultar Funcionários por Setor")
                entrada = input("Digite o Setor: ")
                print("-=" * 30)
                for funcionario in funcionarios:
                    if (funcionario["Setor"] == entrada):
                        for key, value in funcionario.items():
                            print(f"{key} : {value}")
                        print("-=" * 30)
            elif consultar == 4:
                break
            else:
                print("Opção inválida")
                continue
        except ValueError:
            print("Escolha uma opção válida")
            continue
#----------FIM Função Consultar Funcionários--------------------------------------------------------------------------------


#----------INÍCIO Função Remover Funcionários--------------------------------------------------------------------------------
def remover_funcionario():
    print("MENU REMOVER FUNCIONÁRIO")
    entrada = int(input("Digite o ID do Funcionário a ser removido: "))
    for funcionario in funcionarios:
        if (funcionario["ID"] == entrada):
            funcionarios.remove(funcionario)
    else:
        print("Funcionário removido")
#----------FIM Função Remover Funcionários--------------------------------------------------------------------------------


#----------PROGRAMA PRINCIPAL----------------------------------------------------------------------------------------------
print("Boas-vindas ao Controle de Funcionários do Alessandro Aguiar da Silva")
contadorFuncionarios = 0
while True:
    try:
        opcao = int(input("Digite a opção desejada:\n1- Cadastrar Funcionários\n2- Consultar Funcionários\n3- Remover Funcionários\n4- Sair\n-->"))
        if opcao == 1:
            contadorFuncionarios = contadorFuncionarios + 1
            cadastrar_funcionario(contadorFuncionarios)
        elif opcao == 2:
            consultar_funcionarios()
        elif opcao == 3:
            remover_funcionario()
        elif opcao == 4:
            print("Programa Finalizado")
            break
        else:
            print("Digite uma opção válida")
            continue
    except ValueError:
        print("Opção inválida.")