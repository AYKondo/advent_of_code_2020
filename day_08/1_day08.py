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
    
    comand_indexes = []
    acc = 0
    index = 0

    while True:
        if index in comand_indexes:
            print(acc)
            break

        command = lines[index].split()
        comand_indexes.append(index)

        acc, index = execute_command(index, command, acc)
