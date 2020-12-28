#   Written by Sergievsky&Finogenova
#   https://github.com/yepiwt/syncmm
#   2020


from vk_api import VkApi
from vk_api import audio
import asyncio

class smmvk(object):

	__slots__ = ('client','vk_audio','albums','favs','playlists')

	def __init__(self,login,password):
		vk_session = VkApi(login=login, password=password)
		vk_session.auth()
		self.client = vk_session.get_api()
		self.vk_audio = audio.VkAudio(vk_session)

	async def check_availability(self,owner_id):
		try:
			self.vk_audio.get(owner_id=owner_id)
		except:
			print('Access Denied or Empty')
			exit()

	async def main(self,owner_id=None):
		await self.check_availability(owner_id)
		await self.get_favs(owner_id)
		await self.get_albums_with_playlists(owner_id)
		
	def get(self):
		asyncio.run(self.main())
		return True

	async def get_favs(self,owner_id):
		self.favs = []
		for song in self.vk_audio.get(owner_id):
			arg = {
				'artist': song['artist'],
				'title': song['title'],
				'link': song['url'],
			}
			self.favs.append(arg)
		return self.favs

	async def get_albums_with_playlists(self,owner_id):
		self.albums = []
		self.playlists = []
		songs = []
		for obj in self.vk_audio.get_albums(owner_id = owner_id):
			album_songs_info = self.vk_audio.get(album_id=obj['id'],owner_id=obj['owner_id'],access_hash=obj['access_hash'])
			if album_songs_info != []: #Если с альбомом что-то произошло
				if obj['owner_id'] > 0: # Это плейлист
					for playlist_songs in album_songs_info:
						track = {
							'artist': playlist_songs['artist'],
							'title': playlist_songs['title'],
							'link': playlist_songs['url']
                        }
						songs.append(track)
					author_iter = self.client.users.get(user_ids = obj['owner_id'])[0]
					author = author_iter['first_name'] + ' ' + author_iter['last_name']
					arg = {
						'title': obj['title'],
						'author': author,
						'tracks': songs,
					}
					self.playlists.append(arg)
				else:
					for album_songs in album_songs_info:
						track = {
							'title': album_songs['title'],
							'link': album_songs['url']
							}
						songs.append(track)
					arg = {
						'title': obj['title'],
						'author': album_songs_info[0]['artist'],
						'tracks': songs,
					}
					self.albums.append(arg)
			songs = []
		return self.albums, self.playlists

if __name__ == "__main__":
	print('This is module smm-vk. Smoke docs')
