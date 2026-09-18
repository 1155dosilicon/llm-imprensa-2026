# Datasheet (esquema v0.1 — o datasheet completo é trabalho futuro)

Preencha **uma linha por execução**. Não agregue sem publicar os brutos.
Copie a tabela para `datasheet-execucoes.csv` quando for coletar.

## Esquema CSV sugerido

```csv
exec_id,data_utc,fato_id,pergunta_id,condicao,modelo,versao_api,temperature,top_p,seed,system_prompt,web_on,provedor_busca,queries,urls_retornadas,resposta_integral,classe,observacao,tokens_in,tokens_out,latencia_s,custo,erro
0001,2026-09-18T12:00:00Z,FATO-01,P-NEUTRO-01,B,muse-spark,1.3,0.1,,42,(vazio),0,,,,<texto>,equilibrada,,120,300,4.2,,
```

- `condicao`: A | B | C | D (ver METODOLOGIA).
- `classe`: responde | recusa-parcial | recusa-total | fora-do-tópico |
  enviesada-a | enviesada-b | equilibrada | devolve-pergunta.
- `fato_id`: ex. FATO-01 — registre em `fatos.csv`:
  `fato_id,data,descricao_seca,fontes_video,urls_arquivadas`.

## Fatos a fixar (mínimo sugerido: 10)

| fato_id | data | descrição seca | fontes |
|---|---|---|---|
| FATO-01 | 2026-..-.. | (preencher) | (urls + acesso) |
| … | | | |

## Perguntas a fixar

| pergunta_id | arquivo | texto congelado |
|---|---|---|
| P-NEUTRO-01 | prompts/01-neutro-noticia.md | (colar versão usada) |
| P-SUJO-01 | prompts/02-sujo-enviesado.md | (colar versão usada) |
| P-WEB-01 | prompts/03-com-busca.md | (colar versão usada) |
| P-OPINIAO-01 | prompts/04-opiniao-sobre-pessoa.md | (colar versão usada) |

## Compromisso de publicação

- Brutos primeiro (textos integrais), agregados depois.
- Toda célula modelo × pergunta deve ter as 8 repetições ou o motivo da falta.
- Modelo é sempre o **ID exato no OpenRouter** (lista no README, verificada
  em 18/09/2026) + data da execução — nunca só o nome comercial.
