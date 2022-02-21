def solution(plate1,plate2):
    from_char,to_char= "OQITZSB", "0011258" #the  matching index value of @from_char is similar to @to_char
    p1,p2 = plate1, plate2
    for character in from_char:
        replace_with = to_char[from_char.index(character)] #this holds character which needs replacing if found in either plates
        if character in plate1:
            #if @character is found in plate1, we are replacing it with matching index of @to_char
            p1 = p1.replace(character, replace_with)
        if character in plate2:
            p2 = p2.replace(character, replace_with)
    print(p1,p2)
    return p1 == p2

print(solution("BOX","B0X")) #true
print(solution("BOX","B0B")) #false