# pip install mysql-connector-python
# pip install pandas

import mysql.connector
import pandas as pd
from mysql.connector import Error

dataframe = pd.DataFrame()


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',          # Altere para o seu host
            user='root',               # Altere para seu usuário
            password='',               # Altere para sua senha
            database='bdlojabolos'          # Altere para seu banco de dados
        )
        if connection.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso.")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def insert_cliente(connection, cpf, nome, email, telefone, endereco):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO clientes (cpf, nome, email, telefone, endereco) VALUES (%s, %s, %s, %s, %s)"
        values = (cpf, nome, email, telefone, endereco)
        cursor.execute(query, values)
        connection.commit()
        print("Cliente inserido com sucesso.")
    except Error as e:
        print(f"Erro ao inserir cliente: {e}")
    finally:
        cursor.close()


def insert_produto(connection, nome, descricao, categoria, preco):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO produtos (nome, descricao, categoria, preco) VALUES (%s, %s, %s, %s)"
        values = (nome, descricao, categoria, preco)
        cursor.execute(query, values)
        connection.commit()
        print("Produto inserido com sucesso.")
    except Error as e:
        print(f"Erro ao inserir produto: {e}")
    finally:
        cursor.close()


def insert_venda(connection, cpf_cliente, produto_id, data_venda, quantidade):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO vendas (cpf_cliente, produto_id, data_venda, quantidade) VALUES (%s, %s, %s, %s)"
        values = (cpf_cliente, produto_id, data_venda, quantidade)
        cursor.execute(query, values)
        connection.commit()
        print("Venda inserida com sucesso.")
    except Error as e:
        print(f"Erro ao inserir venda: {e}")
    finally:
        cursor.close()


def update_cliente(connection, cpf, nome, email, telefone, endereco):
    try:
        cursor = connection.cursor()
        query = "UPDATE clientes SET nome = %s, email = %s, telefone = %s, endereco = %s WHERE cpf = %s"
        values = (nome, email, telefone, endereco, cpf)
        cursor.execute(query, values)
        connection.commit()
        print("Cliente atualizado com sucesso.")
    except Error as e:
        print(f"Erro ao atualizar cliente: {e}")
    finally:
        cursor.close()


def update_produto(connection, id_produto, nome, descricao, categoria, preco):
    try:
        cursor = connection.cursor()
        query = "UPDATE produtos SET nome = %s, descricao = %s, categoria = %s, preco = %s WHERE id = %s"
        values = (nome, descricao, categoria, preco, id_produto)
        cursor.execute(query, values)
        connection.commit()
        print("Produto atualizado com sucesso.")
    except Error as e:
        print(f"Erro ao atualizar produto: {e}")
    finally:
        cursor.close()


def update_venda(connection, id_venda, cpf_cliente, produto_id, data_venda, quantidade):
    try:
        cursor = connection.cursor()
        query = "UPDATE vendas SET cpf_cliente = %s, produto_id = %s, data_venda = %s, quantidade = %s WHERE id_venda = %s"
        values = (cpf_cliente, produto_id, data_venda, quantidade, id_venda)
        cursor.execute(query, values)
        connection.commit()
        print("Venda atualizada com sucesso.")
    except Error as e:
        print(f"Erro ao atualizar venda: {e}")
    finally:
        cursor.close()


def delete_cliente(connection, cpf):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM clientes WHERE cpf = %s"
        values = (cpf,)
        cursor.execute(query, values)
        connection.commit()
        print("Cliente deletado com sucesso.")
    except Error as e:
        print(f"Erro ao deletar cliente: {e}")
    finally:
        cursor.close()


def delete_produto(connection, id_produto):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM produtos WHERE id = %s"
        values = (id_produto,)
        cursor.execute(query, values)
        connection.commit()
        print("Produto deletado com sucesso.")
    except Error as e:
        print(f"Erro ao deletar produto: {e}")
    finally:
        cursor.close()


def delete_venda(connection, id_venda):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM vendas WHERE id_venda = %s"
        values = (id_venda,)
        cursor.execute(query, values)
        connection.commit()
        print("Venda deletada com sucesso.")
    except Error as e:
        print(f"Erro ao deletar venda: {e}")
    finally:
        cursor.close()


