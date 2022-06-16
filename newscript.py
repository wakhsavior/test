import sys


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