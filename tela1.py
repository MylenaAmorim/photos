import PySimpleGUI as ps

class TelaPython:
    def __init__(self):
    #def == metodo
    #__init__ == metodo construtor, o construtor inicializa a classe e o objeto
    #o parametro self é obrigatorio

        #Layout
        layout = [
            [ps.Text('Nome:', size=(5,0)), ps.Input(size=(30,0), key='nome')],
            [ps.Text('Idade:', size=(5,0)), ps.Input(size=(15,0), key='idade')],
            [ps.Text('Cor favorita:')],
            [ps.Checkbox('Rosa', key='rosa'), ps.Checkbox('Roxo', key='roxo'), ps.Checkbox('Laranja', key='laranja')],
            [ps.Text('Marque:')],
            [ps.Radio('Sim', 'marque', key='sim'), ps.Radio('Não', 'marque', key='nao')],
            [ps.Button('Enviar Dados')],
            [ps.Output(size=(30,20))]

        ]
        #Janela
        self.janela = ps.Window("Dados do Usuário").layout(layout)
       

    def Iniciar(self): #metodo
        while True:
            #Extrair os dados da tela
            self.Button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            cor_rosa = self.values['rosa']
            cor_roxo = self.values['roxo']
            cor_laranja = self.values['laranja']
            sim = self.values['sim']
            nao = self.values['nao']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Cor rosa: {cor_rosa}')
            print(f'Cor roxa: {cor_roxo}')
            print(f'Cor laranja: {cor_laranja}')
            print(f'Marque sim: {sim}')
            print(f'Marque não: {nao}')
        

tela = TelaPython()
tela.Iniciar()
