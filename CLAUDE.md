# Contexto do projeto (memória)

Este repositório guarda uma **série de materiais explicativos em PDF** (português do
Brasil) sobre **como usar o Claude junto com o Google Ads**, produzidos a partir de
vídeos da **Mentoria Alvo** (apresentadora: Luciana).

O objetivo é transformar cada vídeo/trecho em um **guia passo a passo, com imagens
numeradas e sinalizadas com retângulos e setas vermelhas**, destacando tudo o que é
mencionado no áudio. Os materiais são pensados para serem lidos em sequência e
**integrados** conforme novos vídeos chegam.

## Onde ficam os materiais
- Pasta `materiais/` — ver `materiais/README.md` para o índice completo e o padrão
  visual dos guias.

## Estado atual da série
- **Parte 1** (`materiais/01-extensao-claude-chrome/`): instalar a extensão "Claude
  para Chrome" e abrir o painel sobre o Google Ads. Termina ao abrir o painel.
- **Parte 2** (`materiais/02-painel-claude-google-ads/`): usar o painel já aberto —
  permitir acesso à tela, chat, modelo (Sonnet 5) e botão "+" (anexar). Termina na
  apresentação do botão "+".
- **Próxima parte:** continuar a partir do uso do "+"/anexos (aguardando material).

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
