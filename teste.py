cadastro = []
#---CADASTRO---
def cadastrar_usuario():
    print("CADASTRAR NOVO USUÁRIO")
    nome = input("Digite seu nome: ")
    while True:
        idade = int(input("Digite sua idade: "))
        if idade < 18:
            print("\033[31mVocê precisa ser maior de idade para se cadastrar!\033[0m")
            continue
        else:
            break
 
    email = input("Digite seu Email: ")
    senha = input("Crie sua senha: ")
    usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": senha,
        "saldo": 0.0
    }
    print(
        f"\033[32mCadastro realizado com sucesso! "
        f"Nome: {nome}, Idade: {idade}, Email: {email}\033[0m"
    )
 
    cadastro.append(usuario)
    menu_principal(usuario)
 
#---LOGAR---
def logar_na_conta():
    print("INICIAR SESSÃO")
    email = input("Digite seu Email: ")
    senha = input("Digite sua senha: ")
    for usuario in cadastro:
        if usuario["email"] == email and usuario["senha"] == senha:
            print(f"\033[32mLogin realizado com sucesso! Bem-vindo, {usuario['nome']}!\033[0m")
            return usuario
 
    print("\033[31mEmail ou senha incorretos!\033[0m")
    return None
 
#---DEPÓSITO---
def depositar_dinheiro(usuario):
    print("===DEPOSITAR DINHEIRO===")
    deposito = float(input("Digite o valor que você irá depositar no banco: "))
    if deposito > 0:
        usuario["saldo"] += deposito
        print(
            f"\033[32mDepósito de R${deposito:.2f} realizado com sucesso!\033[0m"
        )
        print(f"Seu saldo atual é de R${usuario['saldo']:.2f}")
    else:
        print("\033[31mO valor do depósito deve ser maior que zero!\033[0m")
        return
 
#---SAQUE----
def sacar_dinheiro(usuario):
    print("===SACAR DINHEIRO===")
    saque = float(input("Digite o valor que você irá sacar: "))
    if saque <= 0:
        print("\033[31mO valor do saque deve ser maior que zero!\033[0m")
        return
    elif saque > usuario["saldo"]:
        print("\033[31mSaldo insuficiente!\033[0m")
        return
    else:
        usuario["saldo"] -= saque
        print(
            f"\033[32mSaque de R${saque:.2f} realizado com sucesso!\033[0m"
        )
        print(f"Seu saldo atual é de R${usuario['saldo']:.2f}")
 
#---EMPRÉSTIMO---
def solicitar_emprestimo(usuario):
    print("===SOLICITAR EMPRÉSTIMO===")
    emprestimo = float(input("Digite o valor do empréstimo desejado: "))
    if emprestimo <= 0:
        print("\033[31mO valor do empréstimo deve ser maior que 0!\033[0m")
        return solicitar_emprestimo
    elif emprestimo > 10000:
        print("\033[31mNão aceitamos empréstimos nesse valor!\033[0m")
        return solicitar_emprestimo
    else:
        usuario["saldo"] += emprestimo
        print("\033[32mEmpréstimo aceito e realizado com sucesso!\033[0m")
 
#---MUDAR A SENHA---
print("===MUDAR SUA SENHA===")
def mudar_senha(usuario):
    senha = input("Digite sua nova senha: ")
    usuario["senha"] = senha
 
    print("\033[32mSenha alterada com sucesso!\033[0m")
 
#---MENU PRINCIPAL---
def menu_principal(usuario):
    while True:
        print(f"\033[34m=====BEM VINDO AO BANCO VERCARO, {usuario['nome']}!=====\033[0m")
        print(f"Seu saldo é de: {usuario['saldo']}")
        print("opções:")
        print("1- Depositar dinheiro")
        print("2- Sacar dinheiro")
        print("3- Solicitar Empréstimo")
        print("4- Trocar de senha")
        print("5- Sair")
        opcao = int(input("Digite oque deseja fazer: "))
 
        if opcao == 1:
            depositar_dinheiro(usuario)
        elif opcao == 2:
            sacar_dinheiro(usuario)
        elif opcao == 3:
            solicitar_emprestimo(usuario)
        elif opcao == 4:
            mudar_senha(usuario)
        elif opcao == 5:
            print("Saindo da conta...")
            return
        else:
            print("\033[0mDigite uma opção váilida\033[0m")    
            return menu_entrar()
 
#---MENU DE ENTRADA---
def menu_entrar():
    while True:
        print("\033[34m=====BANCO VERCARO=====!\033[0m")
        print("1- Cadastro")
        print("2- Log-in")
        print("3- Sair")
        opcao_entrada = int(input("Oque deseja fazer? "))
        if opcao_entrada == 1:
            cadastrar_usuario()
            usuario = cadastrar_usuario()
            menu_principal(usuario)
 
        elif opcao_entrada == 2:
            usuario = logar_na_conta()
            if usuario is not None:
                menu_principal(usuario)
        elif opcao_entrada == 3:
            print("Obrigado por utilizar o banco!")
            break
        else:
            print("\033[31mDigite um numero válido!\033[0m")
            return
 
 
#---INICIAR---
menu_entrar()
