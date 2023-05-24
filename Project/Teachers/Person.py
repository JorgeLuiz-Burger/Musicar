"""
Arquivo orientado a objeto para descrever os professores presentes na escola.

    * Informações que se precisa adquirir dos professores:
        PESSOAIS
        1. Nome completo
        2. Idade
        3. Aniversário
        4. CPF
        5. Telefone para contato
        6. E-mail para contato
        7.

        INSTITUCIONAIS
        1. Data de entrada na escola
        2. Turmas que leciona
        3. Horários ocupados
        4. Salário por aula
        5.

    * Ações a se tomar com os professores?
        1. Adicionar uma turma
        2. Alterar uma turma
        3. Remover uma turma
        4. Adicionar um novo horário ocupado
        5. Alterar um horário ocupado
        6. Remover um horário ocupado
        7. Alterar o salário
        8. Alterar Informações de contato
        9.

"""


class newTeacher():

    def __init__(self):
        self.__name = "Novo_Professor"

    def nameIt(self, name):
        self.__name = name


# End of file
