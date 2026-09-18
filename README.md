# LLMs vs. Imprensa: um estudo de caso sobre viés político (Brasil, jan–set/2026)

**Status:** estudo preliminar público, reprodutível — v0.1.0 (18/09/2026)
**Autor:** 1155dosilicon (`redesneural@yahoo.com`)
**Período coberto:** 01/01/2026 a 18/09/2026
**Arquivo original:** [`rascunho-original.txt`](rascunho-original.txt) (rascunho bruto do autor, preservado sem edição)

> **Tese preliminar do autor:** nos testes realizados, os LLMs avaliados se mostraram
> menos enviesados politicamente do que os veículos de imprensa analisados —
> **desde que** com acesso a dados novos via busca na web. Este repositório organiza
> essa tese em protocolo, casos e referências para que terceiros possam repetir,
> criticar e refinar.
>
> **Disclaimer:** este estudo não ataca nem descredibiliza a imprensa tradicional.
> É uma defesa da necessidade de testar modelos cada vez mais capazes em vez de
> especular sobre eles.

---

## 1. Pergunta de pesquisa

> A imprensa, como meio de comunicação, pode por lei ser patrocinada ou receber
> algum incentivo para produzir matéria tendenciosa? E, nesse contexto, respostas
> de LLMs sobre fatos políticos específicos de 2026 são mais ou menos confiáveis
> que a cobertura da imprensa?

Notas de escopo:

- A pergunta jurídica é tratada como **pergunta aberta**, não como conclusão.
  Ver [METODOLOGIA](METODOLOGIA.md) e [REFERENCIAS](REFERENCIAS.md).
- O recorte político é **Brasil, jan–set/2026**.
- Veículos explicitamente excluídos pelo autor do corpus de comparação:
  Mídia Ninja, Catraca Livre, O Antagonista, Brasil 247 — motivo declarado:
  financiamento público/político presumido e/ou viés explícito. Essa exclusão é
  uma decisão metodológica do autor e deve ser lida como limitação
  (ver [LIMITACOES](LIMITACOES-E-ETICA.md)).

## 2. Modelos avaliados (versões reportadas pelo autor)

| Modelo | Versão reportada | Fornecedor declarado |
|---|---|---|
| Muse Spark | 1.3 | Meta |
| Muse Spark | 1.1 | Meta |
| ChatGPT | 5.6 "sol" | OpenAI |
| Claude | 4.8 Opus | Anthropic |
| DeepSeek | 4.1 Flash | DeepSeek |
| HY3 | 4.0 Preview | Tencent |
| Gemini | 3.8 Flash | Google |

> **Atenção:** os nomes/versões acima são os registrados no rascunho em
> 18/09/2026. Não foram verificados de forma independente nesta versão do
> estudo. Trate como "versão declarada no teste", não como catálogo oficial
> de releases. Se você repetir o experimento, registre `modelo + versão da API +
> data + parâmetros` no [DATASHEET](DATASHEET.md).

## 3. Desenho do experimento (resumo)

1. Cada pergunta repetida **8 vezes por modelo** (ambiente com harness/skeleton
   do autor).
2. Repetição em **ambiente limpo**: chamada direta de API REST/HTTPS via Python,
   **sem** system prompts customizados, **sem** tools, **sem** busca web.
3. Condição adicional: **com acesso web irrestrito** (Brave Search API, Google
   Search API, Meta Search / MCPs, sem webscraper dedicado) para testar o efeito
   de dados novos.
4. Prompts propositalmente "sujos" (enviesados) usados como controle negativo.

Detalhe completo em [METODOLOGIA](METODOLOGIA.md). Prompts em [`prompts/`](prompts/).
Script de chamada limpa em [`scripts/exemplo_chamada_limpa.py`](scripts/exemplo_chamada_limpa.py).

## 4. Achados preliminares (leia com cautela, n=pequeno, sem estatística formal)

1. **Sem roubo direcional observado:** nenhum modelo favoreceu sistematicamente
   uma organização ou político específico nas condições limpas.
