# Classificador de urgência com o Jev

Script que usa o **Jev** (modelo de decisão da TypeSafe) para separar mensagens de alunos em
**urgente** e **não urgente**. Se o Jev tiver pouca confiança (menos de 60%), a mensagem vai para **revisão humana**.

## Pré-requisitos

1. Python 3.10 ou mais recente (sem bibliotecas extras).
2. Uma chave de API da TypeSafe (console.typesafe.ai). O cadastro de novas contas pode estar
   pausado ou ter lista de espera.

## Como usar

```bash
export TYPESAFE_API_KEY="sua-chave"
python classificar_urgencia.py mensagens_exemplo.json
```

Para ver o que seria enviado, sem chave:

```bash
python classificar_urgencia.py mensagens_exemplo.json --dry-run
```

## Como ajustar

- **O que conta como urgente:** edite os textos de `criteria` em `PERGUNTAS`, dentro de `classificar_urgencia.py`.
- **Quando mandar para revisão humana:** mude `CONFIANCA_MINIMA`.
- **Suas mensagens:** troque o arquivo `mensagens_exemplo.json` por um com o mesmo formato
  (`[{"aluno": "...", "mensagem": "..."}]`).

## Usando com o Claude Code

Com a skill oficial da TypeSafe instalada, o Claude Code já sabe chamar o Jev:

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```
