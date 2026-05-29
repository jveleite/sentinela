from repository import buscar_pedidos
from motor import avaliar_pedidos
from relatorio import imprimir_relatorio, salvar_relatorio
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

    logger.info("Sentinela finalizado.")


if __name__ == "__main__":
    main()