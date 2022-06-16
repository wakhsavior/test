import sys

def check_add(used, cab):    # used - заполняемая бухта    cab - текущий кабель
    r = False
    p_used = used + cab      #  Добавляем кабель в бухту для проверки
    p_ost = size - p_used     #   Проверяем остаток после добавления кабеля
    if p_used <= size:          # Проверяем, умещается ли кусок в бухту
        if p_ost <= dopusk:     # Проверяем, находится ли остаток в допуске     
            r = True
        if p_ost >= cab:        # Если остаток  кабеля больше длины самого кабеля
            r = True
    return r


def main(argv):
    num = 100
    summ = 0
    i = 0
    while i <= num:
        summ = summ + i
        print(summ)
        i = i + 1

    print("Сумма всех чисел " + str(num) + " равна: " + str(summ))

if __name__ == "__main__":
    main(sys.argv)