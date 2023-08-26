salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500

Qual a forma correta de executar a função:
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel)