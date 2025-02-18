import pandas as pd

arquivo_excel = 'retorno.xlsx'
df = pd.read_excel(arquivo_excel, engine='openpyxl')

todas_as_colunas = df.columns.tolist()

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


# CRIA UMA LISTA COM AS COLUNAS QUE DEVEM SER EXCLUIDAS
for coluna in todas_as_colunas:
    if coluna not in colunas_para_n_deletar:
        colunas_para_deletar.append(coluna)


# DELETA AS COLUNAS ARMAZENADAS NA LISTA
df = df.drop(colunas_para_deletar, axis=1)


# # EXCLUINDO TODAS AS LINHAS QUE TENHAM SUPERVISOR VERIFICANDO NA
# # COLUNA ORÇAMENTO
coluna_excluir = 'SITUAÇÃO ORÇAMENTO'
linha_excluir = 'SUPERVISOR VERIFICANDO'
df = df[df[coluna_excluir] != linha_excluir]

# EXCLUINDO TODAS AS LINHAS CUJO VALOR NÃO SEJA 0 NA COLUNA
# TOTAL C/ IMPOSTO
df = df[df['TOTAL C/ IMPOSTO'] == 0]

# EXCLUINDO TODAS AS LINHAS CUJO VALOR NÃO SEJA CONCLUSIVA NA COLUNA
# STATUS ATIVIDADE
df = df[df['STATUS DA ATIVIDADE'] == 'CONCLUSIVA']


df.to_excel('retorno_final.xlsx', index=False, engine='openpyxl')
