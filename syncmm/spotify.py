# According to old code-style
# Written by Sergievsky
# https://github.com/yepIwt
# 2021

import spotipy
from librespot.core import Session

class Library:

	__scope = "user-library-read"
	__tracks = []

	def __init__(self, login: str = None, password: str = None, token: str = None):
		if token:
			self.__api = spotipy.Spotify(auth = token)
		else:
			session = Session.Builder().user_pass(login, password).create()
			access_token = session.tokens().get(self.__scope)
			self.__api = spotipy.Spotify(auth = access_token)

	def __process_tracks_data(self, data: list):
		
		results = []

		for track_data in data:
			results.append(
				{
					"title": track_data['track']['name'],
					"album": track_data['track']['album']['name'],
					"artists": [art['name'] for art in track_data['track']['album']['artists']],
					"uri": track_data['track']['uri'],
					"cover_url": track_data['track']['album']['images'][0]['url'],
					"track_num": track_data['track']['track_number'],
				}
			)
		return results

	def __process_albums_data(self, data: list):
		
		result = []

		for track_data in data:
			result.append(
				{
					"album": track_data['album']['name'],
					"artists": [ art['name'] for art in track_data['album']['artists'] ],
					"uri": track_data['album']['uri'],
					"cover_url": track_data['album']['images'][0]['url'],
					"tracks": [
						{
							"title": track_data['name'],
							"artists": [art['name'] for art in track_data['artists']],
							"uri": track_data['uri'],
							"track_num": track_data['track_number'],
						}
						for track_data in track_data['album']['tracks']['items']
					],
				}
			)
		return result

	def __get_liked_tracks(self):
		offset = len(self.__tracks)
		result = self.__api.current_user_saved_tracks(limit=50,offset=offset)['items']
		if result:
			self.__tracks.extend(result)
			self.__get_liked_tracks()
		return self.__process_tracks_data(self.__tracks)

	def __get_user_albums(self):
		offset = len(self.__tracks)
		result = self.__api.current_user_saved_albums(limit = 50, offset = offset)['items']
		if result:
			self.__tracks.extend(result)
			self.__get_user_albums()
		return self.__process_albums_data(self.__tracks)

	def liked(self):
		self.__tracks = []
		return self.__get_liked_tracks()
	
	def albums(self):
		self.__tracks = []
		return self.__get_user_albums()