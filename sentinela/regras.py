class Incidente:
    def __init__(self, pedido, tipo, severidade, detalhe):
        self.pedido     = pedido
        self.tipo       = tipo
        self.severidade = severidade
        self.detalhe    = detalhe

    def __repr__(self):
        return (f"[SEV {self.severidade}] {self.pedido.codigo} "
                f"| {self.tipo} | {self.detalhe}")


class RegraTravadoIntegracao:
    def __init__(self, horas_limite=6):
        self.horas_limite = horas_limite

    def avaliar(self, pedido):
        if pedido.status_atual != "INTEGRACAO":
            return None
        if pedido.horas_parado > self.horas_limite:
            return Incidente(
                pedido=pedido,
                tipo="TRAVADO_INTEGRACAO",
                severidade=4,
                detalhe=f"Parado há {pedido.horas_parado:.1f}h na integração (limite: {self.horas_limite}h)",
            )
        return None


class RegraPendenciaVencida:
    def __init__(self, horas_limite=8):
        self.horas_limite = horas_limite

    def avaliar(self, pedido):
        if pedido.pendencias_abertas == 0:
            return None
        if pedido.horas_parado > self.horas_limite:
            return Incidente(
                pedido=pedido,
                tipo="PENDENCIA_VENCIDA",
                severidade=3,
                detalhe=f"{pedido.pendencias_abertas} pendência(s) aberta(s) há {pedido.horas_parado:.1f}h",
            )
        return None


class RegraInconsistenciaStatus:
    def avaliar(self, pedido):
        if pedido.status_atual == "APROVADO" and pedido.pendencias_abertas > 0:
            return Incidente(
                pedido=pedido,
                tipo="INCONSISTENCIA_STATUS",
                severidade=5,
                detalhe=f"Pedido APROVADO com {pedido.pendencias_abertas} pendência(s) aberta(s)",
            )
        return None