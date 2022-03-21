# Iago Leonardo Alves de Oliveira
# 20/03/2022
# Calculadora com interface gráfica que realiza cáculos matemáticos com a lib eval

### Importa as bibliotecas
#PyQt5 - Interface gráfica (.ui) (pip install PyQt5)
from PyQt5 import uic, QtWidgets
#OS - Controle do sistema operacional
import os


#Lista de operadores
operadores = ['+', '-', '/', '*']

#Função responsável por alterar o valor do visor ao clicar no botão
def clicouBotao(botao):
    
    #Recebe o visor e o valor dele
    visor = forms.txtVisor #elemento visor
    valor = str(visor.text()) #valor dentro do elemento visor

    #Se o valor no visor for 0
    if valor == '0':
        #Se o botão clicado for ponto ou operador
        if(botao == '.' or botao in operadores):
            #Altera o texto do visor com 0 na esquerda
            visor.setText('0' + botao)
    
        #Se o botão não for ponto ou operador
        else:
            #Altera o texto do visor para o número que foi clicado
            visor.setText(botao)    
    
    #Se o valor no visor for diferente de zero
    else:
        #Se o botão for um operador
        if(botao in operadores):
           
            #Se o ultimo digito do visor não for um operador e nao for ponto
            if(not(valor[-1] in operadores) and not(valor[-1] == '.')):
                #Concatena ao valor já existente
                visor.setText(valor + botao)
        
        #Se o botão for ponto
        elif(botao == '.'):
            
            #Se o último dígito do visor for um operador ao invés de um número
            if(valor[-1] in operadores):
                #Concatena zero e ponto ao valor já existente
                visor.setText(valor + '0' + botao)

            #Se o último dígito do visor não for um operador 
            else:
                numero = ''
                #Verifica se o último número do visor já contém ponto
                i = 1
                while i <= len(valor):
                    #Recebe o dígito de trás para frente
                    digito = valor[-i]
                    
                    #Se o dígito atual for um operador
                    if digito in operadores:
                        #Quebra o loop
                        break 
                    else:
                        #Adiciona o digito para formar o ultimo numero do visor
                        numero = digito + numero

                    #Incrementa o contador
                    i += 1
                
                #Se o último número inserido não contém ponto
                if not('.' in numero):
                    #Concatena o ponto ao valor já existente
                    visor.setText(valor + botao)
        
        #Se o botão não for operador e nem ponto
        else:
            #Concatena ao valor já existente
            visor.setText(valor + botao)


#Função que calcula o resultado
def calcular():
    #Recebe o visor e o valor dele
    visor = forms.txtVisor #elemento visor
    valor = str(visor.text()) #valor dentro do elemento visor

    #Recebe a barra de histórico
    historico = forms.txtHistorico

    #Se o ultimo digito do visor não for um operador e nao for ponto
    if(not(valor[-1] in operadores) and not(valor[-1] == '.')):
        
        #Loop por cada dígito do visor
        for d in valor:    
            #Se houver algum operador no visor
            if d in operadores:
                #Atualiza a barra de histórico
                historico.setText(valor)
                #Substitui o texto do visor pelo resultado do cálculo
                visor.setText(str(eval(valor)))
        
                #Quebra o loop
                break
    
#Função que apaga o ultimo valor digitado
def apagar():
    #Recebe o visor e o valor dele
    visor = forms.txtVisor
    valor = str(visor.text())

    #Se o valor tiver apenas 1 dígito
    if len(valor) == 1:
        #Se o valor do visor for diferente de 0
        if valor != '0':
            #Altera o valor do visor para 0
            visor.setText('0')

    #Se o valor tiver mais de 1 dígito
    else:
        #Remove o ultimo dígito do valor e atualiza o visor
        visor.setText(valor[:-1])

#Função que limpa o visor
def apagarTudo():
    #Recebe o visor e o valor dele
    visor = forms.txtVisor
    valor = str(visor.text())
    #Recebe a barra de histórico
    historico = forms.txtHistorico

    #Se o valor do visor for diferente de 0
    if valor != '0':
        #Altera o valor do visor para 0
        visor.setText('0')
    
    #Limpa o historico
    historico.setText('')



####### Esse trecho faz o link com a interface gráfica
app = QtWidgets.QApplication([])
#Carrega a interface gráfica
forms = uic.loadUi(uifile=os.path.dirname(os.path.abspath(__file__)) + '/Interface/formsCalc.ui')

#Botões apagar
forms.btnApagar.clicked.connect(apagar)
forms.btnApagarTudo.clicked.connect(apagarTudo)
#Botões números e ponto
forms.btnPonto.clicked.connect(lambda: clicouBotao('.'))
forms.btnNum0.clicked.connect(lambda: clicouBotao('0'))
forms.btnNum1.clicked.connect(lambda: clicouBotao('1'))
forms.btnNum2.clicked.connect(lambda: clicouBotao('2'))
forms.btnNum3.clicked.connect(lambda: clicouBotao('3'))
forms.btnNum4.clicked.connect(lambda: clicouBotao('4'))
forms.btnNum5.clicked.connect(lambda: clicouBotao('5'))
forms.btnNum6.clicked.connect(lambda: clicouBotao('6'))
forms.btnNum7.clicked.connect(lambda: clicouBotao('7'))
forms.btnNum8.clicked.connect(lambda: clicouBotao('8'))
forms.btnNum9.clicked.connect(lambda: clicouBotao('9'))
#Botões operadores
forms.btnDividir.clicked.connect(lambda: clicouBotao('/'))
forms.btnMultiplicar.clicked.connect(lambda: clicouBotao('*'))
forms.btnSomar.clicked.connect(lambda: clicouBotao('+'))
forms.btnSubtrair.clicked.connect(lambda: clicouBotao('-'))
#Botão igual
forms.btnIgual.clicked.connect(lambda: calcular())

#Exibe a interface
forms.show()
#Executa
app.exec()