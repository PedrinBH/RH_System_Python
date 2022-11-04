
# Software Controle de Funcionários #

O Script RH System apresenta um software para controle de funcionários de forma automatizada com phyton. Projeto com fins educacionais.

# Tecnologias Utilizadas #
- PHYTON (3.11)


### Preparando ambiente 

Não utilizaremos bibliotecas especiais, apenas uma importação.
para utilizar essa importação basta adicionar o seguinte código no inicio do arquivo.
```Python
# Importations
import os
```
### Como Executar Arquivo Main.py? ###

Para executar as funções `def()` é só chamar ela na área de execuções do arquivo.
```Python
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
```

## Versionamento

- 1.0.0.0 (beta)