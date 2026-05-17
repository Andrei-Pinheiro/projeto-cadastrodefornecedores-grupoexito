import sqlite3


def init_database():
    connection = sqlite3.connect("database.db")

    with open("database/schema.sql", "r", encoding="utf-8") as file:
        connection.executescript(file.read())

    connection.close()

    print("Banco de dados criado com sucesso!")


if __name__ == "__main__":
    init_database()
