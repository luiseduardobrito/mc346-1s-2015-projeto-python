__author__ = 'danilomendes'


def main():

    chosennumber = input("Enter your input: ")

    print(chosennumber)

    list = [1, 2, 3, 4, 5]
    for number in list:
        if number == float(chosennumber):
            list.remove(number)

    print(list)






if __name__ == "__main__":
    main()

