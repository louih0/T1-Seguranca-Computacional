from viginere import attack, cipher, decipher

menu = 0
while menu != 4:
    file = input("Digite o nome do arquivo da cifra/mensagem(deve estar na pasta do projeto): ")

    with open (file) as file:
        text = file.read()
    try:
        menu = int(input(
            "Digite a função que deseja acessar do código:\n\
    1 - Cifrar mensagem(com chave)\n\
    2 - Decifrar mensagem(com chave)\n\
    3 - Ataque de recuperação de senha(decifrar mensagem sem chave)\n\
    4 - Sair\n"))
    except: # menu not int
        menu = 0
    if (menu == 1 or menu == 2): # menu com chave
        key = input("Digite a chave: ")
    match menu:
        case 1: cipher(key, text)
        case 2: decipher(key, text)
        case 3: attack(text)
        case 4: pass
        case _: print("\nValor inválido. Digite novamente:")
    if (menu >= 1 and menu <= 3):
        sair = input("Deseja sair?(s/n) ")
        if sair.lower() == 's':
            menu = 4
        elif sair.lower() != 'n':
            print("\nCaractere inválido.")
print("Obrigado por acessar o programa. Volte sempre!")