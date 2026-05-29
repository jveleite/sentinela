# 🛡️ Sentinela

Monitor automatizado de incidentes para fluxos comerciais.

Desenvolvido em Python + PostgreSQL, o Sentinela analisa pedidos de venda,
detecta anomalias via regras de negócio configuráveis e gera relatórios
classificados por severidade (1-5).

---

## 🎯 Problema que resolve

Em fluxos comerciais com alto volume de pedidos (PF, PJ),
incidentes como pedidos travados na integração, pendências vencidas e
inconsistências de status passam despercebidos até virarem reclamação.

O Sentinela monitora continuamente e detecta esses problemas antes que
impactem o cliente.

---

## 🏗️ Arquitetura
banco/          → scripts SQL (criação e população)
sentinela/
├── db.py       → conexão com PostgreSQL
├── models.py   → classe Pedido
├── repository.py → queries ao banco
├── regras.py   → regras de negócio e classe Incidente
├── motor.py    → orquestra a avaliação dos pedidos
├── relatorio.py → geração do relatório de saída
├── logger.py   → logging estruturado
└── main.py     → ponto de entrada
tests/          → testes automatizados com pytest

### Princípios aplicados
- Separação de responsabilidades por camada
- Regras de negócio isoladas e testáveis sem banco
- Configuração externa via `.env`
- Princípio aberto-fechado: novas regras sem alterar o motor

---

## ⚙️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.14 | Linguagem principal |
| PostgreSQL 17 | Banco de dados |
| psycopg2 | Driver Python → PostgreSQL |
| pytest | Testes automatizados |
| python-dotenv | Configuração externa |

---

## 🚀 Como rodar

### Pré-requisitos
- Python 3.12+
- PostgreSQL 17

### Instalação

```bash
git clone https://github.com/seu-usuario/sentinela.git
cd sentinela
pip install -r requirements.txt
```

### Configuração

Cria um arquivo `.env` na raiz:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sentinela
DB_USER=postgres
DB_PASSWORD=sua_senha
LOG_LEVEL=INFO

### Banco de dados

```bash
psql -U postgres -c "CREATE DATABASE sentinela;"
psql -U postgres -d sentinela -f banco/01_criar_tabelas.sql
psql -U postgres -d sentinela -f banco/02_popular_dados.sql
```

### Execução

```bash
cd sentinela
python main.py
```

### Testes

```bash
pytest tests/ -v
```

---

## 📊 Exemplo de saída

============================================================
SENTINELA — RELATÓRIO DE INCIDENTES
Gerado em: 29/05/2026 09:21
Pedidos analisados  : 8
Incidentes detectados: 7
[ SEVERIDADE 4 ]
Pedido  : SS-0002 (SUPERSIMPLES)
Tipo    : TRAVADO_INTEGRACAO
Detalhe : Parado há 38h na integração (limite: 6h)
---

## 🔍 Regras de negócio implementadas

| Regra | Condição | Severidade |
|---|---|---|
| Travado na integração | Status INTEGRACAO + tempo > limite | 4 |
| Pendência vencida | Pendência aberta + tempo > limite | 3 |
| Inconsistência de status | APROVADO com pendência aberta | 5 |

---

## 🗺️ Roadmap

- [x] Modelagem do banco de dados
- [x] Conexão Python → PostgreSQL
- [x] Motor de regras de negócio
- [x] Relatório formatado
- [x] Logging estruturado
- [x] Testes automatizados
- [ ] Containerização com Docker
- [ ] Camada de IA (resumo de triagem + card Azure DevOps)

---

## 👤 Autor

**João Victor Melo Leite** — Analista funcional em transição para desenvolvimento.
