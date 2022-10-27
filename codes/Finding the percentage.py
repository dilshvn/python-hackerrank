if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
       
    query_name = input()
    total = student_marks[query_name]
    avg = 0
    
    for val in total:
        avg += val
    
    #print(total)    
    avg = avg/3
    
    print("{:.2f}".format(avg))
