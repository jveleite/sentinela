class Pedido:
    def __init__(self, id, codigo, tipo_fluxo, 
                 status_atual, horas_parado, pendencias_abertas):
        self.id                = id
        self.codigo            = codigo
        self.tipo_fluxo        = tipo_fluxo
        self.status_atual      = status_atual
        self.horas_parado      = float(horas_parado)
        self.pendencias_abertas = int(pendencias_abertas)

    def __repr__(self):
        return (f"Pedido({self.codigo} | {self.tipo_fluxo} | "
                f"{self.status_atual} | {self.horas_parado:.1f}h | "
                f"{self.pendencias_abertas} pendência(s))")