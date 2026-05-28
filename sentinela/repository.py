from db import get_connection
from models import Pedido

def buscar_pedidos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            pv.id,
            pv.codigo,
            pv.tipo_fluxo,
            pv.status_atual,
            EXTRACT(EPOCH FROM (NOW() - pv.atualizado_em))/3600 AS horas_parado,
            COUNT(p.id) FILTER (WHERE p.resolvida = FALSE) AS pendencias_abertas
        FROM pedido_venda pv
        LEFT JOIN pendencia p ON p.pedido_id = pv.id
        GROUP BY pv.id, pv.codigo, pv.tipo_fluxo, pv.status_atual, pv.atualizado_em
        ORDER BY horas_parado DESC
    """)

    pedidos = [Pedido(*linha) for linha in cursor.fetchall()]
    cursor.close()
    conn.close()
    return pedidos