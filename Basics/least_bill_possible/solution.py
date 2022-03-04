def solution(str):
    sums = str
    hundred = 0
    fifty = 0
    twenty = 0
    remainder = sums % 100
    if remainder == 30 or remainder == 10:
        hundred = ((sums - remainder) / 100) - 1
        remainder = remainder + 1
        remainder = remainder - 50
        fifty += 1
    elif 30 < remainder<100:
        hundred = ((sums - remainder) / 100)
        twenty = remainder / 20
    else:
        twenty = remainder / 20
    return [round(hundred), round(fifty),round(twenty)]
    
print(solution(270))