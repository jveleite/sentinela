from regras import (
    RegraTravadoIntegracao,
    RegraPendenciaVencida,
    RegraInconsistenciaStatus,
)

REGRAS = [
    RegraTravadoIntegracao(horas_limite=6),
    RegraPendenciaVencida(horas_limite=8),
    RegraInconsistenciaStatus(),
]

def avaliar_pedidos(pedidos):
    incidentes = []
    for pedido in pedidos:
        for regra in REGRAS:
            resultado = regra.avaliar(pedido)
            if resultado is not None:
                incidentes.append(resultado)
    return incidentes