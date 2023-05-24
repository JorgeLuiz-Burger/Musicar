"""
Arquivo orientado a objeto para descrever os professores presentes na escola.

    * Informações que se precisa adquirir dos professores:
        PESSOAIS
        1. Nome completo
        2. Idade
        3. Aniversário
        4. Endereço
        5. CPF
        6. Telefone para contato
        7. E-mail para contato
        8. Conta bancária e Pix
        9.

        INSTITUCIONAIS
        1. Data de entrada na escola
        2. Turmas que leciona
        3. Horários ocupados
        4. Método de salário (Hora / Alunos)
        5. Salário recebido
        6. Recuperação
        7. Notas enviadas
        8.

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
        self.__address = [dfTxt, dfNumber, dfTxt, dfNumber]  # Street / Number / Complement / CEP
        self.__cpf = dfTxt  # xxx.xxx.xxx-xx
        self.__phone = dfTxt  # (xx) 9xxxx-xxxx
        self.__email = dfTxt  # nome@email.com
        self.__bank = [dfTxt, dfNumber, dfNumber, dfTxt]  # Nome do banco / Agência / Conta / Pix

        self.__startData = [dfNumber, dfNumber, dfNumber]  # Day / Month / Year
        self.__classes = []
        self.__schedule = []
        self.__payment = dfNumber

    def showInfo(self):
        print(f"""
    Profissional {self.__name}, {self.__age} anos de {self.__birthDay[0]}/{self.__birthDay[1]}/{self.__birthDay[2]}.
    
    Endereço: {self.__address[0]}, {self.__address[1]}, {self.__address[2]}, {self.__address[3]}
    CPF: {self.__cpf}
    Telefone: {self.__phone}
    E-Mail: {self.__email}
    
    pix {self.__bank[0]} - Banco {self.__bank[1]}, ag {self.__bank[2]} - conta {self.__bank[3]}
    
    Entrou na Musicar em {self.__startData[0]}/{self.__startData[1]}/{self.__startData[2]}
    
    Leciona as seguintes aulas:
    {self.__classes}
    
    Nos horários:
    {self.__schedule}
    
    Recebendo {self.__payment} por aula. """)

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setBirthDay(self, day, month, year):
        self.__birthDay[0] = day
        self.__birthDay[1] = month
        self.__birthDay[2] = year

    def setAddress(self, street, number, complement, cep):
        self.__address[0] = street
        self.__address[1] = number
        self.__address[2] = complement
        self.__address[3] = str(cep)[:-3] + '-' + str(cep)[-3:]

    def setCpf(self, cpf):
        self.__cpf = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]

    def setPhone(self, phone):
        self.__phone = '(' + phone[:2] + ') ' + phone[2:7] + '-' + phone[7:]

    def setEmail(self, email):
        self.__email = email

    def setBank(self, pix, name, ag, cn):
        self.__bank[0] = pix
        self.__bank[1] = name
        self.__bank[2] = ag
        self.__bank[3] = cn

    def setStartDay(self, day, month, year):
        self.__startData[0] = day
        self.__startData[1] = month
        self.__startData[2] = year

    def setPayment(self, value):
        self.__payment = value

    def verifyData(self):
        if self.__name == dfName:
            return 1

        if self.__age == dfNumber:
            return 2

        if dfNumber in self.__birthDay:
            return 3

        if (dfTxt in self.__address) or (dfNumber in self.__address):
            return 4

        if self.__cpf == dfTxt:
            return 5

        if self.__phone == dfTxt:
            return 6

        if self.__email == dfTxt:
            return 7

        # Erro encontrado, Informações bancárias incorretas
        if (dfTxt in self.__bank) or (dfNumber in self.__bank):
            return 8

        # Erro encontrado, Informações de entrada incorretas
        if dfNumber in self.__startData:
            return 9

        # Erro encontrado, salário não pode ser 0
        if self.__payment == dfNumber:
            return 10

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
