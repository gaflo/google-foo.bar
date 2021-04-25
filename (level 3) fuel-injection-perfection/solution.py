def solution(n):
    current = int(n)
    counter = 0
    while current > 1:
        if current % 2 == 0:
            current /= 2
        elif 3 & current == 3 and current != 3:
            current += 1
        else:
            current -= 1
        counter += 1
    return counter
    