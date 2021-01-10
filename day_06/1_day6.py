if __name__ == "__main__":
    questions = []
    count_questions = []
    with open('./input.txt', 'r') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if line != '\n':
            for question in range(0, len(line.strip())):
                if line[question] not in questions:
                    questions.append(line[question])
        
        if len(line.strip()) == 0 or i+1 >= len(lines):
            count_questions.append(len(questions))
            questions = []

    print(sum(count_questions))
