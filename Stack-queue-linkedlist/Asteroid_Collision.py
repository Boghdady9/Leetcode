asteroids = [5, 10, -5]
stack = []
for asteroid in asteroids:
    while stack and stack[-1] > 0 and asteroid < 0:
        if stack[-1] == -asteroid:
            stack.pop()
            break
        elif stack[-1] < -asteroid:
            stack.pop()
            continue
        else:
            break
    else:
        stack.append(asteroid)




