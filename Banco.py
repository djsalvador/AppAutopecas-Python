#importando módulo
import psycopg2

class Banco(object):
    def __init__(self):
        self.conexao = psycopg2.connect(host='localhost', database = 'Autopecas' , user="postgres", password="postgres")
        self.createTable()
    
    def createTable(self):
        c = self.conexao.cursor()
    
        c.execute(""" create table 
            if not exists pecas (
                codigo integer primary key,
                nome text,
                quantidade integer,
                preco integer
                )
                """
                )
        self.conexao.commit()
        c.close()