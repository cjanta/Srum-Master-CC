import sqlite3


class DB_Component_SQLite:

    table_name_userine = "poll_app_userine"
    table_name_card = "poll_app_card"

    __col_descriptions = {
        f"{table_name_userine}" : "(id, userin_name)",
        f"{table_name_card}" : "(id, question_text, answer_text, category, type)"
    }

    def __init__(self):
        self.db = None
        self.__check_db()

    def __check_db(self):
        if not self.db:
            self.db = sqlite3.connect("quiz_project/db.sqlite3")

    def name_to_col_description(self,table_name :str):
        return self.__col_descriptions.get(table_name)
    
    def read_next_index(self, table_name):
        self.__check_db()
        c = self.db.cursor()
        c.execute(f"SELECT * FROM {table_name}")
        datasets = c.fetchall()
        max_id = 0
        for data in datasets:
            if data[0] > max_id : 
                max_id = data[0]         
        return  max_id +1

    def insert_userine(self, userine_name :str):
        self.__check_db()
        table_name = self.table_name_userine
        next_id = self.read_next_index(table_name)    
        self.db.cursor().execute \
        (f"INSERT INTO {table_name} {self.name_to_col_description(table_name)} VALUES ('{next_id}', '{userine_name}')")
        self.db.commit()
        return self
    
    def insert_card(self, question_text :str, answer :str, category :str, type :str):
        self.__check_db()
        table_name = self.table_name_card
        next_id = self.read_next_index(table_name)    
        self.db.cursor().execute \
        (f"INSERT INTO {table_name} {self.name_to_col_description(table_name)} VALUES ('{next_id}', '{question_text}', \
            '{answer}', '{category}', '{type}' )")
        self.db.commit()
        return self

    def read_table(self, table_name :str):
        self.__check_db()
        c = self.db.cursor()
        c.execute(f"SELECT * FROM {table_name}")   
        datasets = c.fetchall()
        for data in datasets:
            print(data) 
        return self
    
    def force_db_close(self):
        if self.db:
            self.db.close()
            self.db = None
            print("Conncetion to db closed by force.")
    
    def __del__(self):
        if self.db:
            self.db.close()
            print("Conncetion to db closed.")
        