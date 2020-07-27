#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

# NOME: ERGON ZAMARIAN LIMA
# RA: 167776

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Quantos dias de férias devo tirar
# Cria as variáveis do problema
 # IDENTIFICANDO
estresse = ctrl.Antecedent(np.arange(0, 11, 1), 'estresse')
cansado = ctrl.Antecedent(np.arange(0, 11, 1), 'cansado')
qtd_dias_ferias = ctrl.Consequent(np.arange(0, 30, 1), 'qtd_dias_ferias')

# Cria automaticamente o mapeamento entre valores nítidos e difusos 
# usando uma função de pertinência padrão (triângulo)
estresse.automf(names=['pouco', 'médio', 'muito'])


# Cria as funções de pertinência usando tipos variados
cansado['baixo'] = fuzz.trimf(cansado.universe, [0, 0, 5])
cansado['intermediario'] = fuzz.gaussmf(cansado.universe, 5, 2)
cansado['alto'] = fuzz.gaussmf(cansado.universe, 10,3)

qtd_dias_ferias['poucos_dias'] = fuzz.trimf(qtd_dias_ferias.universe, [0, 0, 15])
qtd_dias_ferias['medios_dias'] = fuzz.trimf(qtd_dias_ferias.universe, [0, 15, 30])
qtd_dias_ferias['muitos_dias'] = fuzz.trimf(qtd_dias_ferias.universe, [15, 30, 30])

rule1 = ctrl.Rule(estresse['muito'] | cansado['alto'], qtd_dias_ferias['muitos_dias'])
rule2 = ctrl.Rule(estresse['médio'], qtd_dias_ferias['medios_dias'])
rule3 = ctrl.Rule(estresse['pouco'] & cansado['baixo'], qtd_dias_ferias['poucos_dias'])


class Application:
    def __init__(self, master=None):

        master.title("Analisador de Férias")
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 30
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.setimotoContainer = Frame(master)
        self.setimotoContainer["pady"] = 20
        self.setimotoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 30
        self.quintoContainer.pack()
        
        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] = 30
        self.sextoContainer.pack()

        self.ultimoContainer = Frame(master)
        self.ultimoContainer["pady"] = 30
        self.ultimoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="ANALISADOR DE FÉRIAS ")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
    
        self.FraseLabel = Label(self.segundoContainer,text="ESTRESSE (0 a 10) : ", font=self.fontePadrao)
        self.FraseLabel.pack(side=LEFT)

        self.FraseLabel = Label(self.terceiroContainer,text="CANSADO (0 a 10) : ", font=self.fontePadrao)
        self.FraseLabel.pack(side=LEFT)

        self.frase1 = Entry(self.segundoContainer)
        self.frase1["width"] = 100
        self.frase1["font"] = self.fontePadrao
        self.frase1.pack(side=LEFT)

        self.frase2 = Entry(self.terceiroContainer)
        self.frase2["width"] = 100
        self.frase2["font"] = self.fontePadrao
        self.frase2.pack(side=LEFT)

        self.analisar = Button(self.quartoContainer)
        self.analisar["text"] = "ANALISAR"
        self.analisar["font"] = ("Calibri", "10", "bold")
        self.analisar["width"] = 12
        self.analisar["command"] = self.print_analise
        self.analisar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.titulo2 = Label(self.setimotoContainer, text="GRAFICOS")
        self.titulo2["font"] = ("Arial", "10", "bold")
        self.titulo2.pack()

        self.print_grafico = Button(self.quintoContainer)
        self.print_grafico["text"] = "FUNÇAO"
        self.print_grafico["font"] = ("Calibri", "10", "bold")
        self.print_grafico["width"] = 12
        self.print_grafico["command"] = self.printar_grafico1
        self.print_grafico.pack()

        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.print_grafico = Button(self.sextoContainer)
        self.print_grafico["text"] = "RESULTADO"
        self.print_grafico["font"] = ("Calibri", "10", "bold")
        self.print_grafico["width"] = 12
        self.print_grafico["command"] = self.printar_grafico2
        self.print_grafico.pack()

        self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.titulo3 = Label(self.ultimoContainer, text=" QUANTOS DIAS DE FÉRIAS? ")
        self.titulo3["font"] = ("Arial", "10", "bold")
        self.titulo3.pack()

        self.mensagem = Label(self.ultimoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # ANALISANDO FÉRIAS
    def print_analise(self):
        frase_use1 = self.frase1.get()
        frase_use2 = self.frase2.get()
        qtd_dias_ferias_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
        qtd_dias_ferias_simulador = ctrl.ControlSystemSimulation(qtd_dias_ferias_ctrl)
        qtd_dias_ferias_simulador.input['estresse'] = int(frase_use1)
        qtd_dias_ferias_simulador.input['cansado'] = int(frase_use2)
        qtd_dias_ferias_simulador.compute()
        
        print(round(qtd_dias_ferias_simulador.output['qtd_dias_ferias']))
        self.mensagem["text"] =  round(qtd_dias_ferias_simulador.output['qtd_dias_ferias'])

        
    def printar_grafico1(self):

        estresse.view()
        cansado.view()
        qtd_dias_ferias.view()
        print('oi')
    def printar_grafico2(self):

        frase_use1 = self.frase1.get()
        frase_use2 = self.frase2.get()
        qtd_dias_ferias_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
        qtd_dias_ferias_simulador = ctrl.ControlSystemSimulation(qtd_dias_ferias_ctrl)
        qtd_dias_ferias_simulador.input['estresse'] = int(frase_use1)
        qtd_dias_ferias_simulador.input['cansado'] = int(frase_use2)
        qtd_dias_ferias_simulador.compute()

        estresse.view(sim=qtd_dias_ferias_simulador)
        cansado.view(sim=qtd_dias_ferias_simulador)
        qtd_dias_ferias.view(sim=qtd_dias_ferias_simulador)
        print('oi')
        
root = Tk()
Application(root)
root.mainloop()