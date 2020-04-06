
def plotStats(fileName):
    """
    플레이리스트로부터 정보를 읽어들여서, 플랏 만들기
    """
    plist=plistlib.readPlist(fileName)
    tracks=plist['Tracks']
    ratings=[]
    durations=[]
    for trackId, track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
        except:
            pass

    if ratings==[] or durations==[]:
        print("No valid Album Rating/Total Time data in %s." % fileName)
        return
    x=np.array(durations, np.int32)
    x=x/60000.0
    y=np.array(ratings, np.int32)
    pyplot.subplot(2,1,1)
    pyplot.plot(x,y,'o')
    pyplot.axis([0,1.05*np.max(x),-1,110])
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Track rating')

    pyplot.subplot(2,1,2)
    pyplot.hist(x,bins=20)
    pyplot.xlabel('Track duration')
    pyplot.ylabel('Count')
    pyplot.show()