def read_data(connection, table):
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        dataframe = pd.DataFrame(rows, columns=columns)
        print(dataframe)
    except Error as e:
        print(f"Erro ao ler dados: {e}")
    finally:
        cursor.close()


def main():
    """Função principal do script."""
    connection = connect_to_database()
    if connection:
        while True:
            print("\nEscolha uma tabela para operar:")
            print("1. Clientes")
            print("2. Produtos")
            print("3. Vendas")
            print("4. Sair\n")
            choice_table = input("Digite o número da tabela: ")

            if choice_table == '1':
                print("\nEscolha uma opção para 'Clientes':")
                print("1. Inserir")
                print("2. Atualizar")
                print("3. Deletar")
                print("4. Ler")
                choice = input("Digite o número da opção: ")

                if choice == '1':
                    cpf = input("Digite o CPF do cliente: ")
                    nome = input("Digite o nome do cliente: ")
                    email = input("Digite o email do cliente: ")
                    telefone = input("Digite o telefone do cliente: ")
                    endereco = input("Digite o endereço do cliente: ")
                    insert_cliente(connection, cpf, nome, email, telefone, endereco)
                elif choice == '2':
                    cpf = input("Digite o CPF do cliente: ")
                    nome = input("Digite o novo nome do cliente: ")
                    email = input("Digite o novo email: ")
                    telefone = input("Digite o novo telefone: ")
                    endereco = input("Digite o novo endereço: ")
                    update_cliente(connection, cpf, nome, email, telefone, endereco)
                elif choice == '3':
                    cpf = input("Digite o CPF do cliente a ser deletado: ")
                    delete_cliente(connection, cpf)
                elif choice == '4':
                    read_data(connection, 'clientes')

            elif choice_table == '2':
                print("\nEscolha uma opção para 'Produtos':")
                print("1. Inserir")
                print("2. Atualizar")
                print("3. Deletar")
                print("4. Ler")
                choice = input("Digite o número da opção: ")

                if choice == '1':
                    nome = input("Digite o nome do produto: ")
                    descricao = input("Digite a descrição do produto: ")
                    categoria = input("Digite a categoria do produto: ")
                    preco = float(input("Digite o preço do produto: "))
                    insert_produto(connection, nome, descricao, categoria, preco)
                elif choice == '2':
                    id_produto = int(input("Digite o ID do produto a ser atualizado: "))
                    nome = input("Digite o novo nome do produto: ")
                    descricao = input("Digite a nova descrição: ")
                    categoria = input("Digite a nova categoria: ")
                    preco = float(input("Digite o novo preço: "))
                    update_produto(connection, id_produto, nome, descricao, categoria, preco)
                elif choice == '3':
                    id_produto = int(input("Digite o ID do produto a ser deletado: "))
                    delete_produto(connection, id_produto)
                elif choice == '4':
                    read_data(connection, 'produtos')

            elif choice_table == '3':
                print("\nEscolha uma opção para 'Vendas':")
                print("1. Inserir")
                print("2. Atualizar")
                print("3. Deletar")
                print("4. Ler")
                choice = input("Digite o número da opção: ")

                if choice == '1':
                    cpf_cliente = input("Digite o CPF do cliente: ")
                    produto_id = int(input("Digite o ID do produto: "))
                    data_venda = input("Digite a data da venda (AAAA-MM-DD): ")
                    quantidade = int(input("Digite a quantidade vendida: "))
                    insert_venda(connection, cpf_cliente, produto_id, data_venda, quantidade)
                elif choice == '2':
                    id_venda = int(input("Digite o ID da venda a ser atualizada: "))
                    cpf_cliente = input("Digite o novo CPF do cliente: ")
                    produto_id = int(input("Digite o novo ID do produto: "))
                    data_venda = input("Digite a nova data da venda (AAAA-MM-DD): ")
                    quantidade = int(input("Digite a nova quantidade vendida: "))
                    update_venda(connection, id_venda, cpf_cliente, produto_id, data_venda, quantidade)
                elif choice == '3':
                    id_venda = int(input("Digite o ID da venda a ser deletada: "))
                    delete_venda(connection, id_venda)
                elif choice == '4':
                    read_data(connection, 'vendas')

            elif choice_table == '4':
                break
            else:
                print("Opção inválida. Tente novamente.")

        connection.close()


if __name__ == "__main__":
    main()
