first = int(input ("Первое число: "))
second = int(input ("Второе число: "))
third = int(input ("Третье число: "))
if first == second and first == third:
    print("ТРИ")
elif first == second or first == third or second == third:
    print("ДВА")
else:
    print("НОЛЬ")# Поставил буквенное значение в команде вывода
    # чисто ради интереса, уж не обессудьте))
