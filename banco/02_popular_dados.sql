-- =============================================
-- Sentinela: dados sintéticos
-- Fase 1 | autor: Kilmer
-- =============================================

-- Pedidos de venda
INSERT INTO pedido_venda (codigo, tipo_fluxo, status_atual, criado_em, atualizado_em) VALUES
('PF-0001', 'PF',         'APROVADO',    NOW() - INTERVAL '2 days',  NOW() - INTERVAL '1 hour'),
('PF-0002', 'PF',         'INTEGRACAO',  NOW() - INTERVAL '3 days',  NOW() - INTERVAL '10 hours'),
('PME-001', 'PME',        'INTEGRACAO',  NOW() - INTERVAL '5 days',  NOW() - INTERVAL '12 hours'),
('PME-002', 'PME',        'ANALISE',     NOW() - INTERVAL '1 day',   NOW() - INTERVAL '2 hours'),
('SS-0001', 'SUPERSIMPLES','APROVADO',   NOW() - INTERVAL '4 days',  NOW() - INTERVAL '30 minutes'),
('SS-0002', 'SUPERSIMPLES','INTEGRACAO', NOW() - INTERVAL '6 days',  NOW() - INTERVAL '20 hours'),
('PF-0003', 'PF',         'ANALISE',     NOW() - INTERVAL '1 day',   NOW() - INTERVAL '1 hour'),
('PME-003', 'PME',        'APROVADO',    NOW() - INTERVAL '3 days',  NOW() - INTERVAL '3 hours');

-- Histórico de status
INSERT INTO status_historico (pedido_id, status, entrou_em) VALUES
(1, 'RECEBIDO',   NOW() - INTERVAL '2 days'),
(1, 'ANALISE',    NOW() - INTERVAL '2 days' + INTERVAL '1 hour'),
(1, 'APROVADO',   NOW() - INTERVAL '1 day'),
(2, 'RECEBIDO',   NOW() - INTERVAL '3 days'),
(2, 'ANALISE',    NOW() - INTERVAL '3 days' + INTERVAL '2 hours'),
(2, 'INTEGRACAO', NOW() - INTERVAL '2 days'),
(3, 'RECEBIDO',   NOW() - INTERVAL '5 days'),
(3, 'ANALISE',    NOW() - INTERVAL '4 days'),
(3, 'INTEGRACAO', NOW() - INTERVAL '3 days'),
(4, 'RECEBIDO',   NOW() - INTERVAL '1 day'),
(4, 'ANALISE',    NOW() - INTERVAL '20 hours'),
(5, 'RECEBIDO',   NOW() - INTERVAL '4 days'),
(5, 'ANALISE',    NOW() - INTERVAL '3 days'),
(5, 'APROVADO',   NOW() - INTERVAL '2 days'),
(6, 'RECEBIDO',   NOW() - INTERVAL '6 days'),
(6, 'ANALISE',    NOW() - INTERVAL '5 days'),
(6, 'INTEGRACAO', NOW() - INTERVAL '4 days'),
(7, 'RECEBIDO',   NOW() - INTERVAL '1 day'),
(7, 'ANALISE',    NOW() - INTERVAL '18 hours'),
(8, 'RECEBIDO',   NOW() - INTERVAL '3 days'),
(8, 'ANALISE',    NOW() - INTERVAL '2 days'),
(8, 'APROVADO',   NOW() - INTERVAL '1 day');

-- Pendências
INSERT INTO pendencia (pedido_id, tipo, resolvida, aberta_em) VALUES
(2, 'DOCUMENTO_PENDENTE',   FALSE, NOW() - INTERVAL '2 days'),
(3, 'ASSINATURA_PENDENTE',  FALSE, NOW() - INTERVAL '3 days'),
(3, 'DOCUMENTO_PENDENTE',   FALSE, NOW() - INTERVAL '2 days'),
(4, 'CADASTRO_INCOMPLETO',  FALSE, NOW() - INTERVAL '18 hours'),
(5, 'DOCUMENTO_PENDENTE',   TRUE,  NOW() - INTERVAL '3 days'),
(6, 'ASSINATURA_PENDENTE',  FALSE, NOW() - INTERVAL '4 days'),
(8, 'DOCUMENTO_PENDENTE',   TRUE,  NOW() - INTERVAL '2 days');