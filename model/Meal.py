class Meal:
    def __init__(self, carboidratos, data, horario, refeicao):
        self.carboidratos = carboidratos
        self.data = data
        self.horario = horario
        self.refeicao = refeicao

    def __str__(self):
        return self.carboidratos+ " " + self.data + " " + self.horario + " " + self.refeicao