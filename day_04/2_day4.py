import re

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

def validate_byr(byr):
    if 1920 <= int(byr) <= 2002:
        return True
    return False

def validate_iyr(iyr):
    if 2010 <= int(iyr) <= 2020:
        return True
    return False

def validate_eyr(eyr):
    if 2020 <= int(eyr) <= 2030:
        return True
    return False

def validate_hgt(hgt):
    if (hgt[-2:] == 'cm') and (150 <= int(hgt[:-2]) <= 193):
        return True
    elif (hgt[-2:] == 'in') and (59 <= int(hgt[:-2]) <= 76):
        return True
    
    return False

def validate_hcl(color):
    regex = re.compile(r"^#[0-9a-f]{6}$")
    result = regex.match(color)

    return result != None

def validate_ecl(ecl):
    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True

    return False

def validate_pid(pid):
    regex = re.compile(r"^\d{9}$")
    result = regex.match(pid)
    return result != None

def validate_cid(id):
    return True

if __name__ == "__main__":
    passport_attributes = ['byr', 'iyr', 'eyr', 'hgt',
                           'hcl', 'ecl', 'pid']
    validators = {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid,
        'cid': validate_cid
    }

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
            validation = validators[field[0]](field[1])

            if validation:
                validation_passport[field[0]] = field[1]
            else:
                validation = False
                break
        
        if validation:
            for attribute in passport_attributes:
                if attribute not in validation_passport:
                    valid = 0
                    break
            
            valid_passports += valid

    print(valid_passports)
