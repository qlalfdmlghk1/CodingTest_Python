def solution(schedules, timelogs, startday):
    end_times = []
    for schedule in schedules :
        if (schedule + 10) % 100 >= 60 :
            end_time = schedule + 100 - 60
        else :
            end_time = schedule
        end_times.append(end_time + 10)

    answer = len(timelogs)
    for idx,timelog in enumerate(timelogs) :  # idx : n번째 사람
        # print(idx+1, "번째 사람")
        day_num = startday % 7
        for t in timelog:
            # print(end_times[idx], t)

            if 0 < day_num < 6 and end_times[idx] < t :
                answer -= 1
                break
            day_num += 1
            day_num = day_num % 7
            # print("요일", day_num)
    return answer