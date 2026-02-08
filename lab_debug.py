def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

def main():
    list = [2,3,5,6,8,9]
    result_sum = sum_list(list)
    result_greatest = greatest_number(list)
    print("List: ", list)
    print(result_sum)
    print(result_greatest)

if __name__ == '__main__':
    main()