from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='pt', target='en')

texto = 'Criado um app de tradução'

traducao = tradutor.translate(texto)

print(traducao)
