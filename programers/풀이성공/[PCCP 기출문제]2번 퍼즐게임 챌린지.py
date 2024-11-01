diffs = [1, 99999, 100000, 99995]
times = [9999, 9001, 9999, 9001]
limit = 3456789012

diffs.insert(0,0)
times.insert(0,0)
puzzleCnt = len(diffs)
levelEnd = max(diffs)
start = 1
end = levelEnd + 1
level = -1
answer = []

while start <= end :
    level = (start + end) // 2
    # print("level",level)
    time = 0
    for j in range(1,puzzleCnt) :
        if diffs[j] <= level :
            time += times[j]
        else :
            time += (((diffs[j] - level) * (times[j] + times[j-1])) + times[j])
    # print("time", time)
    if time <= limit :
        end = level - 1
        answer.append(level)
    else :
        start = level + 1
    # print("start", start)
    # print("end", end)
print(min(answer))