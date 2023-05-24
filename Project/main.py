from Teachers import Person as teacher


if __name__ == '__main__':
    print("Inciando o processamento.")

    Jorge = teacher.newTeacher()

    Jorge.setName("Jorge Luiz")
    Jorge.setAge(28)

    error = Jorge.verifyData()
    if (error != 0):
        print(f"\n\tErro encontrado {error}")
    else:
        Jorge.showInfo()






# End of file
