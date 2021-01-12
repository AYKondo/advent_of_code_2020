def execute_command(index, command, acc):
    commands = {
        "nop": execute_nop(acc, index),
        "acc": execute_acc(acc, index, command),
        "jmp": execute_jmp(acc, index, command)
    }

    acc, index = commands[command[0]]

    return acc, index

def execute_nop(acc, index):
    index += 1
    return acc, index

def execute_acc(acc, index, command):
    acc += int(command[1])
    index += 1
    return acc, index

def execute_jmp(acc, index, command):
    index += int(command[1])
    return acc, index

if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
    
    last_command = len(lines)
    nops_and_jmp_to_change = 0
    loop_program = True

    while loop_program:
        nops_and_jmp_to_change += 1
        nops_and_jmp = 0
        comand_indexes = []
        acc = 0
        index = 0

        while True:
            if index >= last_command:
                print(acc)
                loop_program = False
                break

            if index in comand_indexes:
                break

            command = lines[index].split()
            comand_indexes.append(index)

            if command[0] == 'nop' or command[0] == 'jmp':
                nops_and_jmp += 1

                if nops_and_jmp == nops_and_jmp_to_change:
                    switch_command = {
                        "nop": "jmp",
                        "jmp": "nop"
                    }
                    command[0] = switch_command[command[0]]

            acc, index = execute_command(index, command, acc)
