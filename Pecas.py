from Banco import Banco
 
class Pecas(object):
    def __init__(self, codigo = 0, nome = "", quantidade = 0, preco = 0.0):
        self.info = {}
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    #INSERIR PEÇAS
    def insertPecas(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("insert into pecas(codigo, nome, quantidade, preco) values('" + self.codigo +"','"+ self.nome +"','"+ self.quantidade +"','"+ self.preco +"') ")
            banco.conexao.commit()
            c.close()
            return "Peça cadastrada com sucesso!"
        except:
            return "Ocorreu um erro na inserção da peça"
    
    #ALTERAR PEÇAS
    def updatePecas(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update pecas set codigo = '"+ self.codigo +"' , nome = '"+ self.nome +"' , quantidade = '"+ self.quantidade +"' , preco = '"+ self.preco +"' where codigo = '"+ self.codigo +"' ")
            banco.conexao.commit()
            c.close()
            return "Peça atualizada com sucesso!"
        except:
            return "Ocorreu um erro na alteração da peça"
    
    #EXCLUIR PEÇAS
    def deletePecas(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from pecas where codigo = " + self.codigo + " ")
            banco.conexao.commit()
            c.close()
            return "Peça excluída com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do peça"

    #BUSCAR PEÇAS
    def selectPecas(self, codigo):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from pecas where codigo = " + codigo + "  ")
            for linha in c:
                self.codigo = linha[0]
                self.nome = linha[1]
                self.quantidade = linha[2]
                self.preco = linha[3]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da peça"

    #BUSCAR PEÇAS COM MAIOR VALOR
    def selectPecasMaVlr(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from pecas group by codigo order by preco desc limit 1")
            for linha in c:
                self.codigo = linha[0]
                self.nome = linha[1]
                self.quantidade = linha[2]
                self.preco = linha[3]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da peça"

    #BUSCAR PEÇAS COM MENOR VALOR
    def selectPecasMeVlr(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from pecas group by codigo order by preco limit 1")
            for linha in c:
                self.codigo = linha[0]
                self.nome = linha[1]
                self.quantidade = linha[2]
                self.preco = linha[3]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da peça"

    #BUSCAR PEÇAS COM MAIOR QUANTIDADE
    def selectPecasMaQtde(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from pecas group by codigo order by quantidade desc limit 1")
            for linha in c:
                self.codigo = linha[0]
                self.nome = linha[1]
                self.quantidade = linha[2]
                self.preco = linha[3]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca da peça"