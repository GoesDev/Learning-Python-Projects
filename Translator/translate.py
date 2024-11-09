from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source='pt', target='en')

texto = 'Saudações RPGistas, vamos lá pra mais um vídeo'

traducao = tradutor.translate(texto)

print(traducao)
