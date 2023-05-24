"""
Arquivo orientado a objeto para descrever os estudantes presentes na escola.

    * Informações que se precisa adquirir dos professores:
        PESSOAIS:
        1. Nome completo
        2. Idade
        3. Aniversário
        4. Nome do responsável
        5. CPF do responsável
        6. Endereço do professor
        7. Telefone para contato
        8. E-mail para contato
        9. Contrato [Asssinado / Renovado]
        10. Assinar

        INSTITUCIONAIS
        1. Data de entrada na escola
        2. Turmas que participa
        3. Pagamento por aula
        4. Possui desconto?
        5. Valor do desconto?
        6. Pagamento total do responsável
        7. Situação atual financeira
        8. Tipo de plano para cada modalidade
        9.

    * Ações a se tomar com os estudantes?
        1. Adicionar em uma turma
        2. Remover de uma turma
        3. Adicionar um valor de pagamento
        4. Alterar um valor de pagamento
        5. Remover um valor de pagamento
        6. Alterar responsável
        7. Alterar Informações de contato
        8.

"""


class newStudent():

    def __init__(self):
        self.__name = "Novo_Estudante"

    def nameIt(self, name):
        self.__name = name


# End of file
