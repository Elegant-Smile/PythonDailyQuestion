def chose(ask_people=10):
    number = 0
    count = 0
    while True:
        if number == ask_people: break
        gender = input("please input your gender(f:female,m:man)\n")
        gender = gender.strip(' ')
        if gender not in ['f', 'm']:
            print("your gender is illegal\n")
            continue
        age = input("please input your age:(1,120)\n")
        age = int(age.strip(' '))
        if age <= 0 or age >= 120:
            print("your age is illegal\n")
            continue

        number += 1
        if (gender == 'f') and (10 <= age <= 12):
            count += 1
            print("Congratulation,you can jion in us\n")
        else:
            print("Sorry,we need female and that her age is (10,12)\n")
    print(f"{count}\n")


if __name__ == '__main__':
    chose()
