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
        

    def find_by_id(self, livro_id):
        conn = get_connection()
        try:
            cursor = conn.execute("SELECT * FROM livro WHERE id = ?", (livro_id,))
            linha = cursor.fetchone()
            
            if linha is None:
                return None
            
            return Entity(
                id = linha["id"],
                titulo = linha["titulo"],
                autor = linha["autor"],
                lido = bool(linha["lido"])
                )
            
        finally:
            conn.close()
        # Consultar pelo ID

    def update(self, livro):
        conn = get_connection()
        
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE livro SET titulo = ?, autor = ? WHERE id = ?",
                (livro.titulo, livro.autor, livro.id)
                )
            conn.commit()
        finally:
            conn.close()
        # Atualizar

    def delete(self, livro_id):
        conn = get_connection()
        
        try:
            conn.execute("DELETE FROM livro WHERE id = ?", (livro_id,))
            conn.commit()
            
        finally:
            conn.close()
        
        
        pass