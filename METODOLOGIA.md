# Metodologia

Protocolo de replicação do estudo. Objetivo: qualquer pessoa com acesso às APIs
conseguir repetir o essencial e comparar.

## 1. Corpus de notícias

- **Janela:** 01/01/2026 a 18/09/2026, política brasileira.
- **Fontes de vídeo usadas como referência inicial** (declaradas pelo autor —
  ver [REFERENCIAS](REFERENCIAS.md) para URLs e leitura crítica):
  - canal/programa associado a "Metrópole / MBL"
  - BandNews FM
  - Record News
  - GloboNews
- **Exclusões declaradas:** Mídia Ninja, Catraca Livre, O Antagonista,
  Brasil 247. Motivo declarado: financiamento/posicionamento presumido.
  Registre qualquer mudança nesse conjunto no datasheet — ela altera o resultado.

## 2. Condições de teste

| Condição | Código | Descrição |
|---|---|---|
| Harness do autor | A | 8 repetições por modelo × pergunta, no ambiente usual do autor |
| API limpa | B | chamada REST/HTTPS direta em Python, sem system prompt custom, sem tools, sem web |
| API + web | C | condição B + busca web irrestrita (Brave/Google/Meta Search via API ou MCP), sem webscraper dedicado |
| Prompt sujo (controle) | D | mesmo fato, mas com enquadramento forçadamente enviesado no prompt |

## 3. Parâmetros a fixar (e registrar)

- ID exato do modelo no OpenRouter (ex. `meta/muse-spark-1.3`,
  `openai/gpt-5.6-sol`, `anthropic/claude-opus-4.8`,
  `deepseek/deepseek-v4.1-flash`, `tencent/hy3-preview`,
  `google/gemini-3.8-flash`), data/hora (UTC), seed/temperature/top_p
  (use temperature baixa, ex. 0.0–0.2, para a condição B; registre o valor real);
- latência, tokens in/out, custo, código HTTP/erro;
- recusa ou não-recusa (literal), texto integral da resposta;
- para a condição C: provedor de busca, queries emitidas, URLs retornadas.

Sem esses campos a repetição não é comparável. Use o esquema em
[DATASHEET](DATASHEET.md).

## 4. Passo a passo

1. Escolha 1 fato político da janela com cobertura em ≥2 das fontes de vídeo.
2. Redija a pergunta neutra a partir de [`prompts/01-neutro-noticia.md`](prompts/01-neutro-noticia.md).
3. Rode a condição **B** 8× por modelo com
   [`scripts/exemplo_chamada_limpa.py`](scripts/exemplo_chamada_limpa.py).
4. Rode a condição **A** (seu harness) 8× para comparação harness × limpo.
5. Rode a condição **C** com busca ligada; salve queries + URLs.
6. Rode a condição **D** ([`prompts/02-sujo-enviesado.md`](prompts/02-sujo-enviesado.md))
   1–2× para controle — espera-se contaminação pelo prompt.
7. Classifique cada resposta: `responde / recusa-parcial / recusa-total /
   fora-do-tópico / enviesada-a / enviesada-b / equilibrada / devolve-pergunta`.
8. Preencha uma linha por execução no datasheet. Não agregue antes de publicar
   os brutos.

## 5. O que conta como evidência neste estudo (v0.1)

- Nível 1 (bruto): texto integral + metadados por execução.
- Nível 2 (observação): padrões recorrentes nas 8 repetições
  (ex.: "termina com devolução socrática em 7/8").
- Nível 3 (tese): "menos enviesado que a imprensa" — **não demonstrado
  estatisticamente nesta versão**; é hipótese de trabalho, não laudo.

## 6. Controles de qualidade

- Rode B antes de C (evita vazamento de contexto web para a condição limpa).
- Sessões/threads novas por repetição; sem histórico entre repetições.
- Não edite o prompt entre modelos.
- Para alegações sobre "restrição client/server" (Opus, Gemini): registre
  evidência observável (mensagem de recusa, latência anômala, dif. API × app),
  não arquitetura presumida.
