import pandas as pd

arquivo_excel = 'orcamento.xlsx'
df = pd.read_excel(arquivo_excel, engine='openpyxl')

coluna = ['ID AGENDA',
          'STATUS DA ATIVIDADE',
          'STATUS DA ATIVIDADE',
          'SITUAÇÃO DO ORÇAMENTO',
          'SITUAÇÃO DO ORÇAMENTO',
          'SITUAÇÃO DO ORÇAMENTO',
          'ATP']

valor = ['PRODUTIZADO',
         'PENDÊNCIA',
         'CANCELADA',
         'FINALIZADO',
         'SUPERVISOR VERIFICANDO',
         'N/A'
         'SP4']

for i in range(6):
    df = df[df[coluna[i]] != valor[i]]

todas_as_colunas = list(df.columns)

count = 0
colunas_para_deletar = []
colunas_para_n_deletar = [
    'SITUAÇÃO DO ORÇAMENTO',
    'STATUS DA ATIVIDADE',
    'ATP',
    'ID AGENDA',
    'DATA ANEXO ORÇ ATIVIDADE',
    'SP-C/SP-I',
    'SUB_PAI',
    'SUBPROCESSO',
    'DATA FINALIZAÇÃO'
]

count = 0

# CRIA UMA LISTA COM AS COLUNAS QUE DEVEM SER EXCLUIDAS
for c in todas_as_colunas:
    if c not in colunas_para_n_deletar:
        colunas_para_deletar.append(count)
    count += 1

# DELETA AS COLUNAS ARMAZENAS NA LISTA
df = df.drop(df.columns[colunas_para_deletar], axis=1)

# REMOVE LINHAS EM BRANCO NAS COLUNAS A SEGUIR
df = df.dropna(subset=['STATUS DA ATIVIDADE'])
df = df.dropna(subset=['SITUAÇÃO DO ORÇAMENTO'])

# REMOVE AS LINHAS QUE NÃO ESTÃO VAZIAS
df = df[df['SUBPROCESSO'].isna()]

# TRANSFORMA TUDO EM STRING E REMOVE AS LINHAS QUE COMEÇAM
# COM OSX
df = df[df['ATP'] != 'SP4']
df['ATP'] = df['ATP'].astype(str)
df = df[~df['ATP'].str.startswith('OSX')]

print(df.head(100))

df.to_excel('orcamento_final.xlsx', index=False, engine='openpyxl')
