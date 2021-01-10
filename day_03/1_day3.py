if __name__ == "__main__":
    trees = 0
    position = 0
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    line_size = len(lines[0]) - 1
    terrain_height = len(lines) - 1

    for line in range(0, len(lines)):
        if position + 3 < line_size:
            position += 3
        else:
            position = (position + 3) - line_size
        
        
        if line != terrain_height:
            if lines[line + 1][position] == '#':
                trees += 1
    
    print(trees)