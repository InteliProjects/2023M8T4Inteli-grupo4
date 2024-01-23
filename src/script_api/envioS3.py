import pandas as pd
import requests
import datetime
import csv
import json
import os
import boto3
from io import StringIO

aws_access_key_id = " " # A chave de acesso da AWS não está sendo passada por questões de segurança
aws_secret_access_key = " " # A chave de acesso secreta da AWS não está sendo passada por questões de segurança
aws_session_token = " " # O token de sessão da AWS não está sendo passado por questões de segurança
bucket = "grupo4-bigd-api"
tabelas = ["sale","category","establishment"]

class ConexaoAPI:
    def recuperar_dados(self,table_name):
        url = "https://intelifunctiongetdata.azurewebsites.net/api/InteliFunctionGetData"
        params = {
            "code": "",
            "table": table_name
        }
         
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            print(f"Erro ao recuperar dados de {table_name}: {error}")
            raise error
    
    def dados_tabelados(self, dados):
        if not dados:
            return pd.DataFrame()

        df_dados = pd.DataFrame(dados, columns=['value'])
        df_dados['tipo'] = "api_data"
        df_dados['ingestion_date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return df_dados

class ConexaoAWS:
    def __init__(self, aws_secret_access_key, aws_access_key_id, aws_session_token):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_session_token = aws_session_token
        try:
            self.s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key, aws_session_token=self.aws_session_token)
            print("Conexão com a AWS S3 feita com sucesso.")
        except Exception as e:
            print("Ocorreu um erro ao conectar-se à AWS S3")
    
    def enviar_dados(self, bucket, dados, nome_arquivo):
        try:
            # Criando uma string CSV a partir do DataFrame
            csv_buffer = StringIO()
            dados.to_csv(csv_buffer, index=False)

            # Convertendo a string CSV em bytes
            dados_encoded = csv_buffer.getvalue().encode('utf-8')

            # Enviando dados para o S3
            self.s3.put_object(Bucket=bucket, Key=nome_arquivo, Body=dados_encoded)
            print(f"Dados enviados com sucesso para o bucket '{bucket}' com o nome '{nome_arquivo}'.")
            return True
            
        except Exception as error:
            print("Erro ao enviar os dados para o bucket:", error)
            return False

def app():
    conexao_aws = ConexaoAWS(aws_secret_access_key, aws_access_key_id, aws_session_token)

    api_parceiro = ConexaoAPI()

    for tabela in tabelas:
        dados_api = api_parceiro.recuperar_dados(tabela)
        print(f"{tabela} recuperada da API com sucesso.")

        if dados_api:
            dados_df = api_parceiro.dados_tabelados(dados_api)
            nome_arquivo = f'tabela_api_{tabela}.csv'
            print(f"Base {tabela} estruturada na tabela com sucesso.")
            
            if not dados_df.empty:
                conexao_aws.enviar_dados(bucket, dados_df, nome_arquivo)
                print(f"{nome_arquivo} enviada para o {bucket} com sucesso.")

if __name__ == "__main__":
    app()