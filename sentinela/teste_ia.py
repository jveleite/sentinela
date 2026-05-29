from repository import buscar_pedidos
from motor import avaliar_pedidos
from ia import enriquecer_incidentes

pedidos = buscar_pedidos()
incidentes = avaliar_pedidos(pedidos)

# Testa só com o incidente mais grave para economizar tokens
mais_grave = sorted(incidentes, key=lambda i: i.severidade, reverse=True)[0]

print(f"Testando IA com incidente: {mais_grave}")
print("=" * 60)

resultado = enriquecer_incidentes([mais_grave])

for incidente, analise in resultado:
    print(analise)