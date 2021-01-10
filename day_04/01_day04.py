def extract_all_passports(passport_file):
    passports = []
    passport = ""

    for i, line in enumerate(passport_file):
        if line != '\n':
            passport += line.strip() + ' '

        if len(line.strip()) == 0 or i+1 >= len(passport_file):
            passports.append(passport)
            passport = ""
            
    
    return passports


if __name__ == "__main__":
    passport_attributes = ['byr', 'iyr', 'eyr', 'hgt',
                           'hcl', 'ecl', 'pid']
    valid_passports = 0
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
        passports = extract_all_passports(lines)

    for passport in passports:
        valid = 1
        validation_passport = {}
        passport_fields = passport.split()

        for field in passport_fields:
            field = field.split(':')
            validation_passport[field[0]] = field[1]

        for attribute in passport_attributes:
            if attribute not in validation_passport:
                valid = 0
                break
        
        valid_passports += valid

    print(valid_passports)
