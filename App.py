from Pecas import Pecas
from tkinter import *

class Application:
    def __init__(self, master=None):
        #container1 = texto = INFORME OS DADOS
        self.fonte = ("Verdana", "8")
        self.container1 = Frame(master)
        self.container1["pady"] = 12
        self.container1.pack()
        #container2 = espaço para inserir o código
        self.container2 = Frame(master)
        self.container2["padx"] = 22
        self.container2["pady"] = 7
        self.container2.pack()
        #container3 = espaço para inserir o nome
        self.container3 = Frame(master)
        self.container3["padx"] = 22
        self.container3["pady"] = 7
        self.container3.pack()
        #container4 = espaço para inserir quantidade
        self.container4 = Frame(master)
        self.container4["padx"] = 22
        self.container4["pady"] = 7
        self.container4.pack()
        #container5 = espaço para inserir o preço
        self.container5 = Frame(master)
        self.container5["padx"] = 22
        self.container5["pady"] = 7
        self.container5.pack()
        #container6 = espaço para os botões INSERIR, ALTERAR e EXCLUIR
        self.container6 = Frame(master)
        self.container6["padx"] = 22
        self.container6["pady"] = 12
        self.container6.pack()
        #container7 = espaço para os botões MAIORVALOR, MENORVALOR e MAIORQTDE
        self.container7 = Frame(master)
        self.container7["padx"] = 22
        self.container7["pady"] = 12
        self.container7.pack()
        #container8 = espaço para um label de msg
        self.container8 = Frame(master)
        self.container8["pady"] = 17
        self.container8.pack()
        
        # TÍTULO (container1 - só o texto)
        self.titulo = Label(self.container1, text="INFORME OS DADOS :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        # CÓDIGO (container2 - texto e espaço para inserir o código)
        self.lblcodigo = Label(self.container2, text="Código:(100)", font=self.fonte, width=10)
        self.lblcodigo.pack(side=LEFT)
        self.txtcodigo = Entry(self.container2)
        self.txtcodigo["width"] = 10
        self.txtcodigo["font"] = self.fonte
        self.txtcodigo.pack(side=LEFT)

        # BOTÃO BUSCAR PELO CÓDIGO (container2 - Botão de busca)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarPecas
        self.btnBuscar.pack(side=RIGHT)

        # NOME (container3 - texto e espaço para o nome da peça)
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        # QUANTIDADE (container4 - texto e espaço para a quantidade de peças)
        self.lblquantidade = Label(self.container4, text="Quantidade:", font=self.fonte, width=10)
        self.lblquantidade.pack(side=LEFT)
        self.txtquantidade = Entry(self.container4)
        self.txtquantidade["width"] = 25
        self.txtquantidade["font"] = self.fonte
        self.txtquantidade.pack(side=LEFT)

        # PREÇO (container5 - texto e espaço para o preço da peça)
        self.lblpreco= Label(self.container5, text="Preço:", font=self.fonte, width=10)
        self.lblpreco.pack(side=LEFT)
        self.txtpreco = Entry(self.container5)
        self.txtpreco["width"] = 25
        self.txtpreco["font"] = self.fonte
        self.txtpreco.pack(side=LEFT)

        # BOTÃO INSERIR (container6 - botão para inserir dados da peça)
        self.btnInsert = Button(self.container6, text="Inserir", font=self.fonte, width=12)
        self.btnInsert["command"] = self.inserirPecas
        self.btnInsert.pack (side=LEFT)

        # BOTÃO ALTERAR (container6 - botão para alterar dados da peça)
        self.btnUpdate = Button(self.container6, text="Alterar", font=self.fonte, width=12)
        self.btnUpdate["command"] = self.alterarPecas
        self.btnUpdate.pack (side=LEFT)

        # BOTÃO EXCLUIR (container6 - botão de excluir dados da peça)
        self.btnDelete = Button(self.container6, text="Excluir", font=self.fonte, width=12)
        self.btnDelete["command"] = self.excluirPecas
        self.btnDelete.pack(side=LEFT)

        # BOTÃO BUSCAR MAIORVALOR (container7 - busca peça de maior valor)
        self.btnBuscar = Button(self.container7, text="Maior Valor", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarMaiorValor
        self.btnBuscar.pack(side=LEFT)

        # BOTÃO BUSCAR MENORVALOR (container7 - busca peça de menor valor)
        self.btnBuscar = Button(self.container7, text="Menor Valor", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarMenorValor
        self.btnBuscar.pack(side=LEFT)

        # BOTÃO BUSCAR MAIORQTDE (container7 - busca peça com maior quantidade)
        self.btnDelete = Button(self.container7, text="Maior Qtde", font=self.fonte, width=12)
        self.btnDelete["command"] = self.buscarMaiorQtde
        self.btnDelete.pack(side=LEFT)

        # Área de MSG (container8 - label de msg)
        self.lblmsg = Label(self.container8, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    # INSERIR PEÇAS
    def inserirPecas(self):
        pecas = Pecas()
        pecas.codigo = self.txtcodigo.get()
        pecas.nome = self.txtnome.get()
        pecas.quantidade = self.txtquantidade.get()
        pecas.preco = self.txtpreco.get()
        self.lblmsg["text"] = pecas.insertPecas()
        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtquantidade.delete(0, END)
        self.txtpreco.delete(0, END)

    # ALTERAR PEÇAS
    def alterarPecas(self):
        pecas = Pecas()
        pecas.codigo = self.txtcodigo.get()
        pecas.nome = self.txtnome.get()
        pecas.quantidade = self.txtquantidade.get()
        pecas.preco = self.txtpreco.get()
        self.lblmsg["text"] = pecas.updatePecas()
        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtquantidade.delete(0, END)
        self.txtpreco.delete(0, END)

    # EXCLUIR PEÇAS
    def excluirPecas(self):
        pecas = Pecas()
        pecas.codigo = self.txtcodigo.get()
        self.lblmsg["text"] = pecas.deletePecas()
        self.txtcodigo.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtquantidade.delete(0, END)
        self.txtpreco.delete(0, END)

    # BUSCAR PEÇAS
    def buscarPecas(self):
        pecas = Pecas()
        codigo = self.txtcodigo.get()
        self.lblmsg["text"] = pecas.selectPecas(codigo)
        self.txtcodigo.delete(0, END)
        self.txtcodigo.insert(INSERT, pecas.codigo)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, pecas.nome)
        self.txtquantidade.delete(0, END)
        self.txtquantidade.insert(INSERT, pecas.quantidade)
        self.txtpreco.delete(0, END)
        self.txtpreco.insert(INSERT, pecas.preco)

    # BUSCAR PEÇAS MAIOR VALOR
    def buscarMaiorValor(self):
        pecas = Pecas()
        codigo = self.txtcodigo.get()
        self.lblmsg["text"] = pecas.selectPecasMaVlr()
        self.txtcodigo.delete(0, END)
        self.txtcodigo.insert(INSERT, pecas.codigo)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, pecas.nome)
        self.txtquantidade.delete(0, END)
        self.txtquantidade.insert(INSERT, pecas.quantidade)
        self.txtpreco.delete(0, END)
        self.txtpreco.insert(INSERT, pecas.preco)

    # BUSCAR PEÇAS MENOR VALOR
    def buscarMenorValor(self):
        pecas = Pecas()
        codigo = self.txtcodigo.get()
        self.lblmsg["text"] = pecas.selectPecasMeVlr()
        self.txtcodigo.delete(0, END)
        self.txtcodigo.insert(INSERT, pecas.codigo)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, pecas.nome)
        self.txtquantidade.delete(0, END)
        self.txtquantidade.insert(INSERT, pecas.quantidade)
        self.txtpreco.delete(0, END)
        self.txtpreco.insert(INSERT, pecas.preco)
    
    # BUSCAR PEÇAS MAIOR QTDE
    def buscarMaiorQtde(self):
        pecas = Pecas()
        codigo = self.txtcodigo.get()
        self.lblmsg["text"] = pecas.selectPecasMaQtde()
        self.txtcodigo.delete(0, END)
        self.txtcodigo.insert(INSERT, pecas.codigo)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, pecas.nome)
        self.txtquantidade.delete(0, END)
        self.txtquantidade.insert(INSERT, pecas.quantidade)
        self.txtpreco.delete(0, END)
        self.txtpreco.insert(INSERT, pecas.preco)

root = Tk()
root.title("AUTOPEÇAS DO SALVADOR")
Application(root)
root.mainloop()