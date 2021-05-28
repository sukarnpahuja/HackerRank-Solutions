if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    scorecard = student_marks[query_name]
    total = 0
    for i in range (len(scorecard)):
        total  = total + scorecard[i]
    output = total/len(scorecard)
    print("{:.2f}".format(output))
