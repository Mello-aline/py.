import json 

arquivo cadastros = "cadastros.json"

def exibir_menu():
print("\n ---- MENU CADASTRO ----")
print("1 - cadastrar pessoas")
print("2 - ver cadastros")
print("3 - sair")
print("--------------------")

def salvar_cadastros (cadastros):
    with open (arquivo_cadastros, "w", encoding="utf-8")
        json.dump(cadastros, arquivos, indent=4, ensure_ascil=false)

def carregar_cadastros();
    try:
        with open(arquivo_cadastros, "r", encording="utf-8") as arquivo:
            return json.load(arquivo)
    except(FileNotFoundError, json.JSONDecodeError):
        return[]
    
def cadastrar_pessoas(cadastros):
    nome = input("nome:  ")
    idade = input("idade:  ")
    turma = input("turma:  ")
    curso = input("curso:  ")
    
    cadastros.appeend({"nome": nome,"idade": idade,"turma": turma,"curso": curso,})
    salvar_cadastros(cadastros)
    print("cadastro realizado com sucesso!")

def ver cadastros(cadastros):
    if not cadaastros:
        print("\nNenhum cadastro realizado.")
    else:
        print("\n===== LISTA DE CADASTROS =====")
        for i, pessoa in enumerate( cadastros, 1):
            print(f"{i}. nome:{pessoa['nome']}, idade:{pessoa['idade']}, turma:{pessoa['turma']}, curso:{pessoa['curso']}")
            input("\nPressione Enter para Voltar ao menu...")

def main();
    cadastros = carregar_cadastros()
    while true:
        exibir_menu()
        opcao = input("Escolha uma opção:  ")
        if opcao == "1":
            cadastrar_pessoas(cadastros)
        elif opcao == "2":
            ver_cadastros(cadastros)
        elif opcao == "3":
            print ("obrigada por utilizar o sistema de cadastro!")
            break
        else:
            print ("Opção invalida! tente novamente.")

if__name__ == "__main__":
    main()