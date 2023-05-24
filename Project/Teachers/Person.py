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
        7. Conta bancária
        8.

        INSTITUCIONAIS
        1. Data de entrada na escola
        2. Turmas que leciona
        3. Horários ocupados
        4. Salário por aula
        5.

    * Ações a se tomar com os professores?
        1. Adicionar uma turma
        2. Remover uma turma
        3. Adicionar um novo horário ocupado
        4. Alterar um horário ocupado
        5. Remover um horário ocupado
        6. Alterar o salário
        7. Alterar Informações de contato
        8.

"""

dfName = "Novo_Professor"
dfNumber = 0
dfTxt = "To-Do"


class newTeacher():

    global dfName
    global dfNumber
    global dfTxt

    def __init__(self):
        self.__name = dfName
        self.__age = dfNumber
        self.__birthDay = [dfNumber, dfNumber, dfNumber]  # Day / Month / Year
        self.__cpf = dfTxt  # xxx.xxx.xxx-xx
        self.__phone = dfTxt  # (xx) 9xxxx-xxxx
        self.__email = dfTxt  # nome@email.com
        self.__banc = [dfTxt, dfNumber, dfNumber]  # Nome do banco / Agência / Conta

        self.__startData = [dfNumber, dfNumber, dfNumber]  # Day / Month / Year
        self.__classes = []
        self.__schedule = []
        self.__payment = dfNumber

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__name = age

    def setBirthDay(self, day, month, year):
        self.__birthDay[0] = day
        self.__birthDay[1] = month
        self.__birthDay[2] = year

    def setCpf(self, cpf):
        self.__cpf = cpf

    def setPhone(self, phone):
        self.__phone = phone

    def setEmail(self, email):
        self.__email = email

    def setBanc(self, name, ag, cn):
        self.__banc[0] = name
        self.__banc[1] = ag
        self.__banc[2] = cn

        # Erro encontrado, Informações bancárias incorretas
        if dfNumber in self.__startData:
            return 8

    def setStartDay(self, day, month, year):
        self.__startData[0] = day
        self.__startData[1] = month
        self.__startData[2] = year

        # Erro encontrado, Informações de entrada incorretas
        if dfNumber in self.__startData:
            return 8

    def setPayment(self, value):
        self.__payment = value

        # Erro encontrado, salário não pode ser 0
        if self.__payment == dfNumber:
            return 9

    def verifyCreation(self):
        if self.__name == dfName:
            return 1

        if self.__age == dfNumber:
            return 2

        if dfNumber in self.__birthDay:
            return 3

        if self.__cpf == dfTxt:
            return 4

        if self.__phone == dfTxt:
            return 5

        if self.__email == dfTxt:
            return 6

        # Erro encontrado, Informações bancárias incorretas
        if (dfTxt in self.__banc) or (dfNumber in self.__banc):
            return 7

        # Erro encontrado, Informações de entrada incorretas
        if dfNumber in self.__startData:
            return 8

        # Erro encontrado, salário não pode ser 0
        if self.__payment == dfNumber:
            return 9

        return 0

    def addClass(self, name):
        self.__classes.append(name)

        # Organizando a ordem
        self.__classes.sort()

    def removeClass(self, name):
        if name in self.__classes:
            self.__classes.remove(name)

    def addTimeSchedule(self, time):
        self.__schedule.append(time)

        # Organizando a ordem
        self.__schedule.sort()

    def removeTimeSchedule(self, time):
        if time in self.__schedule:
            self.__schedule.remove(time)

    def changeTimeSchedule(self, time, newTime):
        if time in self.__schedule:
            index = self.__schedule.index(time)

            self.__schedule[index] = newTime

            # Organizando a ordem
            self.__schedule.sort()


# End of file
