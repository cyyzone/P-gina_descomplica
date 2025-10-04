# Importando as ferramentas que acabamos de instalar
import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv() # Esta função carrega as variáveis do arquivo .env

# Criando o nosso aplicativo (o servidor)
app = Flask(__name__)
CORS(app) # Aplicando o CORS para permitir a comunicação

# --- A PARTE MAIS IMPORTANTE: SUA CHAVE SECRETA ---
# Cole a sua Chave de API que você guardou, DENTRO DAS ASPAS
# É MUITO IMPORTANTE que a chave fique aqui, no back-end, e não no javascript.
# Pega a chave de API das variáveis de ambiente
API_KEY = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=API_KEY)

# Configurando a biblioteca do Google com a nossa chave
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Definindo o modelo de IA que vamos usar
model = genai.GenerativeModel('models/gemini-2.5-flash')

# Criando a "rota" ou "endereço" que o nosso front-end vai chamar
@app.route('/descomplicar', methods=['POST'])
def descomplicar_texto():
    try:
        # 1. Pega o texto que o front-end enviou
        dados = request.get_json()
        texto_para_explicar = dados.get('texto')

        if not texto_para_explicar:
            return jsonify({"error": "Nenhum texto foi fornecido."}), 400

        # 2. Monta a instrução para a IA (o "prompt")
        prompt = f"""
            Explique o seguinte tópico de forma extremamente simples, divertida e didática para um adolescente de 14 anos. 
            Use gírias atuais brasileiras, emojis e analogias com games, séries, TikTok ou outras coisas do universo jovem.
            O tópico é: "{texto_para_explicar}"
        """

        # 3. Envia o prompt para a IA e obtém a resposta
        response = model.generate_content(prompt)
        
        # 4. Envia a resposta da IA de volta para o front-end
        return jsonify({"explicacao": response.text})

    except Exception as e:
        # Se algo der errado, envia uma mensagem de erro
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"ERRO CAPTURADO NO BACK-END: {e}")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return jsonify({"error": "Ocorreu um erro ao processar a sua solicitação."}), 500

# Esta linha faz o servidor rodar quando executamos o arquivo
if __name__ == '__main__':
    app.run(debug=True)