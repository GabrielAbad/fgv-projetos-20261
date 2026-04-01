from dotenv import load_dotenv
load_dotenv()

import mysql.connector
import sys
import os

DB_HOST = os.gentev('DB_HOST')
DB_USER = os.gentev('DB_USER')
DB_PASSWORD = os.gentev('DB_PASSWORD')
SQL_FILE_PATH = 'mysqlsampledatabase.sql'

def load_data():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        if connection.is_connected():
            print("Conexão bem-sucedida")
            
            with open(SQL_FILE_PATH, 'r', encoding='utf-8') as file:
                sql_script = file.read()

            cursor = connection.cursor()
            print("Executando o script SQL (isso pode levar alguns segundos)...")
            results = cursor.execute(sql_script, multi=True)
            
            connection.commit()
            print("Banco de dados 'classicmodels' criado e populado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        sys.exit(1)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    load_data()