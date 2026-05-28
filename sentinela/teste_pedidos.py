from repository import buscar_pedidos

pedidos = buscar_pedidos()

print(f"Total de pedidos encontrados: {len(pedidos)}")
print("-" * 60)

for pedido in pedidos:
    id, codigo, tipo, status, horas, pendencias = pedido
    print(f"{codigo} | {tipo} | {status} | {horas:.1f}h | {pendencias} pendência(s)")