from database.connection import get_connection
from entities.entity import Entity

class DAOEntity:

    def create(self, livro):
        conn = get_connection()
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO livro (titulo, autor, lido) VALUES (?, ?, ?)",
                (livro.titulo, livro.autor, int(livro.lido))
                )
            conn.commit()
            return cursor.lastrowid
        finally :
            conn.close()

    def find_all(self):
        conn = get_connection()
        
        try:
            cursor = conn.execute("SELECT * FROM livro")
            linhas = cursor.fetchall()
            
            livros = []
            for linha in linhas:
                livro = Entity(
                    id = linha["id"],
                    titulo = linha["titulo"],
                    autor = linha["autor"],
                    lido = bool(linha["lido"])
                )
                
                livros.append(livro)
            
            return livros
        
        finally:
            conn.close()
        # Consultar todas as entidades
        

    def find_by_id(self, task_id):
        # Consultar pelo ID
        pass

    def update(self, task):
        # Atualizar
        pass

    def delete(self, task_id):
        # Excluir
        pass