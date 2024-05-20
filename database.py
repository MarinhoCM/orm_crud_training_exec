from mysql.connector import connect


class Mercantil:
    def __init__(self) -> None:
        self.config: dict = {
            "user": "root",
            "password": "",
            "host": "localhost",
            "database": "mercantil",
        }
        self.cnx = connect(**self.config)
        self.cursor = self.cnx.cursor()


class Produtos(Mercantil):
    def __init__(self, table: str) -> None:
        super().__init__()
        self.table = table

    def queries(self) -> dict:
        return {
            "QUERY_SELECT": f"SELECT * FROM {self.table}",
            "QUERY_INSERT_ONE": f"INSERT INTO {self.table} (nome_prod, qtd_prod, preco_prod, desc_prod) VALUES (%s, %s, %s, %s)",
            "QUERY_DELETE_ONE": f"DELETE FROM {self.table} WHERE nome_prod = %s",
            "QUERY_UPDATE_ONE": f"UPDATE {self.table} SET nome_prod = %s, qtd_prod = %s, preco_prod = %s, desc_prod = %s",
        }

    def select_all_from_table(self) -> list:
        query = self.queries()["QUERY_SELECT"]
        self.cursor.execute(query)
        rows = []

        for row in self.cursor.fetchall():
            print(row)
            rows.append(row)

        print(f"{len(rows)} linhas foram afetadas")
        return rows

    def select_one_in_table(self, sort: str | bool=False, **filter):
        query = f"SELECT * FROM {self.table} WHERE"
        for key, value in filter:
            query += f"{key} = {value}"

        if sort:
            query = f"SELECT * FROM {self.table} WHERE {filter} LIKE {sort}"
        else:
            query = f"SELECT * FROM {self.table} WHERE {filter}"

        print(query)
        
        self.cursor.execute(query)
        rows = []

        for row in self.cursor.fetchall():
            print(row)
            rows.append(row)
        
        if len(rows) < 1:
            print("Não foi possivel encontrar a linha especificada")
        else:
            print(f"{len(rows)} linhas foram afetadas")

        return rows


    def insert_in_table(self, obj_list: dict):
        query = self.queries()["QUERY_INSERT_ONE"]
        self.cursor.execute(query, obj_list)
        self.cnx.commit()

    def delete_one_in_table(self, product_name: str):
        query = self.queries()["QUERY_DELETE_ONE"]
        self.cursor.execute(query, (product_name,))
        self.cnx.commit()

    def update_one_in_table(self, obj_list: list, product_name: str):
        query = self.queries()["QUERY_UPDATE_ONE"]
        query += " WHERE nome_prod = %s"
        obj_list.append(product_name)
        self.cursor.execute(query, obj_list)
        self.cnx.commit()

    def close_all(self):
        self.cnx.close()
        self.cursor.close()
