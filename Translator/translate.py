from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='pt', target='en')

texto = "Removendo"

traducao = tradutor.translate(texto)

print(traducao)
