def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    mcount, hcount = 0,0
    start_time = h1 * 3600 + m1 * 60 + s1
    end_time = h2 * 3600 + m2 * 60 + s2

    if start_time == 0 or start_time == 3600 * 12:
        answer += 1

    for time in range(start_time, end_time):
        cur_s = (time * 6) % 360
        cur_m = (time / 10) % 360
        cur_h = (time / 120) % 360

        nex_s = 360 if (time+1) * 6 % 360 == 0 else (time+1) * 6 % 360
        nex_m = 360 if (time+1) / 10 % 360 == 0 else (time+1) / 10 % 360
        nex_h = 360 if (time+1) / 120 % 360 == 0 else (time+1) / 120 % 360
        
        if cur_s < cur_h and nex_s >= nex_h :
            hcount += 1
        if cur_s < cur_m and nex_s >= nex_m :
            mcount += 1
        if nex_s == nex_m == nex_h :
            answer -= 1
    answer += mcount + hcount
    return answer