import requests

user_id = 'vbbgi9atrwy0u3e7ki3d42fte'
bye = ['1. Let It Be', '2. My Heart Will Go On', '3. I Will Always Love You', '4. Hotel California', '5. Somebody to Love']
#bye = ["1. Let It Be"]


SPOTIFY_API_URL = "https://api.spotify.com/v1"
SEARCH_ENDPOINT = "/search"
CLIENT_ID = "dcee707a5f2449c8a23dd20234727874"
CLIENT_SECRET = "e0353b0e94af4cfa986484d7b7a3f183"
REDIRECT_URI = 'http://localhost:8080/'
SCOPE = 'playlist-modify-public'


def authenticate(client_id, client_secret):
    auth_response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret)
    )
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

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


def create_playlist(search_results):
    song = []
    playlist = []
    for i in range(10):
        playlist.append(trackURI[i])
    userID = user['id']
    playlisteach = sp.user_playlist_create(userID, name = mood, public=True)
    playlistID = playlisteach['id']
    sp.user_playlist_add_tracks(userID, playlistID, playlistSongs)

# Example usage
if __name__ == "__main__":
    for i in bye:
        x = i.index(".")
        songname = i[x+1:]
        access_token = authenticate(CLIENT_ID, CLIENT_SECRET)
        search_results = search_track(songname, access_token)
        print(search_results["tracks"]["items"][0]["album"]["id"])

