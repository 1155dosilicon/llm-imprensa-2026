# Limitações e ética

1. **Amostra pequena, sem estatística.** 8 repetições por célula e um único
   avaliador (o autor) não sustentam generalização. A tese "LLMs menos
   enviesadas que a imprensa" é hipótese de trabalho.
2. **Corpus de imprensa enviesado por construção.** Excluir 4 veículos e partir
   de 4 vídeos escolhe o adversário. Qualquer replicação deve variar o corpus.
3. **Snapshots mudam.** Os 7 modelos foram verificados como reais via
   catálogo do OpenRouter em 18/09/2026 (IDs no README), mas provedores
   atualizam snapshots por trás do mesmo nome. Sempre registrar o ID exato
   e a data da execução.
4. **Harness × API limpa.** O efeito "performaram parecidos" precisa dos dois
   conjuntos de brutos para ser crível.
5. **Hipótese "client-side" não testada.** Dizer que Opus/Gemini têm restrição
   extra de inferência exige comparar API × app com logs — hoje é conjectura.
6. **"Fora do tópico" ≠ incapacidade.** Resposta evasiva em modelo chinês pode
   ser filtro de segurança, tradução, ou prompt mal adaptado ao modelo.
7. **Ano eleitoral.** 2026 é ano eleitoral no Brasil; cobertura e moderação de
   modelos mudam ao longo do ano. Data cada execução.
8. **Reuso responsável.** Não use os prompts "sujos" fora do controle
   metodológico; não exponha pessoas reais nos exemplos publicados sem
   necessidade; arquive fontes (vídeos saem do ar).
9. **Jurídico.** Nada aqui é parecer legal. A pergunta sobre patrocínio de
   matéria tendenciosa exige jurista e caso concreto.
