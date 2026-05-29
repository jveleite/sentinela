from datetime import datetime


def gerar_relatorio(pedidos, incidentes):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    linhas = []
    linhas.append("=" * 60)
    linhas.append("        SENTINELA — RELATÓRIO DE INCIDENTES")
    linhas.append(f"        Gerado em: {agora}")
    linhas.append("=" * 60)
    linhas.append(f"  Pedidos analisados  : {len(pedidos)}")
    linhas.append(f"  Incidentes detectados: {len(incidentes)}")
    linhas.append("=" * 60)

    if not incidentes:
        linhas.append("  Nenhum incidente detectado. Fluxo saudável.")
    else:
        severidade_atual = None
        for incidente in sorted(incidentes, key=lambda i: i.severidade, reverse=True):
            if incidente.severidade != severidade_atual:
                severidade_atual = incidente.severidade
                linhas.append(f"\n  [ SEVERIDADE {severidade_atual} ]")
                linhas.append("  " + "-" * 56)
            linhas.append(f"  Pedido  : {incidente.pedido.codigo} ({incidente.pedido.tipo_fluxo})")
            linhas.append(f"  Tipo    : {incidente.tipo}")
            linhas.append(f"  Detalhe : {incidente.detalhe}")
            linhas.append("")

    linhas.append("=" * 60)
    return "\n".join(linhas)


def imprimir_relatorio(pedidos, incidentes):
    print(gerar_relatorio(pedidos, incidentes))


def salvar_relatorio(pedidos, incidentes, caminho="relatorio.txt"):
    conteudo = gerar_relatorio(pedidos, incidentes)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    print(f"Relatório salvo em: {caminho}")