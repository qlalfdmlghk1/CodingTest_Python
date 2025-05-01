def solution(m, musicinfos):
    answer_list = []
    musics = []

    m = m.replace('A#', 'M')
    m = m.replace('B#', 'L')
    m = m.replace('C#', 'H')
    m = m.replace('D#', 'I')
    m = m.replace('F#', 'J')
    m = m.replace('G#', 'K')
    m = m.replace('E#', 'M')

    for idx,musicinfo in enumerate(musicinfos) :
        music = musicinfo.split(',')
        musics.append(music)  # 시작 시간, 끝나는 시간, 음악 제목, 악보 정보
        for music in musics :
            hour1,minute1 = music[0].split(':')
            hour2,minute2 = music[1].split(':')
            time = int(hour2) * 60 + int(minute2) - (int(hour1) * 60 + int(minute1))  # 전체 시간
            music[3] = music[3].replace('A#', 'M')
            music[3] = music[3].replace('B#', 'L')
            music[3] = music[3].replace('C#', 'H')
            music[3] = music[3].replace('D#', 'I')
            music[3] = music[3].replace('F#', 'J')
            music[3] = music[3].replace('G#', 'K')
            music[3] = music[3].replace('E#', 'M')

            if time > len(music[3]) :
                music[3] = music[3] * ((time // len(music[3])) + 1)
            music[3] = music[3][:time]
            # print(music[3])
            if m in music[3] :
                answer_list.append((time,idx,music[2]))

    if not answer_list :
        answer = '(None)'
    else :
        answer_list.sort(key=lambda x : (-x[0], x[1]))
        answer = answer_list[0][2]

    return answer