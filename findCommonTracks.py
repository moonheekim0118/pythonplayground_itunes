#finding common tracks
def findCommonTracks(fileNames):
    """
    주어진 파일 내에서 중복된 트랙을 찾고,
    common.txt에 저장한다.
    """
    trackNamesSets=[]
    for fileName in fileNames: #파일 이름 탐색
        trackNames=set()
        plist=plistlib.readPlist(fileName) #파일 읽기
        tracks=plist['Tracks']
        for trackId, track in tracks.items():
            try:
                trackNames.add(track['Name'])
            except:
                pass
        trackNamesSets.append(trackNames)
        commonTracks=set.intersection(*trackNamesSets) #중복된것 찾기
        if len(commonTracks) > 0: #중복된게 1개 이상
            f = open("common.txt", 'w') #common.txt에 입력
            for val in commonTracks:
                s="%s\n" % val
                f.write(s.encode("UTF-8"))
            f.close()
            print("%d common tracks found. "
                  "Track names written to common.txt" % len(commonTracks))
        else: #중복된게 없다면
            print("No common Tracks!")
