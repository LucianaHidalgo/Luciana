# Série de Materiais Explicativos — Claude + Google Ads (Mentoria Alvo)

Esta pasta reúne os materiais explicativos (PDFs em português, passo a passo, com
capturas de tela numeradas e sinalizadas com **retângulos e setas vermelhas**)
criados a partir dos vídeos da mentoria. Cada material corresponde a uma parte/etapa
da explicação e foi feito para ser lido em sequência.

## Padrão visual dos guias
- Formato **A4 (retrato)**, PDF.
- **Capa** com identidade "Mentoria Alvo" (verde + dourado).
- Página **"Como ler este guia"** com a legenda: retângulo vermelho (destaca o
  elemento citado), seta vermelha (para onde olhar/clicar) e número do passo.
- **Um passo por página**: emblema numerado + título, captura de tela anotada em
  vermelho e explicação em texto.
- **Callouts** (caixas de observação) para dicas, avisos e variações.
- Rodapé: "Guia elaborado a partir de gravação de tela".

## Índice da série

| # | Pasta | Material | Conteúdo | Status |
|---|-------|----------|----------|--------|
| 1 | `01-extensao-claude-chrome/` | `Guia_Claude_Extensao_Chrome.pdf` | Assinar o plano pago, instalar a extensão "Claude para Chrome", fixá-la na barra e abrir o painel sobre o Google Ads. Termina no momento em que o painel é aberto (Passo 11). | ✅ Concluído |
| 2 | `02-painel-claude-google-ads/` | `Guia_Claude_Painel_Google_Ads_Parte2.pdf` | **Continua a Parte 1.** Com o painel já aberto: permitir o acesso à tela, entender que o Claude enxerga a campanha, conversar pelo chat, escolher o modelo (Sonnet 5) e usar o "+" para anexar arquivos. Termina na apresentação do botão "+". | ✅ Concluído |
| 3 | `03-comandos-analise-claude/` | `Guia_Claude_Comandos_Analise_Parte3.pdf` | **Continua a Parte 2.** O que o "+" aceita (texto/imagem, não vídeo), comando por voz (microfone), escrever o comando de análise (ex.: "por que o CPC está tão alto e como diminuir"), acompanhar o Claude trabalhando sozinho ("começou a depurar o navegador", X ações, navega até Palavras-chave/Configurações) e escolher o modo de aprovação (manual x automático x ignorar todas). Termina com o Claude analisando em modo automático. | ✅ Concluído |
| 4 | `04-modelos-e-resultado-analise/` | `Guia_Claude_Modelos_e_Analise_Parte4.pdf` | **Continua a Parte 3.** Manter "Aprovar automaticamente"; seletor de modelos (Sonnet 5 no dia a dia; Fable/Opus para tarefas complexas, consomem mais uso); esforço (Alto = padrão) e pensamento; deixar analisar (pode demorar ~20 min, é normal); e o resultado: diagnóstico do CPC alto (estratégia "Maximizar cliques" batendo no teto de CPC R$ 0,60, média R$ 0,57) + recomendações (reduzir o CPC máximo gradualmente / trocar para "Maximizar conversões" / melhorar página de destino; pode pedir "faz para mim"). | ✅ Concluído |
| 5 | _(a definir)_ | _(a definir)_ | Continuação — aplicar os ajustes (reduzir CPC máximo / trocar estratégia), manual ou pedindo ao Claude. Aguardando novo vídeo/material. | ⏳ Pendente |

## Como a série se conecta (continuidade)
- **Parte 1 → Parte 2:** a Parte 1 termina exatamente quando o painel do Claude é
  aberto sobre o Google Ads. A Parte 2 começa desse ponto (permissão de acesso à tela).
- **Parte 2 → Parte 3:** a Parte 2 termina quando o botão "+" (anexar arquivo) é
  apresentado. A Parte 3 começa daí (o que o "+" aceita) e mostra o Claude analisando
  a campanha de fato.
- **Parte 3 → Parte 4:** a Parte 3 termina com o Claude trabalhando sozinho (modo
  automático). A Parte 4 mostra a configuração (modelos/esforço/pensamento) e o
  resultado: o diagnóstico do CPC + as recomendações.
- **Parte 4 → próximas partes:** a Parte 4 termina com o diagnóstico e as recomendações
  entregues. O próximo material deve continuar aplicando os ajustes (reduzir o CPC
  máximo / trocar a estratégia), manualmente ou pedindo ao Claude ("faz para mim").

## Instruções para novos materiais (integração)
Quando um novo vídeo/trecho for enviado:
1. Criar uma nova pasta numerada (`03-...`, `04-...`).
2. Manter **o mesmo padrão visual** descrito acima (capa, legenda, um passo por
   página, sinalização vermelha, callouts, rodapé).
3. Começar o material fazendo a **ponte com a parte anterior** (de onde a explicação
   parou), como a Parte 2 faz com a Parte 1.
4. Atualizar o índice acima e o arquivo `CLAUDE.md` na raiz do repositório.
