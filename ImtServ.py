def imtCalc(weight, height):
    temp = (height * height)
    imt = weight / temp
    return imt


def imtRez(imt):
    if imt <= 18:
        rez = "У Вас недостаток веса"
    elif imt <= 25:
        rez = "У Вас нормальный вес"
    elif imt <= 30:
        rez = "У Вас избыточный вес"
    else:
        rez = "У Вас ожирение"
    return rez
