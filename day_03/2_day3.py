if __name__ == "__main__":
    slopes_trees = list()
    total = 1
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    line_size = len(lines[0]) - 1
    terrain_height = len(lines) - 1

    for slope in slopes:
        trees = 0
        position = 0
        right = slope[0]
        down = slope[1]
        line = 0
        while(line < len(lines)):
            if position + right < line_size:
                position += right
            else:
                position = (position + right) - line_size
            
            
            if (line + down) > terrain_height:
                break
            else:
                if lines[line + down][position] == '#':
                    trees += 1
                line += down

        slopes_trees.append(trees)
    
    for tree in slopes_trees:
        total *= tree

    print(total)