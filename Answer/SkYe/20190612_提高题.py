def num_sort(num_list):
    odd_numbers, even_numbers = [], []
    for number in num_list:
        if number%2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return odd_numbers+even_numbers


def main():
    num_list = eval(input())
    num_list_sorted = num_sort(num_list)
    print(num_list_sorted)


main()
