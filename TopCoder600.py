def getMinimum(numbers, goal):
    slimed = []
    for n in numbers:
        if n =< goal:
            slimed.append(n)
    print slimed

getMinimum([1,2,3,4,5,6], 4)