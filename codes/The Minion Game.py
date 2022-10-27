def minion_game(string):
    v_count = 0
    c_count = 0
    
    for i in range(len(string)):
        if string[i] in "AEIOU":
            v_count += (len(string) - i)
        else:
            c_count += (len(string) - i)
    
    if v_count > c_count:
        print("Kevin", v_count)
    elif c_count > v_count:
        print("Stuart", c_count)
    else:
        print("Draw")
        
