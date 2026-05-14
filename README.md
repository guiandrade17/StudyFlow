<div align="center">

<img src="https://img.shields.io/badge/Study_Flow-1.0.0-4f8ef7?style=for-the-badge&logo=bookstack&logoColor=white" alt="Study Flow"/>

# 📚 Study Flow

### Organizador inteligente de revisões para estudantes

[![Deploy](https://img.shields.io/badge/🌐_Deploy-GitHub_Pages-222?style=for-the-badge&logo=github&logoColor=white)](https://guiandrade17.github.io/StudyFlow)
[![Repositório](https://img.shields.io/badge/📁_Repositório-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/guiandrade17/StudyFlow)
[![Licença](https://img.shields.io/badge/Licença-MIT-green?style=for-the-badge)](LICENSE)

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-passing-brightgreen?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org/)
[![Ruff](https://img.shields.io/badge/Ruff-lint_OK-D7FF64?style=flat-square&logo=ruff&logoColor=black)](https://docs.astral.sh/ruff/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/guiandrade17/StudyFlow/actions)
[![HTML5](https://img.shields.io/badge/Web-HTML%2FCSS%2FJS-E34F26?style=flat-square&logo=html5&logoColor=white)](#)

</div>

---

## 📌 Sobre o Projeto

Muitos estudantes enfrentam dificuldades para organizar sua rotina e definir **quando revisar** conteúdos já estudados. A falta de planejamento compromete a retenção do conhecimento e o desempenho acadêmico.

O **Study Flow** resolve esse problema oferecendo uma aplicação que **calcula automaticamente a próxima data de revisão** com base no intervalo de dias informado. Disponível tanto como ferramenta de linha de comando (CLI) quanto como aplicação web moderna.

---

## 💡 Proposta de Valor

> _"Estudar sem revisar é como encher um balde furado."_

O Study Flow aplica o conceito de **revisão espaçada**, ajudando o estudante a:

- 📅 Planejar revisões com datas calculadas automaticamente
- 📝 Manter um histórico organizado dos conteúdos estudados
- 💬 Receber frases motivacionais durante os estudos
- 🌐 Usar tanto pelo terminal quanto pelo navegador

---

## 👥 Público-Alvo

| Perfil | Benefício |
|---|---|
| 🎓 Estudantes do ensino médio | Organização para vestibulares e ENEM |
| 🏫 Universitários | Controle de revisões por disciplina |
| 📖 Autodidatas | Rotina de estudos estruturada |

---

## ⚙️ Funcionalidades

### 🖥️ Versão CLI (Python)
- [x] Calcular a próxima data de revisão
- [x] Interface interativa via terminal
- [x] Tratamento robusto de entradas inválidas
- [x] Integração com API de frases motivacionais

### 🌐 Versão Web
- [x] Interface moderna e responsiva
- [x] Histórico de revisões salvo com `localStorage`
- [x] Integração com a [Quotable API](https://quotable.io/)
- [x] Deploy automatizado via GitHub Pages

### 🔧 Infraestrutura
- [x] Testes automatizados com Pytest
- [x] Análise estática com Ruff
- [x] Pipeline CI/CD com GitHub Actions

---

## 🛠️ Tecnologias Utilizadas

<div align="center">

| Camada | Tecnologia | Finalidade |
|---|---|---|
| **Backend / CLI** | Python 3.x | Lógica principal da aplicação |
| **Frontend** | HTML5, CSS3, JavaScript | Interface web responsiva |
| **Testes** | Pytest | Testes unitários automatizados |
| **Linting** | Ruff | Análise estática e padronização de código |
| **CI/CD** | GitHub Actions | Integração e entrega contínua |
| **Persistência** | localStorage | Histórico de revisões no navegador |
| **API Externa** | Quotable API | Frases motivacionais dinâmicas |
| **Deploy** | GitHub Pages | Hospedagem da versão web |

</div>

---

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Git instalado

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/guiandrade17/StudyFlow

# 2. Acesse o diretório do projeto
cd StudyFlow

# 3. Instale as dependências
py -m pip install -r requirements.txt
```

---

## ▶️ Execução

### CLI (linha de comando)

```bash
py -m src.main
```

### Web

Acesse diretamente pelo navegador:
**[https://guiandrade17.github.io/StudyFlow](https://guiandrade17.github.io/StudyFlow)**

Ou abra o arquivo `index.html` localmente no seu navegador.

---

## 💻 Exemplo de Uso

```
╔══════════════════════════════╗
║        STUDY FLOW  📚        ║
╚══════════════════════════════╝

  1 - Calcular próxima revisão
  2 - Sair

  Escolha uma opção: 1

  ──────────────────────────────
  Digite o número de dias: 3

  ✅  Próxima revisão: 30/03/2026
  💬  Frase do dia: "Continue estudando,
      você está no caminho certo!" 🚀
  ──────────────────────────────
```

---

## 🧪 Testes Automatizados

O projeto utiliza **Pytest** para garantir a confiabilidade das funcionalidades principais.

```bash
# Rodar todos os testes
py -m pytest

# Rodar com saída detalhada
py -m pytest -v
```

Exemplo de saída esperada:

```
collected 5 items

tests/test_main.py::test_calcular_revisao          PASSED
tests/test_main.py::test_entrada_invalida          PASSED
tests/test_main.py::test_data_futura               PASSED
...

5 passed in 0.42s
```

---

## 🧹 Análise Estática (Lint)

O projeto utiliza **Ruff** para garantir qualidade e padronização do código.

```bash
# Verificar problemas de lint
py -m ruff check .

# Corrigir problemas automaticamente
py -m ruff check . --fix
```

---

## 🔄 CI/CD com GitHub Actions

O pipeline de integração contínua é executado automaticamente a cada `push` ou `pull request` na branch `main`, realizando:

1. ✅ Instalação das dependências
2. ✅ Execução dos testes com Pytest
3. ✅ Verificação de lint com Ruff
4. ✅ Deploy automático no GitHub Pages

---

## 📁 Estrutura do Projeto

```
StudyFlow/
├── src/
│   └── main.py              # Lógica principal da CLI
├── tests/
│   └── test_main.py         # Testes automatizados
├── index.html               # Interface web
├── style.css                # Estilos da versão web
├── script.js                # Lógica da versão web
├── requirements.txt         # Dependências Python
├── .github/
│   └── workflows/
│       └── ci.yml           # Pipeline GitHub Actions
└── README.md
```

---

## 🔢 Versão

**v1.0.0** — Versão inicial com suporte a CLI, versão web, testes e CI/CD.

---

## 👤 Autor

<div align="center">

**Guilherme Brito Andrade**

[![GitHub](https://img.shields.io/badge/GitHub-guiandrade17-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/guiandrade17)

</div>

---

## 🔗 Links

| Recurso | URL |
|---|---|
| 🌐 Versão Web (Deploy) | [guiandrade17.github.io/StudyFlow](https://guiandrade17.github.io/StudyFlow) |
| 📁 Repositório | [github.com/guiandrade17/StudyFlow](https://github.com/guiandrade17/StudyFlow) |

---

<div align="center">

Desenvolvido com 📚 e ☕ por **Guilherme Brito Andrade**

</div>