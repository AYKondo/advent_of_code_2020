def validate_new_number(number_list, validate_number):
    know_numbers = []
    for number in number_list:
        second_number = validate_number - number
        if second_number in know_numbers:
            return True

        know_numbers.append(number)
    
    return False

def find_contiguos_set(number_set, contiguos_number):
    final_set = 2
    for i, number in enumerate(number_set):
        while sum(number_set[i:final_set]) < contiguos_number:
            final_set += 1
        
        if sum(number_set[i:final_set]) == contiguos_number:
            return number_set[i:final_set]



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
                contiguos_number = line
                print(line)
                break

    contiguos_set = sorted(find_contiguos_set(lines[:end], contiguos_number))

    print(contiguos_set[0] + contiguos_set[-1])
