import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sentinela'))

from models import Pedido
from regras import (
    RegraTravadoIntegracao,
    RegraPendenciaVencida,
    RegraInconsistenciaStatus,
)


# ── Fábrica de pedidos para testes ──────────────────────────
def make_pedido(status, horas_parado, pendencias_abertas=0, tipo="PF"):
    return Pedido(
        id=1,
        codigo="TEST-001",
        tipo_fluxo=tipo,
        status_atual=status,
        horas_parado=horas_parado,
        pendencias_abertas=pendencias_abertas,
    )


# ── RegraTravadoIntegracao ───────────────────────────────────
def test_travado_integracao_dispara():
    pedido = make_pedido("INTEGRACAO", horas_parado=10)
    regra = RegraTravadoIntegracao(horas_limite=6)
    resultado = regra.avaliar(pedido)
    assert resultado is not None
    assert resultado.severidade == 4
    assert resultado.tipo == "TRAVADO_INTEGRACAO"


def test_travado_integracao_dentro_do_limite():
    pedido = make_pedido("INTEGRACAO", horas_parado=3)
    regra = RegraTravadoIntegracao(horas_limite=6)
    resultado = regra.avaliar(pedido)
    assert resultado is None


def test_travado_integracao_status_diferente():
    pedido = make_pedido("ANALISE", horas_parado=10)
    regra = RegraTravadoIntegracao(horas_limite=6)
    resultado = regra.avaliar(pedido)
    assert resultado is None


# ── RegraPendenciaVencida ────────────────────────────────────
def test_pendencia_vencida_dispara():
    pedido = make_pedido("ANALISE", horas_parado=10, pendencias_abertas=2)
    regra = RegraPendenciaVencida(horas_limite=8)
    resultado = regra.avaliar(pedido)
    assert resultado is not None
    assert resultado.severidade == 3
    assert resultado.tipo == "PENDENCIA_VENCIDA"


def test_pendencia_vencida_sem_pendencias():
    pedido = make_pedido("ANALISE", horas_parado=10, pendencias_abertas=0)
    regra = RegraPendenciaVencida(horas_limite=8)
    resultado = regra.avaliar(pedido)
    assert resultado is None


def test_pendencia_vencida_dentro_do_limite():
    pedido = make_pedido("ANALISE", horas_parado=5, pendencias_abertas=1)
    regra = RegraPendenciaVencida(horas_limite=8)
    resultado = regra.avaliar(pedido)
    assert resultado is None


# ── RegraInconsistenciaStatus ────────────────────────────────
def test_inconsistencia_aprovado_com_pendencia():
    pedido = make_pedido("APROVADO", horas_parado=1, pendencias_abertas=1)
    regra = RegraInconsistenciaStatus()
    resultado = regra.avaliar(pedido)
    assert resultado is not None
    assert resultado.severidade == 5
    assert resultado.tipo == "INCONSISTENCIA_STATUS"


def test_inconsistencia_aprovado_sem_pendencia():
    pedido = make_pedido("APROVADO", horas_parado=1, pendencias_abertas=0)
    regra = RegraInconsistenciaStatus()
    resultado = regra.avaliar(pedido)
    assert resultado is None