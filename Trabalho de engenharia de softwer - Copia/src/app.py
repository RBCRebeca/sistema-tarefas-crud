# app.py

from logic import (
    create_note_logic,
    list_notes_logic,
    update_note_logic,
    delete_note_logic
)

def menu():
    print("\n=== SISTEMA DE ANOTAÇÕES ===")
    print("1 - Criar anotação")
    print("2 - Listar anotações")
    print("3 - Editar anotação")
    print("4 - Excluir anotação")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        texto = input("Digite a anotação: ")
        create_note_logic(texto)
        print("Anotação criada com sucesso!")

    elif opcao == "2":
        notes = list_notes_logic()
        if not notes:
            print("Nenhuma anotação cadastrada.")
        else:
            for i, note in enumerate(notes):
                print(f"{i} - {note['text']}")

    elif opcao == "3":
        index = int(input("Digite o índice da anotação: "))
        novo_texto = input("Novo texto: ")
        if update_note_logic(index, novo_texto):
            print("Anotação atualizada!")
        else:
            print("Índice inválido!")

    elif opcao == "4":
        index = int(input("Digite o índice da anotação: "))
        if delete_note_logic(index):
            print("Anotação removida!")
        else:
            print("Índice inválido!")

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
