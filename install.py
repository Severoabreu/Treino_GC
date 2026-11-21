from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        # Criar tabela no banco de dados
        connection.execute("""
            CREATE TABLE IF NOT EXISTS livro(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT,
                lido INTEGER NOT NULL DEFAULT 0
                )
            """)

        # Inserir dados iniciais (OBRIGATÓRIO!!!!)
        cursor = connection.execute("SELECT COUNT(*) FROM livro")
        total = cursor.fetchone()[0]
        
        if total == 0:
            connection.execute(
                "INSERT INTO livro (titulo, autor, lido) VALUES (?, ?, ?)",
                ("Paranormal", "Ronaldo", 0)
                )
            connection.execute(
                "INSERT INTO livro (titulo, autor, lido) VALUES (?, ?, ?)",
                ("Troia", "Rafael", 0)
                )
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")