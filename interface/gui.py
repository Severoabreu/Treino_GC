from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        
        while True:
            print("\n=== CATÁLOGO DE livros ===")
            print("1 - Cadastrar livro")
            print("2 - Listar livro")
            print("3 - Consultar livro")
            print("4 - Atualizar livro")
            print("5 - Excluir livro")
            print("6 - Marcar livro como lido")
            print("7 - Marcar livro como não assistido")
            print("0 - sair")
            
            opcao = input("Escolha uma opção ").strip()
            
            try:
                if opcao == "1":
                    titulo = input("Nome do livro: ")
                    autor = input("Nome do autor: ")
                    novo_id = self.services.create(titulo, autor)
                    print(f"Livro cadastrado com sucesso! ID gerado: {novo_id}")
                    
                elif opcao == "2":
                    livro = self.services.list()
                    if not livro:
                        print("Não há livros cadastrados no sistema.")
                    else :
                        print("-- Listas de livros --")
                        for f in livro:
                            situacao = "lido" if f.lido else "Não lido"
                            print(f"ID: {f.id} | Título: {f.titulo} | autor: {f.autor} | Situação: {situacao}")
                            
                elif opcao == "3":
                    livro_id = int(input("Informe o ID do livro: "))
                    f = self.services.get(livro_id)
                    situacao = "lido" if f.lido else "Não lido"
                    print(f"ID: {f.id} | Título: {f.titulo} | autor: {f.autor} | Situação: {situacao}")
                
                elif opcao == "4":
                    livro_id = int(input("Informe o ID do livro: "))
                    titulo = input("Novo título do livro: ")
                    autor = input("Novo autor do livro: ")
                    self.services.update(livro_id, titulo, autor)
                    print("Livro atualizado com sucesso!")
                                            
                elif opcao == "5":
                    livro_id = int(input("Informe o ID do livro: "))
                    self.services.delete(livro_id)
                    print("Livro excluído com sucesso!")       
                        
                        
                    
                elif opcao == "0":
                    print("Saindo...")
                    break
                
            except ValueError as erro:
                print(f"Erro: {erro}")
            
            
        # Exibir opções
        # Receber escolha do usuário
        # Chamar os métodos do service