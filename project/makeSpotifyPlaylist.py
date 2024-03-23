import numpy as np
import spotipy
import csv
import time
import getEmotion
import sys

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

def createPlaylist(sp, user, trackURI, feature, mood, model):
    features = np.asarray(feature, dtype =np.float32)
    prediction = model.predict(features)
    song = []
    playlistSongs = []
    for i in range(len(prediction)):
        if(prediction[i] == mood):
            playlistSongs.append(trackURI[i])
        if(len(playlistSongs)>10):
            break
    userID = user['id']
    playlist = sp.user_playlist_create(userID, name = mood, public=True)
    playlistID = playlist['id']
    sp.user_playlist_add_tracks(userID, playlistID, playlistSongs)

        
def main(sp, user, model, mood):
    trackURI, tracks = getUserHistory(sp, user)
    feature = getAudio(sp, trackURI)
    createPlaylist(sp, user, trackURI, feature, mood, model)
