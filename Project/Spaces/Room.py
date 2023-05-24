"""
Arquivo orientado a objeto para descrever as salas presentes na escola.

    * Informações que se precisa adquirir das salas:
        1. Identificação da sala
        2. Horários utilizados
        3. Horários livres
        4. Capacidade de pessoas
        5. Tamanho da sala
        6. Possíveis aplicações
        7. Situação da sala
        8. Recepção
        9.

    * Ações a se tomar com as matérias?
        1. Alterar a identificação da sala
        2. Adicionar um horário utilizado (Remover um horário livre)
        3. Remover um horário utilizado (Adicionar um horário livre)
        4. Adicionar aplicação
        5. Remover aplicação
        6. Alterar situação da sala
        7.

"""


class newRoom():

    def __init__(self):
        self.__name = "Nova_Sala"

    def nameIt(self, name):
        self.__name = name


# End of file
