import google.generativeai as genai
import os

# COLE A SUA MESMA CHAVE DE API AQUI DENTRO DAS ASPAS
os.environ['GOOGLE_API_KEY'] = "AIzaSyBWcn41Bz28N7DMFFSN5MXUNFgCCdTavNE"

try:
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

    print("--- Modelos de IA disponíveis para sua chave de API ---")

    # Este loop vai pedir ao Google a lista de todos os modelos
    for model in genai.list_models():
        # Verificamos se o modelo suporta o método que queremos usar ('generateContent')
        if 'generateContent' in model.supported_generation_methods:
            print(f"- {model.name}")

    print("-----------------------------------------------------")

except Exception as e:
    print(f"\nOcorreu um erro ao tentar listar os modelos: {e}")