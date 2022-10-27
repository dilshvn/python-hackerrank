if __name__ == '__main__':
    s = input()
    alnum = 0
    alpha = 0
    digit = 0
    lower = 0
    upper = 0
    
    for i in s:
        if i.isalnum() == True:
            alnum += 1
        if i.isalpha() == True:
            alpha += 1
        if i.isdigit() == True:
            digit += 1
        if i.islower() == True:
            lower += 1
        if i.isupper() == True:
            upper += 1
    
    print(bool(alnum))
    print(bool(alpha))
    print(bool(digit))
    print(bool(lower))
    print(bool(upper))
    
