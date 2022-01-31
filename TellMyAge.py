import datetime


def tellAge(myAge, InYear):
    currentYear = datetime.date.today().year
    return myAge + (InYear - currentYear)


if __name__ == '__main__':
    userInput = int(input("Enter your age or your year of birth: "))
    resultInYear = int(input("Enter the year in which you want to find your age: "))
    if userInput > 1500:
        yearOfBirth = userInput
        if resultInYear < yearOfBirth:
            print("You are not born yet!")
        elif resultInYear - yearOfBirth > 100:
            print("Woohoo You are the oldest one alive!!")
        else:
            print(resultInYear - yearOfBirth)
    elif userInput <= 150:
        age = userInput
        print(tellAge(age, resultInYear))
    else:
        print("Is that a joke? Am i looking dumb?")
