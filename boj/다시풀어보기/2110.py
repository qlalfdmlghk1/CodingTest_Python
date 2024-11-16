n, c = map(int, input().split())
houses = []
for _ in range(n) :
    houses.append(int(input()))
houses.sort()
houses = [1,2,4,8,9]

start = 0
end = n-1
cnt = c-2
result = 0

while start < end :
    mid = (start + end) // 2
    result = max(abs(houses[mid] - houses[start]), abs(houses[end] - houses[mid]))
    if c == 0 :
        break
    print(mid)
    if abs(houses[mid]-houses[start]) >= abs(houses[mid]-houses[end]) :
        end = mid - 1
        cnt -= 1
    else :
        start = mid + 1
        cnt -= 1

print(result)