from project import create_app
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import openai
from openai import OpenAI
import jinja2
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_API_URL = "https://api.spotify.com/v1"
SEARCH_ENDPOINT = "/search"
CLIENT_ID = "dcee707a5f2449c8a23dd20234727874"
CLIENT_SECRET = "e0353b0e94af4cfa986484d7b7a3f183"
REDIRECT_URI = 'http://localhost:8080/'
SCOPE = 'playlist-modify-public'

client = OpenAI(api_key='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')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))


def authenticate(client_id, client_secret):
    auth_response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret)
    )
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']
\

# Function to search for a track by name
def search_track(track_name, access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"q": track_name, "type": "track"}
    response = requests.get(
        SPOTIFY_API_URL + SEARCH_ENDPOINT,
        headers=headers,
        params=params
    )
    return response.json()

def create_playlist(user_id, playlist_name, track_ids):
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description = "Test")
    id = playlist['id']
    print(id)
    sp.playlist_add_items(playlist_id=id, items = track_ids)

def makePlaylist(user_id, bye):
    track_id = []
    for i in bye:
        try:
            x = i.index(".")
            songname = i[x+1:]
        except:
            songname = i

        access_token = authenticate(CLIENT_ID, CLIENT_SECRET)
        search_results = search_track(songname, access_token)
        track_id.append("spotify:track:" + search_results["tracks"]["items"][0]["id"])
    print(track_id)
    create_playlist(user_id, "testplaylistNEW7", track_id)

app = create_app()

def getNums():
    nums = []
    for i in range(7):
        item = request.form.get("mood_input_" + str(i + 1))
        nums.append(str(item))
    return nums

@app.route('/', methods=['POST', 'GET'])
def index():
        if request.method == 'GET':
            return render_template('index.html')
        elif request.method == 'POST':
            factors = ["1","1","1","1","1","1","1"]
            nums = getNums()
            paragraph = "Give me a list of songs that meet the criteria on a scale of 0-5. Happy(" + nums[0] + "), Sad(" + nums[1] + "), calm(" + nums[2] + "), energetic(" + nums[3] + "), nostalgic(" + nums[4] + "), romantic(" + nums[5] + "), and inspirational(" + nums[6] + "). Return one string of 8 song titles separated by a semicolon without the artist"
            message = {"role": "user", "content": paragraph}
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages = [{"role": "user", "content": paragraph}]
            )
            item = completion.choices[0].message.content
            print(paragraph)
            print(completion.choices[0].message)
            song_names_str = item.strip('"')  # Remove leading and trailing quotes
            song_names_list = [song.strip() for song in song_names_str.split(';')]
            print(song_names_list)
            makePlaylist('vbbgi9atrwy0u3e7ki3d42fte', song_names_list)

            return redirect('/playlist')
        
@app.route('/playlist', methods=['GET'])
def playlist():
     if request.method == 'GET':
          return render_template('playlist.html')

if __name__ == '__main__':
    app.run(debug=True)
