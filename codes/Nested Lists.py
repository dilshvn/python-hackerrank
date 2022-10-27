if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name,score])
        scores.append(score)
    
    scores = set(scores)
    students.sort()
    scores.remove(min(scores))
    secMin = min(scores)
    
    for i in range(0, len(students)):
        mark = students[i][1]
        if secMin == mark:
            print(students[i][0])
        
        
