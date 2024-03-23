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
