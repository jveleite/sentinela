from repository import buscar_pedidos
from motor import avaliar_pedidos

pedidos = buscar_pedidos()
incidentes = avaliar_pedidos(pedidos)

print(f"Pedidos analisados : {len(pedidos)}")
print(f"Incidentes detectados: {len(incidentes)}")
print("=" * 60)

for incidente in sorted(incidentes, key=lambda i: i.severidade, reverse=True):
    print(incidente)