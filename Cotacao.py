#importando bibliotecas
import pyodbc
import requests
import pandas
from datetime import datetime
import time

#conectando a aplicação com o banco de dados.
dados_conexao = (
    "DRIVER={SQL Server};"
    "SERVER=PEDRO-LENOVO\SQLEXPRESS;"
    "DATABASE=Cotacao;"
    "UID=sa;"
    "PWD=as1453!@;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")

cursor = conexao.cursor()

#WebScrepping

#Pegando a cotação do DOLAR e do EURO.

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL")
requisicao_dic = requisicao.json()

#Cotação das moedas com a data da ultima atualização.
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
data_atualizacao = datetime.now()

cursor = conexao.cursor()

#Inserindo as cotações no banco de dados, na tabela COTACAODIARIA

comando = f""" INSERT INTO COTACAODIARIA (dolar, euro, data_atualizacao) VALUES ('{cotacao_dolar}', '{cotacao_euro}','{data_atualizacao}')"""
cursor.execute(comando)
cursor.commit()
cursor.commit()