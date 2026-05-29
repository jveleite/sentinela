from repository import buscar_pedidos
from motor import avaliar_pedidos
from relatorio import imprimir_relatorio, salvar_relatorio

def main():
    print("Sentinela iniciando...")

    pedidos = buscar_pedidos()
    incidentes = avaliar_pedidos(pedidos)

    imprimir_relatorio(pedidos, incidentes)
    salvar_relatorio(pedidos, incidentes)

if __name__ == "__main__":
    main()