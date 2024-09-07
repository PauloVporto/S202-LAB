from database import Database
from booksModel import BooksModel

db = Database(database="relatorio_5", collection="books")
book_model = BooksModel(database = db)



while True:
        # Exibindo as opções do menu
        print("\n--- MENU ---")
        print("1. Criar Livro")
        print("2. Ler Livro por ID")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("0. Sair")

        # Solicitando a escolha do usuário
        choice = input("Escolha uma opção: ")

        # Executando a operação correspondente à escolha do usuário
        if choice == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = int(input("Digite o ano do livro: "))
            preco = float(input("Digite o preço do livro: "))
            book_model.create_livro(titulo, autor, ano, preco)
        elif choice == "2":
            id_livro = input("Digite o ID do livro: ")
            book_model.read_livro_by_id(id_livro)
        elif choice == "3":
            id_livro = input("Digite o ID do livro que deseja atualizar: ")
            titulo = input("Digite o novo título do livro: ")
            autor = input("Digite o novo autor do livro: ")
            ano = int(input("Digite o novo ano do livro: "))
            preco = float(input("Digite o novo preço do livro: "))
            book_model.update_livro(id_livro, titulo, autor, ano, preco)
        elif choice == "4":
            id_livro = input("Digite o ID do livro que deseja deletar: ")
            book_model.delete_livro(id_livro)
        elif choice == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

