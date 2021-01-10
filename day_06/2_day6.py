if __name__ == "__main__":
    questions = list()
    count_questions = []
    with open('./input.txt', 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line != '\n':
            line_questions = set()
            # Criar todos os sets de questoes
            for question in range(0, len(line.strip())):
                line_questions.add(line[question])

            # Adicionar todas as questoes em uma lista
            questions.append(line_questions)

        if len(line.strip()) == 0 or i+1 >= len(lines):
            # Passar os sets como argumento
            common_questions = set.intersection(*questions)
            count_questions.append(len(common_questions))
            questions = list()

    print(sum(count_questions))
