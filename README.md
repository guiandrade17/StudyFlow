# Study Flow
Projeto desenvolvido para organização de estudos com revisões automatizadas.

![CI](https://github.com/guiandrade17/StudyFlow/actions/workflows/ci.yml/badge.svg)

## 📌 Descrição do Problema

Muitos estudantes enfrentam dificuldades para organizar sua rotina de estudos e definir quando revisar conteúdos já estudados. A falta de planejamento compromete a retenção do conhecimento e o desempenho acadêmico.

## 💡 Proposta da Solução

O Study Flow é uma aplicação em linha de comando (CLI) que auxilia estudantes no planejamento de revisões. A aplicação calcula automaticamente a próxima data de revisão com base na quantidade de dias informada pelo usuário.

## 👥 Público-Alvo

- Estudantes
- Universitários
- Pessoas que desejam melhorar a organização dos estudos

## ⚙️ Funcionalidades Principais

- Calcular a próxima data de revisão
- Interface simples via terminal (CLI)
- Tratamento de entradas inválidas

## 🛠️ Tecnologias Utilizadas

- Python
- Pytest (testes automatizados)
- Ruff (linting/análise estática)
- GitHub Actions (Integração Contínua)

## 📦 Instruções de Instalação

Clone o repositório:

```bash
git clone https://github.com/guiandrade17/StudyFlow
cd StudyFlow

Instale as dependências:
py -m pip install -r requirements.txt

▶️ Instruções de Execução
py -m src.main

💻 Exemplo de Uso
=== Study Flow ===
1 - Calcular próxima revisão
2 - Sair
Digite o número de dias: 3
Próxima revisão: 30/03/2026

🧪 Instruções para Rodar os Testes
py -m pytest

🧹 Instruções para Rodar o Lint
<<<<<<< HEAD
py -m ruff check . --no-cache
=======
py -m ruff check . 
>>>>>>> main

🔢 Versão Atual
1.0.0

👤 Autor
Guilherme Brito Andrade

🔗 Link do Repositório Público
https://github.com/guiandrade17/StudyFlow


---
