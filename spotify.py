#   Written by Sergievsky&Finogenova
#   https://github.com/yepiwt
#   2020

import spotipy
from spotipy.oauth2 import SpotifyOAuth

class smmspotify(object):

	__slots__ = ('client','scope','favs','albums','liked')

	def __init__(self):
		scope = "user-library-read"
		self.client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
		self.liked = []
	
	def make_data_tracks(self,lib):
		for track_info in lib:
			art = ''
			track_name = track_info['track']['name']
		for artist_info in track_info['track']['album']['artists']:
			art += artist_info['name'] + ', '
		art = art[:-2]
		self.favs.append([art,track_name])
		return self.favs

	def get_tracks(self):
		offset = len(self.liked)
		lib = self.client.current_user_saved_tracks(limit=50,offset=offset)['items']
		if len(lib) != 0:
			for track in lib:
				self.liked.append(track)
			get_tracks()
		return self.make_data_tracks(self.liked)

	def get(self):
		self.get_tracks()

if __name__ == "__main__":
	print('This is module smm-spotify. Smoke docs')