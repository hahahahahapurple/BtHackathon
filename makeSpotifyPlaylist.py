def getUserHistory(sp, user):
    result = []
    trackURI = []
    tracks = []
    numTracks = 500
    maxObjects = 50
    for i in range(numTracks//maxObjects):
        pastTracks = sp.current_user_saved_tracks(limit=maxObjects,
                                                  offset = i*maxObjects)
        if(pastTracks != None):
            result.append(pastTracks)
    for i in result:
        for j in i['items']:
            trackURI.append(j['track']['uri'])
            tracks.append(j['track']['name']+" by "+ j['track']['artists'][0]['name'])
    return trackURI, tracks

def getAudio(sp, trackURI):
    feature = []
    featureTotal = []
    m = 100
    for i in range(0, len(trackURI), m):
        audio = sp.audio_features(trackURI[i:i+max])
        time.sleep(1)
        for j in range(len(audio)):
            feature.append(audio[j]['danceability'])
            feature.append(audio[j]['energy'])
            feature.append(audio[j]['valence'])
            featureTotal.append(feature)
        feature = []
    return featureTotal
