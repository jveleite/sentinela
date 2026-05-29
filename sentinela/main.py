from repository import buscar_pedidos
from motor import avaliar_pedidos
from relatorio import imprimir_relatorio, salvar_relatorio
from ia import enriquecer_incidentes
from logger import logger


def main():
    logger.info("Sentinela iniciando...")

    logger.info("Buscando pedidos no banco...")
    pedidos = buscar_pedidos()
    logger.info(f"{len(pedidos)} pedido(s) encontrado(s)")

    logger.info("Avaliando regras de negócio...")
    incidentes = avaliar_pedidos(pedidos)
    logger.info(f"{len(incidentes)} incidente(s) detectado(s)")

    imprimir_relatorio(pedidos, incidentes)
    salvar_relatorio(pedidos, incidentes)

    if incidentes:
        logger.info("Enriquecendo incidentes com IA...")
        mais_grave = sorted(incidentes, key=lambda i: i.severidade, reverse=True)[0]
        enriched = enriquecer_incidentes([mais_grave])
        print("\n" + "=" * 60)
        print("        SENTINELA — ANÁLISE DE IA")
        print("=" * 60)
        for incidente, analise in enriched:
            print(f"\nIncidente: {incidente}")
            print("-" * 60)
            print(analise)

    logger.info("Sentinela finalizado.")


if __name__ == "__main__":
    main()