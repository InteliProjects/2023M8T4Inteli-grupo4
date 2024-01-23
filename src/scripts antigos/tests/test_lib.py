import os
import csv
import shutil
import tempfile
import intelidata.lib as intelidata_lib
import unittest
import pandas as pd

class TesteCSVArquivosAvancado(unittest.TestCase):
    def setUp(self):
        self.temp_dir_com_arquivos = tempfile.mkdtemp()
        self.temp_dir_vazio = tempfile.mkdtemp()
        self.arquivo_csv_teste = self.criar_csv_com_dados()

    def tearDown(self):
        shutil.rmtree(self.temp_dir_com_arquivos, ignore_errors=True)
        shutil.rmtree(self.temp_dir_vazio, ignore_errors=True)

    def criar_csv_com_dados(self):
        caminho_csv = os.path.join(self.temp_dir_com_arquivos, 'dados_teste.csv')
        dados_teste = [
            ['UF', 'ESTRATO_POF', 'ESTADO'],
            [11, 2534, 'São Paulo'],
            [11, 2534, 'São Paulo'],
            [21, 2200, 'Rio de Janeiro'],
            [67, 2235, 'Mato Grosso do Sul'],
            [99, 2253, 'Maranhão']
        ]

        with open(caminho_csv, mode='w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerows(dados_teste)

        return caminho_csv

    def teste_listar_nomes_csv(self):
        try:
            nomes_arquivos = intelidata_lib.listar_nomes_csv(self.temp_dir_com_arquivos)
            self.assertIn('dados_teste.csv', nomes_arquivos, "Arquivo CSV não encontrado na listagem.")
        except Exception as e:
            self.fail(f"Erro inesperado ao listar arquivos CSV: {e}")

    def teste_ler_csv(self):
        try:
            dataframe_csv = intelidata_lib.ler_csv(self.arquivo_csv_teste, ',')
            self.assertFalse(dataframe_csv.empty, "O DataFrame está vazio.")
        except pd.errors.ParserError:
            self.fail("Erro de análise ao ler arquivo CSV.")
        except FileNotFoundError:
            self.fail("Arquivo CSV não encontrado.")
        except Exception as e:
            self.fail(f"Erro inesperado ao ler arquivo CSV: {e}")

    def teste_tratar_salvar_csv(self):
        try:
            intelidata_lib.tratar_e_salvar_csv(self.arquivo_csv_teste, self.temp_dir_vazio, 'N/A')
            arquivo_tratado = os.path.join(self.temp_dir_vazio, 'dados_teste.csv_tratado')
            self.assertTrue(os.path.exists(arquivo_tratado), "Arquivo CSV tratado não foi criado.")
        except Exception as e:
            self.fail(f"Erro inesperado ao tratar e salvar arquivo CSV: {e}")

if __name__ == '__main__':
    unittest.main()
