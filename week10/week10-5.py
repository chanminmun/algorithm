#https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    score_table = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(survey)):
        first_type = survey[i][0]
        second_type = survey[i][1]
        choice = choices[i]

        if choice < 4:
            score_table[first_type] += (4 - choice)
        elif choice > 4:
            score_table[second_type] += (choice - 4)

    result = ""

    if score_table['R'] >= score_table['T']:
        result += 'R'
    else:
        result += 'T'

    if score_table['C'] >= score_table['F']:
        result += 'C'
    else:
        result += 'F'

    if score_table['J'] >= score_table['M']:
        result += 'J'
    else:
        result += 'M'

    if score_table['A'] >= score_table['N']:
        result += 'A'
    else:
        result += 'N'

    return result