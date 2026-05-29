import os
import time
from google import genai
from dotenv import load_dotenv

load_dotenv()

cliente = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELO = "gemini-2.5-flash"


def analisar_incidente(incidente, tentativas=3):
    prompt = f"""
Você é um analista de sistemas especialista em fluxos comerciais de planos de saúde.

Analise o seguinte incidente detectado automaticamente e responda em português,
de forma objetiva e profissional, com exatamente três seções:

INCIDENTE:
- Pedido: {incidente.pedido.codigo} ({incidente.pedido.tipo_fluxo})
- Tipo: {incidente.tipo}
- Severidade: {incidente.severidade}/5
- Detalhe: {incidente.detalhe}

Responda EXATAMENTE neste formato:

RESUMO DE TRIAGEM:
[2-3 frases explicando o problema e seu impacto]

DIRECIONAMENTO SUGERIDO:
[Uma linha: Infraestrutura / TI / Desenvolvimento / Operacional — e o motivo]

CARD AZURE DEVOPS:
Título: [título objetivo do card]
Descrição: [descrição técnica do problema para o time responsável, 3-4 linhas]
"""

    for tentativa in range(1, tentativas + 1):
        try:
            resposta = cliente.models.generate_content(
                model=MODELO,
                contents=prompt,
            )
            return resposta.text
        except Exception as e:
            erro = str(e)
            if "503" in erro or "UNAVAILABLE" in erro:
                print(f"  Servidor ocupado, tentativa {tentativa}/{tentativas}. Aguardando 10s...")
                time.sleep(10)
            else:
                raise
    return f"[IA indisponível após {tentativas} tentativas]"


def enriquecer_incidentes(incidentes):
    resultado = []
    for incidente in incidentes:
        analise = analisar_incidente(incidente)
        resultado.append((incidente, analise))
    return resultado