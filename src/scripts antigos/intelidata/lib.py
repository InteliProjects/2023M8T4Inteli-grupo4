import os
import pandas as pd

def nome_arquivo(pasta):
    arquivo = []
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.csv'):
            arquivo.append(nome_arquivo)
    return arquivo

def ler_csv(caminho_completo_arquivo, separadores):
    for separador in separadores:
        try:
            df = pd.read_csv(caminho_completo_arquivo, encoding='latin1', sep=separador)
            break
        except pd.errors.ParserError:
            continue
    return df

def tratar_csv(nome_arquivo, csv_tratado, valor_preenchimento):
    caminho_completo_arquivo = os.path.join('./csv/', nome_arquivo)
    separadores = [',', ';']
    df = ler_csv(caminho_completo_arquivo, separadores)
    df = df.fillna(valor_preenchimento)
    caminho_arquivo_tratado = os.path.join(csv_tratado, f"{nome_arquivo}_tratado")
    df.to_csv(caminho_arquivo_tratado, index=False, sep=separadores[0], encoding='utf-8') 
    print(f"Arquivo {nome_arquivo} tratado e salvo como {caminho_arquivo_tratado}")

def processar_csv():
    pasta = './csv'
    arquivo = nome_arquivo(pasta)

    csv_tratado = './csv_tratados'
    valor_preenchimento = "N/A"
 
    for nome_arquivo in arquivo:
        tratar_csv(nome_arquivo, csv_tratado, valor_preenchimento)
