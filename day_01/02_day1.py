def find_three_numbers(numbers, target_number):
    know_numbers = list()
    for i in range(0, len(numbers)-1):

        if target_number - numbers[i] in know_numbers:
            return (target_number - numbers[i]) * numbers[i]
            

        know_numbers.append(numbers[i])
    
    return False

if __name__ == "__main__":
    numbers = list()
    multiple_numbers = False
    with open('./input.txt', 'r') as f:
        for currenty_number in f:
            numbers.append(int(currenty_number))

    for i in range(0, len(numbers)):
        curr_sum = 2020 - numbers[i]
        know_numbers = list()
        know_numbers.append(numbers[i])

        for j in range(i+1, len(numbers)):
            if curr_sum - numbers[j] in know_numbers:
                multiple_numbers = (curr_sum - numbers[j]) * numbers[i] * numbers[j]
                break
            know_numbers.append(numbers[j])
        
        if multiple_numbers:
            print(multiple_numbers)
            break
