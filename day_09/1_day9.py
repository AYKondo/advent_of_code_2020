def validate_new_number(number_list, validate_number):
    know_numbers = []
    for number in number_list:
        second_number = validate_number - number
        if second_number in know_numbers:
            return True

        know_numbers.append(number)
    
    return False

if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
    
    start = 0
    end = 25
    valid_numbers = []
    lines = [int(line) for line in lines]

    for line in lines:
        if len(valid_numbers) < 25:
            valid_numbers.append(line)
        else:
            valid_numbers = lines[start:end]

            if validate_new_number(valid_numbers, lines[end]):
                start += 1
                end += 1
            else:
                print(line)
                break