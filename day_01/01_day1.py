def find_two_number(numbers, target_number):
    know_numbers = list()
    for i in range(0, len(numbers)-1):

        if target_number - numbers[i] in know_numbers:
            return (target_number - numbers[i]) * numbers[i]
            

        know_numbers.append(numbers[i])

if __name__ == "__main__":
    numbers = list()
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    for currenty_number in lines:
        numbers.append(int(currenty_number))
        
    print(find_two_number(numbers, 2020))
