def imprime_cabecalho():
    print("\n")
    print("######################################################")
    print("  ☆ Olá, seja bem-vindo ao menu inicial do sistema ☆ :) ")
    print("######################################################")

def cadastra_funcionario(funcionarios):
    print("\n")
    print("       Tela de cadastro - funcionário      ")

    ID_funcionario = input("Digite um código de 5 dígitos para ser o identificador do funcionário: ")
    while ID_funcionario == '':
        print("O id nao pode estar em branco, por favor tente novamente ")
        ID_funcionario = input("Digite um código de 5 dígitos para ser o identificador do funcionário: ")
    while len(ID_funcionario) != 5 or not ID_funcionario.isdigit():
        print("O ID deve ter 5 dígitos numéricos, tente novamente")
        ID_funcionario = input("Digite um código de 5 dígitos para ser o identificador do funcionário: ")
        for i, funcionario in enumerate(funcionarios):
            if funcionario[0] == ID_funcionario:
                print("O ID já existe, tente novamente!")
                ID_funcionario = input("Digite um código de 5 dígitos para ser o identificador do funcionário: ")
        
    nome = input("Digite o nome completo do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ").capitalize()
    print("\n")
    print(f"ID:{ID_funcionario}\nNome:{nome}\nCargo:{cargo}")

    novo_funcionario = (ID_funcionario, nome, cargo)
    funcionarios.append(novo_funcionario)
    salvar_funcionarios_em_arquivo(funcionarios)

    print("Funcionário cadastrado com sucesso!")

    print("\n")
    continua_cadastro = input("Pressione 1 para cadastrar novo funcionário\n2 para voltar ao menu do administrador\nDigite a opção: ")
    if continua_cadastro == "1":
        cadastra_funcionario(funcionarios)
    else:
        print("Voltando ao menu do Administrador...")
        menu_admin(funcionarios)

def edita_funcionario(funcionarios):
    print("\n")
    print("Tela de editar cadastro - funcionário")
    funcionario_para_edicao = input("Qual funcionário você pretende editar? Por favor, insira o ID (XXXXX): ")
    funcionario_encontrado = False

    for i, funcionario in enumerate(funcionarios):
        if funcionario[0] == funcionario_para_edicao:
            funcionario_encontrado = True
            print("Funcionário encontrado!")

            print("Escolha o que deseja editar:")
            print("1. Editar ID")
            print("2. Editar Nome")
            print("3. Editar Cargo")
            print("4. Editar Todos os Dados")
            print("5. Voltar ao menu do Administrador")

            opcao = int(input("Opção desejada: "))

            if opcao == 1:
                novo_ID_funcionario = input("Digite o novo ID do funcionário (XXXXX): ")
                while len(novo_ID_funcionario) != 5 or not novo_ID_funcionario.isdigit():
                    print("O ID deve ter 5 dígitos numéricos, tente novamente")
                    novo_ID_funcionario = input("Digite um código de 5 dígitos para ser o identificador do funcionário: ")
                    for i, funcionario in enumerate(funcionarios):
                        if funcionario[0] == novo_ID_funcionario:
                            print("O ID já existe, tente novamente!")
                            novo_ID_funcionario = input("Digite um código de 5 dígitos para ser o identificador do funcionário: ")
                funcionario = list(funcionario)
                funcionario[0] = novo_ID_funcionario
                funcionarios[i] = tuple(funcionario)

            elif opcao == 2:
                novo_nome_funcionario = input("Digite o novo nome do funcionário: ")
                funcionario = list(funcionario)
                funcionario[1] = novo_nome_funcionario
                funcionarios[i] = tuple(funcionario)

            elif opcao == 3:
                novo_cargo_funcionario = input("Digite o novo cargo do funcionário: ").capitalize()
                funcionario = list(funcionario)
                funcionario[2] = novo_cargo_funcionario
                funcionarios[i] = tuple(funcionario)

            elif opcao == 4:
                novo_ID_funcionario = input("Digite o novo ID do funcionário (XXXXX): ")
                novo_nome_funcionario = input("Digite o novo nome do funcionário: ")
                novo_cargo_funcionario = input("Digite o novo cargo do funcionário: ").capitalize()
                novo_funcionario = (novo_ID_funcionario, novo_nome_funcionario, novo_cargo_funcionario)
                funcionarios[i] = novo_funcionario

            elif opcao == 5:
                menu_admin(funcionarios)

            print("Dados editados com sucesso!")
            salvar_funcionarios_em_arquivo(funcionarios)

            continua_edicao = input("Pressione 1 para continuar no menu EDITA FUNCIONARIO ou tecle 5 para sair: ")
            if continua_edicao == "5":
                print("Voltando ao menu do Administrador...")
                menu_admin(funcionarios)
            else:
                edita_funcionario(funcionarios)

    if not funcionario_encontrado:
        print("Funcionário não encontrado.")
        edita_funcionario(funcionarios)

