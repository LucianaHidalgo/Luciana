# Contexto do projeto (memória)

Este repositório guarda uma **série de materiais explicativos em PDF** (português do
Brasil) sobre **como usar o Claude junto com o Google Ads**, produzidos a partir de
vídeos da **Mentoria Alvo** (apresentadora: Luciana).

O objetivo é transformar cada vídeo/trecho em um **guia passo a passo, com imagens
numeradas e sinalizadas com retângulos e setas vermelhas**, destacando tudo o que é
mencionado no áudio. Os materiais são pensados para serem lidos em sequência e
**integrados** conforme novos vídeos chegam.

## Preferência da usuária (SEMPRE)
- **Todo pedido deve ser entregue com o PDF pronto para baixar** no chat (enviar o
  arquivo com a ferramenta de envio de arquivo / `display: attach`), além de salvar
  no repositório. Nunca só descrever o resultado: sempre anexar o PDF baixável.

## Onde ficam os materiais
- Pasta `materiais/` — ver `materiais/README.md` para o índice completo e o padrão
  visual dos guias.

## Guia Completo (vídeo inteiro)
- **`materiais/00-guia-completo/Guia_Completo_Claude_Google_Ads.pdf`** — guia único do
  vídeo completo de 1h25 ("Explicação do Claude.mp4", baixado do Google Drive via link).
  **Fundo branco com detalhes verde e dourado** (padrão pedido pela usuária para este
  guia), 22 páginas, 19 passos em 6 seções: assinar/instalar; painel no Google Ads;
  comando + Claude trabalhando; modelo/esforço/pensamento + diagnóstico do CPC +
  recomendações; prints/planilhas + Memória; Projetos + Regras de Ouro. Consolida as
  Partes 1–4 num só material.
- Vídeos grandes (>~100 MB) não sobem pelo chat: a usuária envia por link do Google
  Drive e eu baixo direto com `curl` (endpoint `drive.usercontent.google.com/download?
  id=<ID>&export=download&confirm=t`), processo com ffmpeg/faster-whisper e monto o PDF.

## Estado atual da série
- **Parte 1** (`materiais/01-extensao-claude-chrome/`): instalar a extensão "Claude
  para Chrome" e abrir o painel sobre o Google Ads. Termina ao abrir o painel.
- **Parte 2** (`materiais/02-painel-claude-google-ads/`): usar o painel já aberto —
  permitir acesso à tela, chat, modelo (Sonnet 5) e botão "+" (anexar). Termina na
  apresentação do botão "+".
- **Parte 3** (`materiais/03-comandos-analise-claude/`): o que o "+" aceita
  (texto/imagem, não vídeo), comando por voz (microfone), escrever o comando de
  análise (CPC alto → como diminuir), Claude trabalhando sozinho ("começou a depurar
  o navegador", X ações) e o modo de aprovação (manual x automático). Termina com o
  Claude analisando em modo automático.
- **Parte 4** (`materiais/04-modelos-e-resultado-analise/`): manter "aprovar
  automaticamente", seletor de modelos (Sonnet 5 x Fable/Opus/Haiku), esforço e
  pensamento, deixar analisar (pode demorar) e o resultado — diagnóstico do CPC alto
  (estratégia "Maximizar cliques" no teto de R$ 0,60) + recomendações (reduzir o CPC
  máximo / trocar para "Maximizar conversões"; pode pedir "faz para mim").
- **Próxima parte:** aplicar os ajustes recomendados (reduzir CPC máximo / trocar
  estratégia), manual ou pedindo ao Claude (aguardando material).

## Padrão a manter em novos materiais
1. PDF A4, capa "Mentoria Alvo" (verde + dourado).
2. Página de legenda "Como ler este guia" (retângulo vermelho, seta vermelha, número).
3. Um passo por página: emblema numerado + título + captura anotada em vermelho +
   explicação; callouts para dicas/avisos.
4. Fazer a **ponte com a parte anterior** (de onde a explicação parou).
5. Atualizar `materiais/README.md` e este arquivo.

## Como os PDFs são gerados (ferramentas)
- Extração de quadros e áudio do vídeo com **ffmpeg**.
- Transcrição do áudio com **faster-whisper** (modelo `small`, pt-BR).
- Anotação das imagens (retângulos/setas/emblemas vermelhos) com **Pillow (PIL)**.
- Montagem do PDF com **reportlab** (fontes DejaVu Sans / Liberation).

## Branch de trabalho
- Desenvolver na branch `claude/pdf-material-explicativo-wl0378`.
