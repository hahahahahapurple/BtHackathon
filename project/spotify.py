import sys
import json
import spotipy
import spotipy.util as util
import os
import getPicture as getPicture
import getEmotion
import makeSpotifyPlaylist
import getTrainingData
import learnSongs

username = "vbbgi9atrwy0u3e7ki3d42fte"

scopes = ("user-read-recently-played"
		  " user-top-read"
		  " user-library-modify"
		  " user-library-read"
		  " user-read-private"
		  " playlist-read-private"
		  " playlist-modify-public"
		  " playlist-modify-private"
		  " user-read-email"
		  " user-read-birthdate"
		  " user-read-private"
		  " user-read-playback-state"
		  " user-modify-playback-state"
		  " user-read-currently-playing"
		  " app-remote-control"
		  " streaming"
		  " user-follow-read"
		  " user-follow-modify")

try:
    token = util.prompt_for_user_token(username, scopes,
                                       client_id='563f890f0bc540309c44d40e35a0a462',
                                       client_secret = '343030b9e9d0440b80bebb96647485af',
                                       redirect_uri='http://google.com/')

except:
	os.remove(".cache-{}".format(username))
	token = util.prompt_for_user_token(username,scopes,
								   client_id='563f890f0bc540309c44d40e35a0a462',
								   client_secret='343030b9e9d0440b80bebb96647485af',
								   redirect_uri='http://google.com/')


if token:
      sp = spotipy.Spotify(auth=token)
      user = sp.current_user()
      while True:
            print("HAHAHAHAHA >:( make the choice")
            print("0 - create plyalist")
            print("1-exit")
            print("")
            choice = input("Your selection:")
            if choice=="0":
                print("Enter happy, angry, sad, or netural. If you dont want to press enter")
                choice = input("Choice: ")
                if choice != '':
                    mood = choice
                else:
                    mood = "getMood.getMood()"
                #jfjsdkfjaslkfjdsf
                model = learnSongs.main()
                makeSpotifyPlaylist.main(sp, user, model, mood)
                print("playlist successfully made")
            if choice == "1":
                 break
