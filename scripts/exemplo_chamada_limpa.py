#!/usr/bin/env python3
"""Chamada limpa mínima (condição B): sem system prompt, sem tools, sem web.

Uso:
    API_URL="https://..." API_KEY="..." MODEL="nome-do-modelo" \
        python3 exemplo_chamada_limpa.py "sua pergunta aqui"
    # ou: python3 exemplo_chamada_limpa.py < prompts/01-preenchido.txt

Adapte o corpo ao esquema do seu provedor (OpenAI-compatível por padrão).
Registre modelo/versão/data/temperature no DATASHEET.
"""
import json
import os
import sys
import urllib.request

API_URL = os.environ.get("API_URL", "https://api.exemplo.com/v1/chat/completions")
API_KEY = os.environ.get("API_KEY", "")
MODEL = os.environ.get("MODEL", "modelo-versao")
TEMPERATURE = float(os.environ.get("TEMPERATURE", "0.1"))

def ler_prompt() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return sys.stdin.read().strip()

def main() -> int:
    prompt = ler_prompt()
    if not prompt:
        print("prompt vazio", file=sys.stderr)
        return 2
    corpo = {
        "model": MODEL,
        "temperature": TEMPERATURE,
        "messages": [{"role": "user", "content": prompt}],
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(corpo).encode("utf-8"),
        headers={"Content-Type": "application/json",
                  **({"Authorization": f"Bearer {API_KEY}"} if API_KEY else {})},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        print(resp.read().decode("utf-8"))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
