

def solution(numbers, hand) :
    result = ''
    pre_left = [(0,0)]
    pre_right = [(2,0)]
    for num in numbers :
        if num == 1 or num == 4 or num == 7 :
            result += 'L'
            if num == 1 : pre_left.append((0,3))
            if num == 4 : pre_left.append((0,2))
            if num == 7 : pre_left.append((0,1))
        elif num == 3 or num == 6 or num == 9 :
            result += 'R'
            if num == 3 : pre_right.append((2,3))
            if num == 6 : pre_right.append((2,2))
            if num == 9 : pre_right.append((2,1))
        else :
            if num == 2 :
                target = [1,3]
                dis_left = abs(target[0] - pre_left[-1][0]) + abs(target[1] - pre_left[-1][1])
                dis_right = abs(target[0] - pre_right[-1][0]) + abs(target[1] - pre_right[-1][1])
                if dis_left > dis_right :
                    result += 'R'
                    pre_right.append((target[0],target[1]))
                elif dis_left < dis_right :
                    result += 'L'
                    pre_left.append((target[0],target[1]))
                else :
                    if hand == "left" :
                        result += 'L'
                        pre_left.append((target[0], target[1]))
                    else :
                        result += 'R'
                        pre_right.append((target[0], target[1]))
            if num == 5 :
                target = [1,2]
                dis_left = abs(target[0] - pre_left[-1][0]) + abs(target[1] - pre_left[-1][1])
                dis_right = abs(target[0] - pre_right[-1][0]) + abs(target[1] - pre_right[-1][1])
                if dis_left > dis_right:
                    result += 'R'
                    pre_right.append((target[0], target[1]))
                elif dis_left < dis_right:
                    result += 'L'
                    pre_left.append((target[0], target[1]))
                else:
                    if hand == "left":
                        result += 'L'
                        pre_left.append((target[0], target[1]))
                    else:
                        result += 'R'
                        pre_right.append((target[0], target[1]))
            if num == 8 :
                target = [1,1]
                dis_left = abs(target[0] - pre_left[-1][0]) + abs(target[1] - pre_left[-1][1])
                dis_right = abs(target[0] - pre_right[-1][0]) + abs(target[1] - pre_right[-1][1])
                if dis_left > dis_right:
                    result += 'R'
                    pre_right.append((target[0], target[1]))
                elif dis_left < dis_right:
                    result += 'L'
                    pre_left.append((target[0], target[1]))
                else:
                    if hand == "left":
                        result += 'L'
                        pre_left.append((target[0], target[1]))
                    else:
                        result += 'R'
                        pre_right.append((target[0], target[1]))
            if num == 0 :
                target = [1,0]
                dis_left = abs(target[0] - pre_left[-1][0]) + abs(target[1] - pre_left[-1][1])
                dis_right = abs(target[0] - pre_right[-1][0]) + abs(target[1] - pre_right[-1][1])
                if dis_left > dis_right:
                    result += 'R'
                    pre_right.append((target[0], target[1]))
                elif dis_left < dis_right:
                    result += 'L'
                    pre_left.append((target[0], target[1]))
                else:
                    if hand == "left":
                        result += 'L'
                        pre_left.append((target[0], target[1]))
                    else:
                        result += 'R'
                        pre_right.append((target[0], target[1]))

    return result

