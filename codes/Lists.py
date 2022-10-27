if __name__ == '__main__':
    N = int(input())
    list_ = []
    n = 0
    command = []
    
    while n < N:
        input_ = input()
        if input_[:6] == "insert":
            command = input_.split()
            list_.insert(int(command[1]), int(command[2]))
        elif input_[:5] == "print":
            print(list_)
        elif input_[:6] == "remove":
            command = input_.split()
            list_.remove(int(command[1]))
        elif input_[:6] == "append":
            command = input_.split()
            list_.append(int(command[1]))
        elif input_[:4] == "sort":
            list_.sort()
        elif input_[:3] == "pop":
            command = input_.split()
            list_.pop(-1)
        else:
            list_.reverse()
        n += 1
        
