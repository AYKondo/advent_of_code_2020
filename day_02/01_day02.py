def separate_policy_from_password(line):
    password = line.split(':')
    policy = password[0].split()
    return policy, password[1].strip()

def prepare_policy(raw_policy):
    policy = dict()
    policy_min_max = raw_policy[0].split('-')
    policy['character'] = raw_policy[1]
    policy['min_character'] = int(policy_min_max[0])
    policy['max_character'] = int(policy_min_max[1])

    return policy

def password_validation(password, policy):
    if policy['character'] not in password:
        return 0

    password_letters = dict()

    for char in password:
        if char not in password_letters:
            password_letters[char] = 1
        else:
            password_letters[char] += 1

    if policy['min_character'] <= password_letters[policy['character']] <= policy['max_character']:
        return 1

    return 0


if __name__ == "__main__":
    numbers = list()
    valid_password = 0
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        raw_policy, password = separate_policy_from_password(line)
        policy = prepare_policy(raw_policy)

        valid_password += password_validation(password, policy)
        
    print(valid_password)
