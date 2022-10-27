def swap_case(s):
    final = ""
    for i in s:
        upper = i.upper()
        lower = i.lower()
        if i == upper:
            final += i.lower()
        elif i == lower:
            final += i.upper()
        else:
            final += i
    return final

