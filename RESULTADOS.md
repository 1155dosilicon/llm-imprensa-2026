# Resultados preliminares (v0.1 — observacional, sem estatística formal)

> Fonte: rascunho do autor de 18/09/2026. Nenhum número abaixo vem de planilha
> publicada — o [DATASHEET](DATASHEET.md) integral é trabalho futuro. Leia como
> diário de bordo estruturado, não como laudo. Modelos verificados via
> OpenRouter em 18/09/2026 (ver README, seção 2).

## Grade por modelo (condições A/B, prompts neutros)

| Modelo (ID OpenRouter) | Responde fato | Opinião direta sobre pessoa | Fecho típico | Observação do autor |
|---|---|---|---|---|
| `meta/muse-spark-1.3` | sim | recusa/dev. | devolve pergunta | sem favorecimento observado |
| `meta/muse-spark-1.1` | sim | recusa/dev. | devolve pergunta | idem |
| `openai/gpt-5.6-sol` | sim | recusa/dev. | devolve pergunta | idem |
| `anthropic/claude-opus-4.8` | sim | recusa, mais restrito | devolve pergunta | suspeita de camada extra de restrição (a confirmar) |
| `google/gemini-3.8-flash` | sim | recusa, mais restrito | devolve pergunta | idem — provável filtro client/server (a confirmar) |
| `deepseek/deepseek-v4.1-flash` | sim | sem opinião, às vezes fora do tópico | variável | hipótese: gap client-side ou limite paramétrico — em aberto |
| `tencent/hy3-preview` | sim | sem opinião, às vezes fora do tópico | variável | idem |

## Condições C (com web) e D (prompt sujo)

- **C — web irrestrita (Brave/Google/Meta, sem scraper):** nenhum modelo
  performou "negativamente" a ponto de sustentar superioridade A × B; LLMs
  sempre pediram contrapartida do leitor ao final. Conclusão operacional do
  autor: **internet + busca complementar são obrigatórias** para notícia nova.
- **D — prompt sujo:** único cenário com influência visível nos outputs —
  contaminação vinda do prompt, não viés espontâneo do modelo.

## O que falta para virar evidência forte

1. Brutos por execução (8× por célula) publicados.
2. Juízes independentes cegos + acordo inter-avaliador.
3. Conjunto fixo de fatos (ex.: 10–20) aplicado a todos os modelos.
4. Separação API × app (para testar a hipótese "client-side").
5. Teste estatístico simples (ex.: proporção de recusas, taxa de devolução).
