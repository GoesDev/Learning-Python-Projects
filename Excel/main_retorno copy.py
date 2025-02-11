import pandas as pd

arquivo_excel = 'b2b-01_01_2025-05_02_2025.xls'
df = pd.read_excel(arquivo_excel, engine='openpyxl')

todas_as_colunas = list(df.columns)

count = 0
colunas_para_deletar = []
colunas_para_n_deletar = [
    'REG OBRA',
    'N° PROJETO',
    'ATP',
    'ID AGENDA',
    'SUBPROCESSO',
    'NOME DO SITE OU CLIENTE',
    'ENDEREÇO DA OBRA',
    'GESTOR RESP. VIVO',
    'DSP/FSP',
    'SEGUIMENTO',
    'TIPO DE SERVIÇO',
    'TIPO DE ATIVIDADE',
    'DATA FINALIZAÇÃO',
    'STATUS DA ATIVIDADE',
    'EQUIPE TÉCNICA',
    'SITUAÇÃO ORÇAMENTO',
    'TOTAL C/ IMPOSTO',
    'ID',
    'REFERENCIA'
]

count = 0

# CRIA UMA LISTA COM AS COLUNAS QUE DEVEM SER EXCLUIDAS
for c in todas_as_colunas:
    if c not in colunas_para_n_deletar:
        colunas_para_deletar.append(count)
    count += 1

# DELETA AS COLUNAS ARMAZENADAS NA LISTA
df = df.drop(df.columns[colunas_para_deletar], axis=1)


# EXCLUINDO TODAS AS LINHAS QUE TENHAM SUPERVISOR VERIFICANDO NA
# COLUNA ORÇAMENTO
coluna_excluir = 'SITUAÇÃO ORÇAMENTO'
linha_excluir = 'SUPERVISOR VERIFICANDO'
df = df[df[coluna_excluir] != linha_excluir]

# EXCLUINDO TODAS AS LINHAS CUJO VALOR NÃO SEJA 0 NA COLUNA
# TOTAL C/ IMPOSTO
df = df[df['TOTAL C/ IMPOSTO'] == 0]

# EXCLUINDO TODAS AS LINHAS CUJO VALOR NÃO SEJA CONCLUSIVA NA COLUNA
# STATUS ATIVIDADE
df = df[df['STATUS DA ATIVIDADE'] == 'CONCLUSIVA']


print(df.head(100))

df.to_excel('retorno_final.xlsx', index=False, engine='openpyxl')
