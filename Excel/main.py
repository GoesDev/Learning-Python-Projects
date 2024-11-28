import pandas as pd

arquivo_excel = 'orcamento.xlsx'
df = pd.read_excel(arquivo_excel, engine='openpyxl')


coluna = ['ID AGENDA',
          'STATUS DA ATIVIDADE',
          'STATUS DA ATIVIDADE',
          'SITUAÇÃO DO ORÇAMENTO',
          'SITUAÇÃO DO ORÇAMENTO',
          'SITUAÇÃO DO ORÇAMENTO']

valor = ['PRODUTIZADO',
         'PENDÊNCIA',
         'CANCELADA',
         'FINALIZADO',
         'SUPERVISOR VERIFICANDO',
         'N/A']

colunas_para_deletar = [
    'REG OBRGA',
    'Nº PROJETO',
    'LIDER',
    'MATERIAL SGCI',
    'SERVIÇO SGCI',
    'SITE'
]


for i in range(6):
    df = df[df[coluna[i]] != valor[i]]

df = df[df['SITUAÇÃO DO ORÇAMENTO'].apply(
    lambda x: pd.notna(x) and x.strip() != '')]
df = df[df['STATUS DA ATIVIDADE'].apply(
    lambda x: pd.notna(x) and x.strip() != '')]

df.to_excel('_arquivo.xlsx', index=False, engine='openpyxl')
