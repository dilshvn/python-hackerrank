if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    maxy = max(arr)
    arr.remove(maxy)
    run = max(arr)
    print(run)
