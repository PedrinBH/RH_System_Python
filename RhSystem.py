# Importations
import os

# Variaveis
funcionarios = [{'Name': 'Pedro', 'Setor': 'RH', 'Salário': 'R$456'}, 
{'Name': 'Lucas', 'Setor': 'RH', 'Salário': 'R$1245'}, 
{'Name': 'Carol', 'Setor': 'DP', 'Salário': 'R$3214'}]

# Funções


def adicionar_funcionario(funcionarios):
    try:

        nome = input('Digite o nome para cadastro: (String) \n-->')

        if not funcionarios:
            setor = input('Digite o setor que '+nome +
                          ' trabalhará: (String) \n-->')

            salario = input('Digite o salário que '+nome +
                            ' receberá: (Integer) \n-->')
            salario = 'R$'+salario
            funcionarios.append({"Name": str(nome), "Setor": str(setor),
                                'Salário': salario})
            return funcionarios
        else:
            for i in funcionarios:
                if i['Name'] == nome:
                    print('Usuário Já Cadastrado')
                    return funcionarios

            setor = input('Digite o setor que '+nome+' trabalhará: \n-->')

            salario = input('Digite o salário que '+nome+' receberá: \n-->')

            funcionarios.append({"Name": str(nome), "Setor": str(setor),
                                'Salário': str(salario)})
            return funcionarios
    except Exception as err:
        print(err)


def remover_funcionario(funcionarios):
    try:
        # adicionar consultar () antes
        consultar_Todos(funcionarios)
        remocao = int(input(
            'Insira o id  do Funcionario que deseja remover: \n-->'))

        del funcionarios[remocao]
        return funcionarios
    except Exception as err:
        print('\n', err)


def consultar_Todos(funcionarios):

    print('### LISTA DE FUNCIONARIOS CADASTRADOS ###\n')
    posicao = -1

    if not funcionarios:
        return print('Lista Vazia!')

    for i in funcionarios:
        posicao = posicao+1
        print('ID ', (posicao), '° ', i)


def consultar_By_Id(funcionarios):
    cod = int(input('Digite o ID para Consulta: \n-->'))
    if funcionarios[cod] in funcionarios:
        print('\nFuncionário', cod, '° Encontrado --> ', funcionarios[cod])
        return
    else:
        print('Funcionário Não Encontrado!\n')
        return
    print('\nFuncionário Encontrado \n-->', funcionarios[cod])


def consultar_By_Setor(funcionarios):
    setor = str(
        input('\nDigite o setor para consultar quem trabalha nele: \n-->'))
    funcionou = False
    idx = 0
    for i in funcionarios:
        if i['Setor'] == setor:
            idx = idx+1
            print(idx, '° Funcionario encontrado --> ', i['Name'])
            funcionou = True

    if funcionou == False:
        print('Sem funcionários no setor')
        return
    elif funcionou == True:
        return


# Execução
try:
    menu = 1
    while (menu != 0):
        menu_text = '\n### Menu - Sistema RH ###\n-- Digite o número da ação desejada --\n1 - Adicionar Funcionario\n2 - Remover\n3 - Consultar\n0 - Sair\n'
        menu = int(input(menu_text+'Digite a opção desejada: (integer) \n-->'))
        if menu == 1:  # Adicionar
            print('\n')
            funcionarios = adicionar_funcionario(funcionarios)
            print('\n')
            print('\n', consultar_Todos(funcionarios))
        elif menu == 2:  # Remover
            funcionarios = remover_funcionario(funcionarios)
            print('\n')
            consultar_Todos(funcionarios)
        elif menu == 3:  # Consultar
            nav2 = 1
            while nav2 != 0:
                nav2 = int(input(
                    '\n Função Consultar - Escolha a opção desejada:\n0 - Voltar \n1 - Consultar Todos Funcionarios\n2 - Consultar Por ID\n3 - Consultar por Setor\n-->'))
                if nav2 == 1:  # Consultar Todos Funcionarios
                    print(consultar_Todos(funcionarios))
                elif nav2 == 0:  # Voltar
                    i = 0
                elif nav2 == 2:  # Consultar By Id
                    print(consultar_By_Id(funcionarios))
                elif nav2 == 3:  # Consultar By Setor
                    print(consultar_By_Setor(funcionarios))
        elif menu == 0:  # sair
            menu = 0
            SystemExit()

except Exception as err:
    print('ERRO PARCEIRO!\n', err)
