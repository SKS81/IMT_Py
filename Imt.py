import ImtServ

print("Расчёт индекса массы.")
print("Если числа дробные, используйте точку.")
weight = float(input("Укажите Ваш вес в килограммах: "))
height = float(input("Укажите Ваш рост в метрах: "))

imt = int(ImtServ.imtCalc(weight, height))

print("Ваш индекс массы тела = ", imt)
print(ImtServ.imtRez(imt))
