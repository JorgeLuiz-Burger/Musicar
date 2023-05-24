"""
Arquivo orientado a objeto para descrever as matérias presentes na escola.

    * Informações que se precisa adquirir dos professores:
        1. Nome da matéria
        2. Horário das aulas
        3. Sala utilizada
        4. Nome do professor
        5. Quantidade de estudantes
        6.

    * Ações a se tomar com as matérias?
        1. Adicionar uma turma
        2. Remover uma turma
        4. Alterar o horário
        6. Alterar a sala
        7. Alterar o professor
        8. Adicionar estudantes
        9. Remover estudantes
        10. Alterar o nome da matéria
        11.

"""


class newSubject():

    def __init__(self):
        self.__name = "Nova_Materia"

    def nameIt(self, name):
        self.__name = name


# End of file
