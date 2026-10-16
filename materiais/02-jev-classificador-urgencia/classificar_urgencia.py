"""Classifica mensagens de alunos em "urgente" ou "nao_urgente" usando o Jev (TypeSafe).

Uso:
    export TYPESAFE_API_KEY="sua-chave"
    python classificar_urgencia.py mensagens_exemplo.json

    # Ver o que seria enviado, sem chamar a API (não precisa de chave):
    python classificar_urgencia.py mensagens_exemplo.json --dry-run

O arquivo de entrada é uma lista JSON de objetos com os campos "aluno" e "mensagem".
Só usa a biblioteca padrão do Python (3.10+).
"""

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

API_URL = "https://api.typesafe.ai/v1/systemone"
MODELO = "jev-latest"
# Abaixo desta confiança, a mensagem vai para revisão humana.
CONFIANCA_MINIMA = 0.6

PERGUNTAS = {
    "urgencia": {
        "type": "choice",
        "instructions": "A mensagem do aluno em `mensagem` é urgente para a equipe de atendimento?",
        "criteria": {
            "urgente": (
                "Precisa de resposta rápida: impede o aluno de estudar ou fazer uma "
                "avaliação, envolve prazo próximo, aula começando, cobrança indevida "
                "ou problema de acesso"
            ),
            "nao_urgente": (
                "Pode esperar: dúvidas gerais, sugestões, elogios, pedidos sem prazo "
                "próximo"
            ),
        },
    },
}


def montar_requisicao(mensagem: str) -> dict:
    return {"model": MODELO, "state": {"mensagem": mensagem}, "questions": PERGUNTAS}


def chamar_jev(corpo: dict, chave: str, tentativas: int = 4) -> dict:
    dados = json.dumps(corpo).encode("utf-8")
    for tentativa in range(tentativas):
        req = urllib.request.Request(
            API_URL,
            data=dados,
            headers={
                "Authorization": f"Bearer {chave}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as erro:
            # 429 (limite de requisições) e 529 (sobrecarga): tenta de novo com espera crescente.
            if erro.code in (429, 529) and tentativa < tentativas - 1:
                time.sleep(2 ** (tentativa + 1))
                continue
            detalhe = erro.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Jev respondeu {erro.code}: {detalhe}") from erro
    raise RuntimeError("Jev indisponível após várias tentativas")


def classificar(mensagem: str, chave: str) -> tuple[str, float]:
    resposta = chamar_jev(montar_requisicao(mensagem), chave)
    urgencia = resposta["answers"]["urgencia"]
    if urgencia["confidence"] < CONFIANCA_MINIMA:
        return "revisao_humana", urgencia["confidence"]
    return urgencia["choice"], urgencia["confidence"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("arquivo", help="JSON com a lista de mensagens")
    parser.add_argument("--dry-run", action="store_true", help="mostra a requisição sem enviar")
    args = parser.parse_args()

    with open(args.arquivo, encoding="utf-8") as f:
        mensagens = json.load(f)

    if args.dry_run:
        for item in mensagens:
            print(json.dumps(montar_requisicao(item["mensagem"]), ensure_ascii=False, indent=2))
        return 0

    chave = os.environ.get("TYPESAFE_API_KEY")
    if not chave:
        print("Defina a variável TYPESAFE_API_KEY com sua chave da TypeSafe.", file=sys.stderr)
        return 1

    for item in mensagens:
        rotulo, confianca = classificar(item["mensagem"], chave)
        print(f"[{rotulo:>14}] ({confianca:.0%}) {item['aluno']}: {item['mensagem']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
