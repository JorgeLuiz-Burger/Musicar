from Teachers import Person as teacher
import ErrorList


if __name__ == '__main__':
    print("Inciando o processamento.")

    Jorge = teacher.newTeacher()

    Jorge.setName("Jorge Luiz")
    Jorge.setAge(28)
    Jorge.setBirthDay(18, "jan", 1995)
    Jorge.setAddress("R. Daniel rossi", 210, "Ap 206", 95076100)
    Jorge.setCpf("01281156027")
    Jorge.setPhone("51991429087")
    Jorge.setEmail("jorgeluiz.burger@yahoo.com.br")
    Jorge.setBank("01281156027", "Nubank", "01", "000000")
    Jorge.setStartDay(24, "mai", 2023)

    error = Jorge.verifyData()
    if (error != 0):
        print(f"\n\tErro encontrado {error}")

    Jorge.showInfo()






# End of file
