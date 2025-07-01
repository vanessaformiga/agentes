import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://router.huggingface.co/featherless-ai/v1/completions"
headers = {
    "Authorization": f"Bearer " + os.environ["HF_TOKEN"],
    "Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(f"Status: {response.status_code}")
    try:
        return response.json()
    except Exception as e:
        print("Erro ao decodificar JSON:", e)
        return {"erro": str(e)}

payload = {
    "model": "microsoft/phi-1_5",
    "prompt": """
Você é um assistente que responde perguntas de forma clara e objetiva em português.

Pergunta: prompt = "Can women drive in Saudi Arabia? Answer clearly based on the current law.".
Resposta:
""",
    "max_tokens": 100,
    "temperature": 0.7
}

output = query(payload)

# Mostra o retorno bruto
print("Resposta completa da API:")
print(output)

# Tenta extrair a resposta do modelo, se possível
if output and "choices" in output:
    print("\nTexto gerado:")
    print(output["choices"][0]["text"])
else:
    print("\n❗ A resposta não contém 'choices'. Verifique a estrutura acima.")