from service.services import Services

class UI:

    def __init__(self, services):
        self.services = services

    def show_principal_menu(self):
        
        while True:
            print("1 - Cadastrar livro")
            print("2 - Listar livro")
            print("3 - Consultar livro")
            print("4 - Atualizar livro")
            print("5 - Excluir livro")
            print("6 - Marcar livro como lido")
            print("7 - Marcar livro como não assistido")
            print("0 - sair")
            
            opcao = input("Escolha uma opção").strip()
            
            try:
                if opcao == "1":
                    titulo = input("Nome do livro: ")
                    autor = input("Nome do autor: ")
                    novo_id = self.services.create(titulo, autor)
                    print(f"Livro cadastrado com sucesso! ID gerado: {novo_id}")
                    
                elif opcao == "0":
                    print("Saindo...")
                    break
                
            except ValueError as erro:
                print(f"Erro: {erro}")
            
            
        # Exibir opções
        # Receber escolha do usuário
        # Chamar os métodos do service