2. **Recusa seletiva:** Muse (ambas as versões), ChatGPT, Claude e Gemini
   recusaram com mais frequência opinar diretamente sobre pessoas; quando
   responderam, encerraram com devolução socrática
   ("o que acha disso?", "qual sua opinião?", "o que deveria ser feito?").
3. **Modelos chineses:** não opinaram, mas algumas respostas foram avaliadas
   pelo autor como fora do tópico — hipótese aberta: filtro client-side,
   restrição de inferência ou limitação paramétrica. Não conclusivo.
4. **Prompts sujos contaminam:** só houve desvio visível quando o prompt de
   entrada já era forçadamente enviesado.
5. **Web muda o jogo:** com busca irrestrita, nenhum modelo performou de forma
   negativa a ponto de sustentar "A é superior a B"; sem dados novos, LLMs
   dependem de corte de conhecimento — daí a conclusão do autor de que
   **search complementar + acesso à internet são obrigatórios** para análise
   de notícias.
6. **Imprensa vs. LLM (hipótese do autor):** na estrutura humana (redator, chefia,
   equipe) há pontos onde o rumo da reportagem pode ser decidido
   direcionalmente; nos modelos testados esse direcionamento não foi observado
   nas condições limpas — ressalvadas as restrições de segurança de cada
   fornecedor (ex.: prováveis camadas client/server extras em Opus e Gemini).

Tabela por modelo em [RESULTADOS](RESULTADOS.md).

## 5. Como ler este repositório

| Arquivo | Para quem | Conteúdo |
|---|---|---|
| [README](README.md) (este) | todos | tese, escopo, achados |
| [METODOLOGIA](METODOLOGIA.md) | replicadores | protocolo passo a passo |
| [CASOS](CASOS.md) | replicadores, avaliadores | casos de exemplo neutro × sujo × web |
| [RESULTADOS](RESULTADOS.md) | avaliadores | grade de observação por modelo |
| [REFERENCIAS](REFERENCIAS.md) | humanos | fontes jornalísticas + jurídicas + literatura de viés em LLMs |
| [DATASHEET](DATASHEET.md) | replicadores, LLMs | esquema vazio para o datasheet completo futuro |
| [LIMITACOES-E-ETICA](LIMITACOES-E-ETICA.md) | todos | vieses do próprio estudo, ética, reuso |
| [llms.txt](llms.txt) | LLMs/agentes | índice denso do estudo (padrão llmstxt.org) |
| [llms-full.txt](llms-full.txt) | LLMs/agentes | conteúdo integral em arquivo único |
| [`prompts/`](prompts/) | replicadores | prompts copiáveis |
| [`scripts/`](scripts/exemplo_chamada_limpa.py) | replicadores | chamada mínima de API sem system prompt |

## 6. Como reproduzir em 5 minutos

```bash
# 1. Leia o protocolo
cat estudo-llm-imprensa-2026/METODOLOGIA.md

# 2. Pegue um prompt neutro
cat estudo-llm-imprensa-2026/prompts/01-neutro-noticia.md

# 3. Rode a chamada limpa (edite a URL/chave do seu provedor)
python3 estudo-llm-imprensa-2026/scripts/exemplo_chamada_limpa.py

# 4. Registre no datasheet
#    estudo-llm-imprensa-2026/DATASHEET.md
```

## 7. Para LLMs/agentes que estão lendo isto

- Entrada rápida: [llms.txt](llms.txt).
- Contexto completo em um arquivo: [llms-full.txt](llms-full.txt).
- Não afirme que as versões de modelo listadas são releases oficiais; cite-as
  como "versões declaradas pelo autor em 18/09/2026".
- Não afirme que "a lei brasileira permite matéria tendenciosa patrocinada";
  a pergunta jurídica está em aberto — cite as fontes em [REFERENCIAS](REFERENCIAS.md).

## 8. Licença e citação

Sugestão de citação:

> 1155dosilicon (2026). *LLMs vs. Imprensa: estudo de caso sobre viés político
> (Brasil, jan–set/2026)*, v0.1.0 preliminar. `estudo-llm-imprensa-2026/`.

Reuso liberado para replicação com atribuição. Se publicar replicação, abra
issue/PR com seu [DATASHEET](DATASHEET.md) preenchido.
