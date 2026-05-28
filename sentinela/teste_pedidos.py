from repository import buscar_pedidos

pedidos = buscar_pedidos()

print(f"Total de pedidos encontrados: {len(pedidos)}")
print("-" * 60)

for pedido in pedidos:
    print(pedido)