def remove_funcionario(funcionarios):
    ID_funcionario = input("Digite o ID do funcionário que deseja remover: ")
    funcionario_encontrado = False

    for funcionario in funcionarios:
        if funcionario[0] == ID_funcionario:
            funcionarios.remove(funcionario)
            print(f"Funcionário com ID {ID_funcionario} removido com sucesso.")
            funcionario_encontrado = True
            salvar_funcionarios_em_arquivo(funcionarios)
            continua_removendo = input("Tecle 1 para remover outro funcionário?\n 2 para retornar ao 'MENU ADM':")
            if continua_removendo == "1":
                remove_funcionario(funcionarios)
            else:
                menu_admin(funcionarios)

    if not funcionario_encontrado:
        print("Funcionário não encontrado.")
        remove_funcionario(funcionarios)

def menu_admin(funcionarios):
    print("\n")
    print("Olá! Seja bem-vindo ao menu do Administrador")
    print("   1. Cadastrar novo funcionário")
    print("   2. Editar Funcionário")
    print("   3. Remover Funcionário")
    print("   4. Sair")

    opcao = int(input("Opção desejada: "))
    if opcao == 1:
        cadastra_funcionario(funcionarios)
    elif opcao == 2:
        edita_funcionario(funcionarios)
    elif opcao == 3:
        remove_funcionario(funcionarios)
    elif opcao == 4:
        print("Saindo do programa...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu_admin(funcionarios)

def salvar_funcionarios_em_arquivo(funcionarios):
    with open('Funcionarios.txt', 'w') as arquivo:
        for funcionario in funcionarios:
            arquivo.write(f"ID: {funcionario[0]}\n")
            arquivo.write(f"Nome: {funcionario[1]}\n")
            arquivo.write(f"Cargo: {funcionario[2]}\n")
            arquivo.write("\n")  # Pra separar os funcionários

def carregar_funcionarios_do_arquivo():
    try:
        with open('Funcionarios.txt', 'r') as arquivo:
            funcionarios = []
            dados = arquivo.read().split('\n')
            i = 0
            while i < len(dados) - 2:  # Reduz o limite em 2
                ID_funcionario = dados[i].split(": ")[1]
                nome = dados[i + 1].split(": ")[1]
                cargo = dados[i + 2].split(": ")[1]
                funcionarios.append((ID_funcionario, nome, cargo))
                i += 4  # Aumenta o índice em 4
            return funcionarios
    except FileNotFoundError:
        return []


def tela_login():
    imprime_cabecalho()
    print("\n")
    login = input("Login: ")
    senha = input("Senha: ")
    if login == "admin" and senha == "admin1234":
        funcionarios = carregar_funcionarios_do_arquivo()
        menu_admin(funcionarios)
    else:
        print("Senha ou Login incorretos, tente novamente!")
        tela_login()

if __name__ == "__main__":
    tela_login()
