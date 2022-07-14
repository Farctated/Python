def solution(pegs):
    number_of_pegs = len(pegs)
    for i in range(number_of_pegs):
        print(i)
    gear1 = pegs[0]
    gearN = pegs[number_of_pegs-1]
    print(gearN,gear1)

    space_between_pegs = 0
    # if 1<= gear_size <= space_between_pegs:
    #     pass
solution([4,5,1,2])