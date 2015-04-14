__author__ = 'danilomendes'

class Struct:
    def __init__(self, char, number):
        self.char = char
        self.number = number


def main():

    chosenstring = input("Enter your input: ")

    count = 0
    charanterior = chosenstring[0]
    list = []

    for c in str(chosenstring):
        if(c == charanterior):
            count = count + 1
        else:
            list.append(Struct(charanterior, count))
            count = 1
            charanterior = c


    list.append(Struct(charanterior, count))
    for item in list:
        print("("+item.char + " , " + str(item.number)+ ")")

if __name__ == "__main__":
    main()