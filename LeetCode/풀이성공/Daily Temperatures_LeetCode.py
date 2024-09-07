temperatures = [73,74,75,71,69,72,76,73]

ans = [0] * len(temperatures)
stack = []
for day, temp in enumerate(temperatures) :
    while stack and stack[-1][1] < temp :
        prev_day = stack.pop()[0]           # day를 출력
        ans[prev_day] = day - prev_day
    stack.append((day,temp))
print(ans)
