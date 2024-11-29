import pandas as pd

# arquivo_excel = 'orcamento-cru.xlsx'
# arquivo_excel = 'orcamento-final.xlsx'
arquivo_excel = '_arquivo.xlsx'
df = pd.read_excel(arquivo_excel, engine='openpyxl')

print(df.head(100))
print(df.shape[0])
