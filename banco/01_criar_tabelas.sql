-- =============================================
-- Sentinela: criação das tabelas
-- Fase 1 | autor: Kilmer
-- =============================================

CREATE TABLE IF NOT EXISTS pedido_venda (
    id               SERIAL PRIMARY KEY,
    codigo           VARCHAR(20)  NOT NULL UNIQUE,
    tipo_fluxo       VARCHAR(20)  NOT NULL,
    status_atual     VARCHAR(30)  NOT NULL,
    criado_em        TIMESTAMP    NOT NULL DEFAULT NOW(),
    atualizado_em    TIMESTAMP    NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS status_historico (
    id          SERIAL PRIMARY KEY,
    pedido_id   INTEGER      NOT NULL REFERENCES pedido_venda(id),
    status      VARCHAR(30)  NOT NULL,
    entrou_em   TIMESTAMP    NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS pendencia (
    id          SERIAL PRIMARY KEY,
    pedido_id   INTEGER      NOT NULL REFERENCES pedido_venda(id),
    tipo        VARCHAR(50)  NOT NULL,
    resolvida   BOOLEAN      NOT NULL DEFAULT FALSE,
    aberta_em   TIMESTAMP    NOT NULL DEFAULT NOW()
);