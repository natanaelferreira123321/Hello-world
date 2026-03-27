import sqlite3
import os

def criar_estrutura():
    # Conecta ao arquivo (se não existir, o SQLite cria na hora)
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Cria a tabela de livros (Igual ao seu projeto real)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER
        )
    ''')

    # Insere um dado inicial para termos o que ver depois
    cursor.execute("INSERT INTO livros (titulo, autor, ano) VALUES ('Dom Casmurro', 'Machado de Assis', 1899)")
    
    conn.commit()
    conn.close()
    print("Sucesso: Banco de dados 'biblioteca.db' criado e populado!")

if __name__ == "__main__":
    criar_estrutura()
    
    # Check de segurança para a Pipeline
    if os.path.exists('biblioteca.db'):
        print("Confirmação: Arquivo gerado com sucesso.")
    else:
        raise FileNotFoundError("Erro crítico: O arquivo do banco não foi gerado!")
