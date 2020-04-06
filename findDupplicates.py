#finding dulicates
def findDuplicates(fileName):
    print('finding duplicate tracks in %s...' % fileName)
    #플레이 리스트를 읽는다.
    plist = plistlib.readPlist(fileName)
    #tracks 딕셔너리로부터 트랙을 가져온다.
    tracks=plist['tracks']
    #트랙 이름 (TrackName) 딕셔너리를 만든다.
    trackNames={}
    #트랙을 탐색
    for trackId, track in tracks.items():
        try: #이름과 듀레이션 저장
            name=track['Name']
            duration=track['Total Time']
            if name in trackNames: #이름이 이미 존재한다면 (중복)
                #만약 플레이 시간(duration)도 같다면
                if duration//1000==trackNames[name][0]//1000:
                    count=trackNames[name][1]
                    trackNames[name]=(duration, count+1)
                    #count+1해준다
            else: #이름이 존재하지 않는다면
                trackNames[name]=(duration,1) #새로 넣어준다.
        except:
            pass
