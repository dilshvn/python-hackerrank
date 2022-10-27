def print_rangoli(size):
    alp = " abcdefghijklmnopqrstuvwxyz"
    
    for i in range(size, 0, -1):
        c = alp[size:i:-1] + alp[i:size+1]
        c = "-".join(c)
        print(c.center((size*4)-3, "-"))
    
    for i in range(size-1):
        c = alp[size:i+2:-1] + alp[i+2:size+1]
        c = "-".join(c)
        print(c.center((size*4)-3, "-"))
        
        
