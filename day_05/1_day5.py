def extract_row(boarding_pass):
    letter_position = {
        "B": extract_upper,
        "F": extract_low
    }
    row = [i for i in range(0, 128)]

    for i in range(0, len(boarding_pass)):
        row = letter_position[boarding_pass[i]](row)

    return row[0]

def extract_colunm(boarding_pass):
    letter_position = {
        "R": extract_upper,
        "L": extract_low
    }
    colunm = [i for i in range(0, 8)]

    for i in range(0, len(boarding_pass)):
        colunm = letter_position[boarding_pass[i]](colunm)

    return colunm[0]

def extract_upper(row):
    return row[int(len(row)/2):]

def extract_low(row):
    return row[:int(len(row)/2)]

if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
    
    seats = []
    highest_seat = 0

    for boarding_pass in lines:
        row = extract_row(boarding_pass[:7])
        column = extract_colunm(boarding_pass[7:].strip())

        seat = (row * 8) + column
        if seat > highest_seat:
            highest_seat = seat
    
    print(highest_seat)