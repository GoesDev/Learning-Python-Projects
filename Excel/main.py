import pandas as pd
from main_variable import coluna, colunas_para_deletar, valor

arquivo_excel = 'orcamento.xlsx'
df = pd.read_excel(arquivo_excel, engine='openpyxl')

for i in range(6):
    df = df[df[coluna[i]] != valor[i]]

df = df[df['SITUAÇÃO DO ORÇAMENTO'].apply(
    lambda x: pd.notna(x) and x.strip() != '')]
df = df[df['STATUS DA ATIVIDADE'].apply(
    lambda x: pd.notna(x) and x.strip() != '')]

n_colunas = len(colunas_para_deletar)

count = 0

for c in range(n_colunas):
    del df[colunas_para_deletar[count]]
    count += 1

df = df[df['ATP'] != 'SP4']
df = df[df['SUBPROCESSO'].isnull() | (df['SUBPROCESSO'] == '')]

df['ATP'] = df['ATP'].astype(str)
df = df[~df['ATP'].str.startswith('OSX-')]

df.to_excel('_arquivo.xlsx', index=False, engine='openpyxl')
